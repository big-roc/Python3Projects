# coding:utf8
import sys


def main():
    for line in sys.stdin:
        line = line.strip()
        fname, lname = line.split(' ')
        l_name = lname.lower()
        print('\t'.join([fname, str(l_name)]))


if __name__ == '__main__':
    main()
