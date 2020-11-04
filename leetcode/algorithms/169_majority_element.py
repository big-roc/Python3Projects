# coding:utf8


class Solution:
    def majority_element(self, nums):
        """
        :param nums: List[int]
        :return: int
        """
        nums.sort()
        return nums[len(nums) // 2]


def main():
    nums = [2, 2, 1, 1, 1, 2, 2]
    res = Solution().majority_element(nums)
    print(res)


if __name__ == '__main__':
    main()
