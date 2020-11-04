# coding:utf8


class Solution:
    def multiply(self, num1, num2):
        """
        :param num1: str
        :param num2: str
        :return: str
        """
        lookup = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        if num1 == '0' or num2 == '0':
            return '0'
        num1, num2 = num1[::-1], num2[::-1]

        tmp_res = [0 for i in range(len(num1) + len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                tmp_res[i + j] += lookup[num1[i]] * lookup[num2[j]]

        res = [0 for i in range(len(num1) + len(num2))]
        for i in range(len(num1) + len(num2)):
            res[i] = tmp_res[i] % 10
            if i < len(num1) + len(num2) - 1:
                tmp_res[i + 1] += tmp_res[i] // 10
        return ''.join(str(i) for i in res[::-1]).lstrip('0')


def main():
    num1 = input('Enter a number: ')
    num2 = input('Enter a number: ')
    res = Solution().multiply(num1, num2)
    print(res)


if __name__ == '__main__':
    main()
