# coding:utf8


def main():
    # 题目：打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。
    # 例如：153是一个“水仙花数”，因为153=1^3＋5^3＋3^3
    for i in range(100, 1000):
        a = int(i / 100)
        b = (int(i / 10)) % 10
        c = i % 10
        if i == a ** 3 + b ** 3 + c ** 3:
            print(a, b, c)
            print('%d' % i)


if __name__ == '__main__':
    main()
