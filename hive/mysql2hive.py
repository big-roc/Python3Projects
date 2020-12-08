# coding=utf-8
import os
import sys
import importlib

from hive.common_func import execute_hql
from hive.time_utils import yesterday

importlib.reload(sys)


def juder_data(table, date):
    wc_command = 'hadoop fs -ls /user/log/kangaroos/' + table + '/' + date + '/ | wc -l'
    file_num = os.popen(wc_command).read()
    return file_num


def add_partition(table, date):
    # 添加分区
    add = 'alter table fin_loan.' + table + ' add partition (data_date=' + date + ')'
    res = execute_hql(add)
    if res != 0:
        return res


def copy_hdfs_data(table, date):
    cp_command = 'hadoop fs -cp /user/log/kangaroos/' + table + '/' + date + '/* /user/hive/warehouse/fin_loan.db/' + table + '/data_date=' + date
    print('命令执行返回码: ', os.system(cp_command))


def main():
    # 表清单
    table_list_p1 = ['tcm_phone_operator', 'tcm_phone_operator_detail', 'tcm_phone_operator_proc', 'tcm_txn_jrnl']

    table_list_p2 = ['tcm_credit_card_mail', 'tcm_credit_card_mail_detail', 'tcm_credit_card_mail_proc',
                     'tcm_face', 'tcm_face_detail', 'tcm_face_video', 'tcm_face_video_detail', 'tcm_id_card_ocr',
                     'tcm_id_card_ocr_detail', 'tcm_phone', 'tcm_phone_detail', 'tcm_taobao', 'tcm_taobao_detail',
                     'tcm_taobao_proc']

    # 表清单
    table_list = table_list_p1 + table_list_p2
    # 时间列表
    date = yesterday()

    # 先创建分区
    for table in table_list:
        # 判断是否有数据更新
        res = juder_data(table, date).rstrip()
        if res != '0':
            # 创建分区
            add_partition(table, date)
            # 拷贝数据
            copy_hdfs_data(table, date)
        else:
            print('数据没有更新!')
    return


if __name__ == '__main__':
    # python2.7 mysql2hive.py > mysql2hive.log 2>&1 &
    main()
