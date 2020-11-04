# coding:utf8
import datetime


def main():
    # 题目：输入某年某月某日，判断这一天是这一年的第几天？
    dtstr = str(input('Enter the datetime(20200628): '))
    dt = datetime.datetime.strptime(dtstr, "%Y%m%d")
    another_dtstr = dtstr[:4] + '0101'
    another_dt = datetime.datetime.strptime(another_dtstr, "%Y%m%d")
    print(int((dt - another_dt).days) + 1)


if __name__ == '__main__':
    main()
