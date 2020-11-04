# coding:utf8


class Solution:
    def two_sum(self, nums, target):
        """
        :param nums: List[int]
        :param target: int
        :return: List[int]
        """
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i
        return []


def main():
    nums = [2, 7, 11, 15]
    target = 9
    so = Solution()
    n = so.two_sum(nums, target)
    print("结果：", n)


if __name__ == '__main__':
    main()
