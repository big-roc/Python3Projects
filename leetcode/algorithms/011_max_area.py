# coding:utf8


class Solution:
    def max_area(self, height):
        """
        :param height: List[int]
        :return: int
        """
        left, right = 0, len(height) - 1
        ans = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            ans = max(ans, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans


def main():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    res = Solution().max_area(height)
    print(res)


if __name__ == '__main__':
    main()
