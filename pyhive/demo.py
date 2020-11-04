# coding=utf-8
import sys
import importlib
from pyhive.common_func import execute_hql
from pyhive.time_utils import last_n2m_day
from multiprocessing import Pool

importlib.reload(sys)


def create_tables():
    sql = '''
            create table if not exists tmp.roc_20190620(
            uid          string,
            platform     string,
            rid          string,
            imei         string,
            token        string
            )
            comment '临时表'
            partitioned by (data_date bigint comment '日期')
            stored as parquet
          '''
    execute_hql(sql)


def jd_dsp_data(param):
    sql = '''
            insert overwrite table dsg.{app_name} partition(data_date={data_date}) 
            select app_key, platform, msg_id, uid, itime, step, error_code
                FROM edw.msg_life_cycle_log
                WHERE platform = 'i'
                    AND data_date = {data_date}
                    AND error_code = -17
          '''.format(**param)
    res = execute_hql(sql)
    if res != 0:
        return res


def main():
    # 建表
    # create_tables()

    # 定义时间列表
    n2m_day = last_n2m_day(246, 1)
    # print(n2m_day)

    params = list()
    for run_day in n2m_day:
        param = dict()
        param['data_date'] = run_day
        param['app_name'] = "msg_life_cycle_log_ios"
        params.append(param)

    pool = Pool(7)
    pool.map(jd_dsp_data, params)
    pool.close()
    pool.join()
    return


if __name__ == '__main__':
    # python2.7 demo.py > demo.log 2>&1 &
    main()
