#!/usr/bin/python3
""" Prime Game """


def is_prime(n):
    """
    Checks is n is prime

    :param n int: the number to check on it
    """
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def isWinner(x, nums):
    """
    Decided who is the winner in the Prime Game

    :param x  int: number of rounds
    :param nums list of int: the list that we will remove from
                            it the prime numbers' multiples
    """

    if not isinstance(x, int) or x <= 0:
        return None

    if not nums or type(nums) is not list or min(nums) < 0:
        return None

    players = {'Maria': 0, 'Ben': 0}

    def play_round(prime_set):
        """ """
        last_played = 'Maria'
        next_play = 'Ben'
        curr_prime = 0
        round_nums = nums.copy()

        for _ in range(len(nums)):
            if len(round_nums) == 1 or curr_prime == len(prime_set):
                players[last_played] += 1
                return
            round_nums = list(map(lambda curr: curr %
                              prime_set[curr_prime] != 0, round_nums))
            curr_prime += 1
            last_played, next_play = next_play, last_played

    for round in nums:
        prime_set = [i for i in range(1, round + 1) if is_prime(i)]
        play_round(prime_set)

    if players['Maria'] == players['Ben']:
        return None
    return max(players, key=lambda k: players[k])
