# coding:utf8
import sys
import numpy as np


def toInt(num):
    return int(num)


def main():
    for line in sys.stdin:
        x = line.split(",")
        v = np.array(map(toInt, x))
        print(v.min)


if __name__ == '__main__':
    main()
