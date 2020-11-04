# coding:utf8
import math


def is_sqr(n):
    a = int(math.sqrt(n))
    return a * a == n


def main():
    # 题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
    num = 1
    while True:
        if is_sqr(num + 100) and is_sqr(num + 168):
            print(num)
            break
        num += 1


if __name__ == '__main__':
    main()
