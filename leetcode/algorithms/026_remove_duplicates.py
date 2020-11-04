# coding:utf8


class Solution:
    def remove_duplicates(self, nums):
        """
        :param nums: List[int]
        :return: int
        """
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
                j += 1
        return i + 1


def main():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    res = Solution().remove_duplicates(nums)
    print(res)


if __name__ == '__main__':
    main()
