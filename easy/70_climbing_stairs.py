# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    # 1 step = 1
    # 2 steps = 2
    # 3 steps = 3
    # 4 steps = 5
    # 5 steps = 8
    # 6 steps = 13

    if n == 1:
        return 1
    elif n == 2:
        return 2

    return climbStairs(n-1) + climbStairs(n-2)

# Works, but becomes slow
# Add memoization

def climbStairs(self, n, memo={}):
    if n in memo:
        return memo[n]

    if n == 1:
        return 1
    elif n == 2:
        return 2

    memo[n] = climbStairs(n-1, memo) + climbStairs(n-2, memo)

    return memo[n]


# Memoization allows you to store any previous result, and uses it if it comes up again





