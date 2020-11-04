# coding:utf8


def main():
    # 题目：输出9*9口诀
    for i in range(1, 10):
        for j in range(1, i + 1):
            print("%d*%d=%d" % (j, i, i * j), end=' | ')
        print(' ')


if __name__ == '__main__':
    main()
