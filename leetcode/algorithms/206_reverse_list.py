# coding:utf8


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverse_list(self, head):
        """
        :param head: ListNode
        :return: ListNode
        """
        prev, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev


def main():
    pass


if __name__ == '__main__':
    main()
