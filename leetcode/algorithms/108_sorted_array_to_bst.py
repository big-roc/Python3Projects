# coding:utf8

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sorted_array_to_bst(self, nums):
        """
        :param nums: List[int]
        :return: TreeNode
        """
        if nums:
            m = len(nums) // 2
            r = TreeNode(nums[m])
            r.left, r.right = map(self.sorted_array_to_bst, [nums[:m], nums[m + 1:]])
            return r


def main():
    pass


if __name__ == '__main__':
    main()
