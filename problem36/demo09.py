# coding:utf8


def main():
    # 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
    n = int(input('Enter a number: '))
    print(n, '=')
    while n != 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n //= i
                if n == 1:
                    print('%d' % i)
                else:
                    print('%d *' % i)
                break


if __name__ == '__main__':
    main()
