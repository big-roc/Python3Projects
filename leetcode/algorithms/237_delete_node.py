# coding:utf8


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def delete_node(self, node):
        node.val = node.next.val
        node.next = node.next.next


def main():
    l1 = Node(4)
    l1.next = Node(5)
    l1.next.next = Node(1)
    l1.next.next.next = Node(9)
    Solution().delete_node(l1)


if __name__ == '__main__':
    main()
