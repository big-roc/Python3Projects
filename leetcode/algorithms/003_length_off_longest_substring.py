# coding:utf8


class Solution:
    def length_of_longest_substring(self, s):
        """
        :param s: str
        :return: int
        """
        start, res, cache = 0, 0, {}
        for idx, c in enumerate(s):
            if c in cache and cache[c] >= start:
                start = cache[c] + 1
                cache[c] = idx
            else:
                cache[c] = idx
                cur = idx - start + 1
                res = max(res, cur)
        return res


def main():
    word = 'abcabcbb'
    res = Solution().length_of_longest_substring(word)
    print(res)


if __name__ == '__main__':
    main()
