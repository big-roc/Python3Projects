# coding:utf8


def main():
    # 题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
    a = 1
    b = 1
    for i in range(1, 21, 2):
        print('%d' % (a + b))
        a += b
        b += a


if __name__ == '__main__':
    main()
