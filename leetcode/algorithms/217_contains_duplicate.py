# coding:utf8


class Solution:
    def contains_duplicate(self, nums):
        """
        :param nums: List[int]
        :return: bool
        """
        return len(nums) != len(set(nums))


def main():
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    res = Solution().contains_duplicate(nums)
    print(res)


if __name__ == '__main__':
    main()
