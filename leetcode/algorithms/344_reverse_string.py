# coding:utf8


class Solution:
    def reverse_string(self, s):
        """
        :param s: List[str]
        :return: None
        """
        n = len(s)
        for i in range(n // 2):
            s[i], s[n - 1 - i] = s[n - 1 - i], s[i]


def main():
    s = ["h", "e", "l", "l", "o"]
    Solution().reverse_string(s)
    print(s)


if __name__ == '__main__':
    main()
