# coding:utf8

import os
import json
import requests
import datetime
from os.path import abspath
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, ArrayType

os.environ["SPARK_HOME"] = "D:/software/spark-2.4.2-bin-hadoop2.7"
warehouse_location = abspath('/user/hive/warehouse')


def analyse(property_value):
    try:
        analyse_url = 'http://192.168.0.102/cerebrum/ai/analytic'
        headers = {'Content-Type': 'application/json'}
        bom = {
            "rowList": [
                {
                    "row_index": 1,
                    "row_content": [str(property_value)]
                }
            ],
            "env": "clean"
        }
        r = requests.post(analyse_url, data=json.dumps(bom), headers=headers)
        json_str = r.json()
        parameter = json_str['data'][0]['row_data']['parameter']
        return parameter
    except Exception as err:
        print(err)
    return None


def standard_property_concat(json_str, concat_sep):
    res = []
    standardParameter = json_str['data']
    # print(standardParameter)

    if standardParameter:
        for i in standardParameter:
            res.append(i['standard'])
    else:
        res = None

    res_len = 0
    if res:
        res_len = len(res)

    if concat_sep and res_len > 1:
        res_str = concat_sep.join(res)
    elif res_len > 1:
        # 去重
        res = list(set(res))
        res_str = ' '.join(res)
    elif res_len == 1:
        res_str = ''.join(res)
    else:
        return None
    # print(res_str)
    return res_str


def standard_property_value(property_value_tmp, concat_sep, category_id):
    property_value_tmp = list(set(property_value_tmp))
    try:
        transform_url = 'http://192.168.0.125:8101/bdp/test/chip/terms/standardizing?thirdCategoryId=%s' % category_id
        headers = {'Content-Type': 'application/json'}
        r = requests.post(transform_url, data=json.dumps(property_value_tmp), headers=headers)
        json_str = r.json()
        # print(json_str)
        return standard_property_concat(json_str, concat_sep)
    except Exception as err:
        print(err)
    return None


def func_time(func):
    def wrapper():
        start_time = datetime.datetime.now()
        func()
        end_time = datetime.datetime.now()
        print(end_time - start_time)

    return wrapper


@func_time
def main():
    spark = SparkSession \
        .builder \
        .appName("Standard Property") \
        .config("spark.sql.warehouse.dir", warehouse_location) \
        .enableHiveSupport() \
        .getOrCreate()

    create_table = """
    create table if not exists dm.t_product_property2_tmp(
    part_number string comment '型号',
    standard_brand_id string comment '标准品牌id',
    standard_brand_name string comment '标准品牌名称',
    category_id string comment '知识库分类id',
    category_name string comment '知识库分类名称',
    param_name string comment '知识库参数名称',
    property_value string comment '第三方属性值',
    property_value_tmp array<string> comment '分词属性值',
    standard_property_value string comment '标准化属性值'
    )
    comment '产品属性表'
    partitioned by (third_platform_name string comment '第三方平台名称',data_date string comment '数据时间:20201104')
    row format delimited fields terminated by '\001'
    stored as textfile;
    """

    query_sql = """
    select
        part_number,
        standard_brand_id,
        standard_brand_name,
        category_id,
        category_name,
        param_name,
        concat_sep,
        property_value
    from dwd.mouser_spider_table10_tmp_tmp
    where property_value!='-'
    """

    df = spark.sql(query_sql)
    df.show(truncate=False)

    # 调用类目预测的接口，按行调用
    pd = df.toPandas()

    rows_len = pd.shape[0]
    batch = 1000
    n = int(rows_len / batch + 1)

    for i in range(n):
        print(i)
        start = i * batch
        end = (i + 1) * batch - 1
        pd_new = pd.loc[start:end].copy()
        # print(pd_new)
        # 调用分词接口
        pd_new.loc[:, 'property_value_tmp'] = pd_new.apply(lambda row: analyse(row['property_value']), axis=1)
        # print(pd_new)

        # 调用标准化接口
        pd_new.loc[:, 'standard_property_value'] = pd_new.apply(
            lambda row: standard_property_value(row['property_value_tmp'], row['concat_sep'], row['category_id']),
            axis=1)

        # 创建临时表
        schema = StructType([StructField("part_number", StringType(), True),
                             StructField("standard_brand_id", StringType(), True),
                             StructField("standard_brand_name", StringType(), True),
                             StructField("category_id", StringType(), True),
                             StructField("category_name", StringType(), True),
                             StructField("param_name", StringType(), True),
                             StructField("concat_sep", StringType(), True),
                             StructField("property_value", StringType(), True),
                             StructField("property_value_tmp", ArrayType(StringType()), True),
                             StructField("standard_property_value", StringType(), True)])
        df = spark.createDataFrame(pd_new, schema=schema)
        df.show(truncate=False)
        df.createTempView("tmp_table1")

        # 插入数据
        insert_sql = """
        insert into table dm.t_product_property2_tmp partition(third_platform_name='Mouser',data_date='20201125')
        select
            part_number,
            standard_brand_id,
            standard_brand_name,
            category_id,
            category_name,
            param_name,
            property_value,
            property_value_tmp,
            standard_property_value
        from tmp_table1
        """
        spark.sql(insert_sql)
        spark.catalog.dropTempView("tmp_table1")

        # 关闭spark
    spark.stop()


if __name__ == '__main__':
    main()
