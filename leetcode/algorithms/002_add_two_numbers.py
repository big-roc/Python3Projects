# coding:utf8


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def add_two_numbers(self, l1, l2):
        """
        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        """
        dummy = p = ListNode(None)
        s = 0
        while l1 or l2 or s:
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            p.next = ListNode(s % 10)
            p = p.next
            s //= 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next

    def add_two_numbers1(self, l1, l2):
        """
        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        val1, val2 = [l1.val], [l2.val]
        while l1.next:
            val1.append(l1.next.val)
            l1 = l1.next
        while l2.next:
            val2.append(l2.next.val)
            l2 = l2.next

        num1 = ''.join([str(i) for i in val1[::-1]])
        num2 = ''.join([str(i) for i in val2[::-1]])

        tmp = str(int(num1) + int(num2))[::-1]
        res = ListNode(tmp[0])
        run_res = res
        for i in range(1, len(tmp)):
            run_res.next = ListNode(tmp[i])
            run_res = run_res.next
        return res


def main():
    # l1: 8 <- 4 <- 2
    # l2: 4 <- 6 <- 5
    # 842+465 = 1307
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(8)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    s = Solution()
    ss = s.add_two_numbers1(l1, l2)
    while ss is not None:
        print(ss.val)
        ss = ss.next


if __name__ == '__main__':
    main()
