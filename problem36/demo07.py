# coding:utf8
from math import sqrt


def main():
    # 题目：判断101-200之间有多少个素数，并输出所有素数。
    for i in range(101, 200):
        flag = 1
        k = int(sqrt(i))
        for j in range(2, k + 1):
            if i % j == 0:
                flag = 0
                break
        if flag == 1:
            print('%5d' % i)


if __name__ == '__main__':
    main()
