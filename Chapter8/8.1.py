#8.1
#Triple Step: A child is running up a staircase with n steps
#and can hop either 1 step, 2 steps, or 3 steps at a time,
#implement a method to count how many possible ways the child can run up the stairs.
#Without Memoization
def countways(n):
    if (n<0):
        return 0
    elif n==0 :
        return 1
    else:
        return countways(n-1) +countways(n-2) + countways(n-3)
#it is roughly  O(3^n)


#With memoization
def memoization(self):
    memo = [-1]*(n+1)
    return better_count_ways(n,memo)

def better_count_ways(n,memo):
    if (n<0):
        return 0
    elif n==0:
        return 1
    elif memo[n] > -1:
        return memo[n]
    else:
        memo[n] = better_count_ways(n-1,memo) + better_count_ways(n-2,memo) + better_count_ways(n-3,memo)
        return memo[n]
