# Given a deck of cards shuffle them such each of the 52! permutations is equally likely.
import random


def rand(low, high):
    return random.randint(low, high)


def shuffle(cards):
    for i in range(0, len(cards)):
        k = rand(0, i)
        temp = cards[k]
        cards[k] = cards[i]
        cards[i] = temp


if __name__ == "__main__":
    cards = map(lambda x: int(x), raw_input().split(" "))
    
    import math
    for _ in range(math.factorial(len(cards))):
        shuffle(cards)
        print cards