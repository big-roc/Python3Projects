# coding:utf8


class Solution:
    def longest_common_prefix(self, strs):
        """
        :param strs: List[strs]
        :return: str
        """
        if len(strs) == 0:
            return ''

        if len(strs) == 1:
            return strs[0]

        a = min(strs)
        b = max(strs)

        for i in range(len(a)):
            if a[i] != b[i]:
                return a[:i]
        return a


def main():
    strs = ["flower", "flow", "flight"]
    res = Solution().longest_common_prefix(strs)
    print(min(strs))
    print(max(strs))
    print(res)


if __name__ == '__main__':
    main()
