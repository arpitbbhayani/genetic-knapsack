memo = {}

def knapsack(W, w, v, n):
    if n == 0 or W == 0:
        return 0
  
    # if weight of the nth item is more than the weight
    # available in the knapsack the skip it
    if (w[n - 1] > W):
        return knapsack(W, w, v, n - 1)
    
    # Check if we already have an answer to the sunproblem
    if (W, n) in memo:
        return memo[(W, n)]
  
    # find value of the knapsack when the nth item is picked
    value_picked = v[n - 1] + knapsack(W - w[n - 1], w, v, n - 1)

    # find value of the knapsack when the nth item is not picked
    value_notpicked = knapsack(W, w, v, n - 1)

    # return the maxmimum of both the cases
    # when nth item is picked and not picked
    value_max = max(value_picked, value_notpicked)

    # store the optimal answer of the subproblem
    memo[(W, n)] = value_max

    return value_max


if __name__ == '__main__':
    wt = [7, 2, 1, 9]
    val = [5, 4, 7, 2]
    W = 15
    n = len(val)
    print(knapsack(W, wt, val, n))
