# coding:utf8


class Solution:
    def reverse_words(self, s):
        """
        :param s: str
        :return: str
        """
        return ' '.join(word[::-1] for word in s.split(' '))

    def reverse_words1(self, s):
        """
        :param s: str
        :return: str
        """
        return ' '.join(s.split(' ')[::-1])[::-1]


def main():
    s = "Let's take LeetCode contest"
    res = Solution().reverse_words1(s)
    print(s)
    print(res)


if __name__ == '__main__':
    main()
