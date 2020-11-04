# coding:utf-8
import random

"""
Bagels是可以和朋友一起玩的一个推理游戏,你的朋友想到一个随机的、没有重复的3位数字，你尝试去猜测它是什么
每次猜测之后，朋友就会给出3种类型的线索:
Bagels: 你猜测的3个数都不在神秘数字中
Pico: 你猜测的是神秘数字中的一个数，但是位置不对
Fermi: 你猜测的是正确位置上的一个正确的数
"""


def get_secret_num(num_digits):
    """返回一个由num_digits个不重复随机数组成的字符串"""
    numbers = list(range(10))
    # 将序列的所有元素随机排序
    random.shuffle(numbers)
    secret_num = ''
    for i in range(num_digits):
        secret_num += str(numbers[i])
    return secret_num


def get_clues(guess, secret_num):
    """返回一个由Pico，Fermi和Bagels组成的，用来提示用户的字符串"""
    if guess == secret_num:
        return 'Yor got it!'
    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append('Fermi')
        elif guess[i] in secret_num:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    clues.sort()
    return ' '.join(clues)


def is_only_digits(num):
    """如果字符串只包含数字，返回真，否则返回假"""
    res = '0 1 2 3 4 5 6 7 8 9'
    if num == '':
        return False
    for i in num:
        if i not in res.split():
            return False
    return True


def main():
    num_digits = 3
    max_guess = 10

    while True:
        secret_num = get_secret_num(num_digits)
        print('I have thought up a number. Yor have %s guesses to get it.' % max_guess)
        guesses_taken = 1
        while guesses_taken <= max_guess:
            guess = ''
            while len(guess) != num_digits or not is_only_digits(guess):
                print('Guess #%s: ' % guesses_taken)
                guess = input()
            print(get_clues(guess, secret_num))
            if guess == secret_num:
                break
            guesses_taken += 1
            if guesses_taken > max_guess:
                print('You ran out of guesses. The answer was %s.' % secret_num)
        print('Do you want to play again? (yes or no)')
        if not input().lower().startswith('y'):
            break


if __name__ == '__main__':
    main()
