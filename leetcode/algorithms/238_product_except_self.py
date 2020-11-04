# coding:utf8


class Solution:
    def product_except_self(self, nums):
        """
        :param nums: List[int]
        :return: List[int]
        """
        length = len(nums)
        left, right, ans = [0] * length, [0] * length, [0] * length

        left[0] = 1
        for i in range(1, length):
            left[i] = nums[i - 1] * left[i - 1]

        right[length - 1] = 1
        for i in reversed(range(length - 1)):
            right[i] = nums[i + 1] * right[i + 1]

        for i in range(length):
            ans[i] = left[i] * right[i]

        return ans

    def product_except_self1(self, nums):
        """
        :param nums: List[int]
        :return: List[int]
        """
        length = len(nums)
        ans = [0] * length
        ans[0] = 1


def main():
    nums = [1, 2, 3, 4]
    res = Solution().product_except_self(nums)
    print(res)

    nums = [0, 0]
    res = Solution().product_except_self(nums)
    print(res)


if __name__ == '__main__':
    main()
