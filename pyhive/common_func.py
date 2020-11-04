# coding=utf-8
"""
author: roc
version: 20180319
description: Python 操作 Hive 的基本功能函数
"""

import importlib
import sys
import os
import requests
from time import ctime

importlib.reload(sys)  # python2的写法:reload(sys) sys.setdefaultencoding("utf-8")

__all__ = ["execute_hql", "find_abnormal", "send_alert"]

hql_config = os.path.join(os.path.dirname(__file__), 'set_macro_func.sql')


# linux 连接 hive
def execute_hql(hql):
    print(hql)
    status = os.system("beeline -i %s -e \" %s\"" % (hql_config, hql))
    return status


# 查询异常
def find_abnormal(hql):
    print(hql)
    res = os.popen("beeline -e \" %s\"" % hql).read().strip()
    return int(res)


# 实时告警
def send_alert(tag, alert):
    """ wrap alert message with time and header, then send it to iPortal
        @alert :: string
    """
    return requests.post('http://nfjd-alert.jpushoa.com/v1/alert/',
                         json={
                             "code": 624,
                             "desc": u" ".join(
                                 [tag, u"\napp-stats:", ctime(), u"\n", alert]
                             )
                         })
