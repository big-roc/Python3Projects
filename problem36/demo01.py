# coding:utf-8


def main():
    # 题目：有1、2、3、4，能组成多少个互不相同且无重复数字的三位数？都是多少？
    num_list = []
    count = 0
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if i != j and j != k and k != i:
                    res = i * 100 + j * 10 + k
                    num_list.append(res)
                    count += 1
    print(num_list)
    print(count)


if __name__ == '__main__':
    main()
