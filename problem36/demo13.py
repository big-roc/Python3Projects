# coding:utf8
from math import sqrt


def main():
    # 题目：一个数如果恰好等于它的因子之和，这个数就称为“完全数”。
    # 例如6=1＋2＋3，编程找出1000以内的所有完全数
    n = int(input('input a number: '))
    sum = n * -1
    k = int(sqrt(n))
    for i in range(1, k + 1):
        if n % i == 0:
            sum += n // i
            sum += i
    if sum == n:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
