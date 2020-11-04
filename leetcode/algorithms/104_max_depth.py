# coding:utf8


class Solution:
    def max_depth(self, root):
        """
        :param root: TreeNode
        :return: int
        """
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        else:
            return 1 + max(self.max_depth(root.left), self.max_depth(root.right))


def main():
    pass


if __name__ == '__main__':
    main()
