# coding:utf8


class Solution:
    def three_sum(self, nums):
        """
        :param nums: List[int]
        :return: List[List[int]]
        """
        sort_nums = sorted(nums)
        print(sort_nums)


def main():
    nums = [-1, 0, 1, 2, -1, -4]
    res = Solution().three_sum(nums)


if __name__ == '__main__':
    main()
