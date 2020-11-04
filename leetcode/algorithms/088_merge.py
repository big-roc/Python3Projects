# coding:utf8


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :param nums1: List[int]
        :param m: int
        :param nums2: List[int]
        :param n: int
        :return: None
        """
        i, j = 0, 0
        while j < n:
            if i >= m + j:
                nums1[i:i + n - j] = nums2[j:n]
                break
            if nums1[i] < nums2[j]:
                i += 1
            else:
                nums1[i], nums1[i + 1:] = nums2[j], nums1[i:len(nums1) - 1]
                j += 1
                i += 1


def main():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    Solution().merge(nums1, 3, nums2, 3)
    print(nums1)


if __name__ == '__main__':
    main()
