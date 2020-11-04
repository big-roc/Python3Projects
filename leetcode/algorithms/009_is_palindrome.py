# coding:utf8


class Solution:
    def is_palindrome(self, x):
        """
        :param x: int
        :return: bool
        """
        if x < 0:
            return False

        str_x = str(x)
        return str_x == str_x[::-1]


def main():
    x = 123321
    res = Solution().is_palindrome(x)
    print(res)


if __name__ == '__main__':
    main()
