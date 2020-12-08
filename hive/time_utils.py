# coding=utf-8
"""时间工具类"""

import datetime
from datetime import datetime as dt


# 返回距离现在n天到距离现在m天的一个列表(n>m)
def last_n2m_day(n, m):
    if n > m:
        res = []
        begin = dt.now()

        for i in range(m, n):
            day = (begin - datetime.timedelta(i)).strftime('%Y%m%d')
            res.append(day)
        return res

    else:
        print("输入有误")


# 返回最近n天的一个列表
def last_n_day(n):
    res = []
    begin = dt.now()

    for i in range(n):
        day = (begin - datetime.timedelta(i)).strftime('%Y%m%d')
        res.append(day)

    return res


# 返回距离现在的第n天
def some_day(n):
    begin = dt.now()
    someday = (begin - datetime.timedelta(n)).strftime('%Y%m%d')
    return someday


# 昨天
def yesterday():
    return some_day(1)


# 时分秒
def now_time():
    return dt.now().strftime('%H:%M:%S')


def main():
    res1 = last_n2m_day(208, 1)
    res2 = last_n2m_day(128, 1)


if __name__ == '__main__':
    main()
