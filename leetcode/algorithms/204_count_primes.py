# coding:utf8


class Solution:
    def count_primes(self, n):
        """
        :param n: int
        :return: int
        """
        is_prime = [1 for i in range(n)]

        i = 2
        while i * i < n:
            if is_prime[i]:
                j = i * i
                while j < n:
                    is_prime[j] = 0
                    j += i
            i += 1
        return sum(is_prime[2:])


def main():
    n = 10
    print(Solution.count_primes(n))


if __name__ == '__main__':
    main()
