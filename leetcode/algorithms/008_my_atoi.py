# coding:utf8


class Solution:
    def my_atoi(self, s):
        """
        :param str: str
        :return: int
        """
        s = s.strip()
        str_num = 0
        if len(s) == 0:
            return str_num

        positive = True
        if s[0] == '+' or s[0] == '-':
            if s[0] == '-':
                positive = False
            s = s[1:]

        for char in s:
            if '0' <= char <= '9':
                str_num = str_num * 10 + ord(char) - ord('0')
            if char < '0' or char > '9':
                break

        if str_num > 2147483647:
            if not positive:
                return -2147483648
            else:
                return 2147483648
        if not positive:
            str_num = 0 - str_num
        return str_num


def main():
    s = '   -42'
    res = Solution().my_atoi(s)
    print(res)


if __name__ == '__main__':
    main()
