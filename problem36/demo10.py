# coding:utf8


def main():
    # 题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
    s = int(input('Enter a number: '))
    if s >= 90:
        grade = 'A'
    elif s >= 60:
        grade = 'B'
    else:
        grade = 'C'
    print(grade)


if __name__ == '__main__':
    main()
