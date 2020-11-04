# coding:utf8


def main():
    # 题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半，再落下，
    # 求它在第10次落地时，共经过多少米？第10次反弹多高？
    s = 100.0
    h = 50.0
    for i in range(2, 11):
        s += 2 * h
        h /= 2
    print('the sum length of path: %f' % s)
    print('the last height is: %f' % h)


if __name__ == '__main__':
    main()
