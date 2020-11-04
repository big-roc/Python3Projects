# coding:utf8


class Solution:
    def is_valid(self, s):
        """
        :param s: str
        :return: bool
        """
        stack = ['?']
        mapping = {'{': '}', '[': ']', '(': ')', '?': '?'}
        for char in s:
            if char in mapping:
                stack.append(char)
            elif mapping[stack.pop()] != char:
                return False
        return len(stack) == 1


def main():
    s = '{[[]{}]}()()'
    res = Solution().is_valid(s)
    print(res)


if __name__ == '__main__':
    main()
