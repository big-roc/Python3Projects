# coding:utf8

import os
from os.path import abspath
from pyspark.sql import SparkSession

# os.environ["SPARK_HOME"] = "D:/software/spark-2.4.2-bin-hadoop2.7"
warehouse_location = abspath('/user/hive/warehouse')


def main():
    spark = SparkSession \
        .builder \
        .appName("Spark on Hive") \
        .master("local[*]") \
        .enableHiveSupport() \
        .getOrCreate()

    df = spark.sql('select * from dp_test.test limit 10')
    df.show(truncate=False)

    spark.stop()

    # 转为pandas的dataframe
    pd = df.toPandas()


if __name__ == '__main__':
    main()
