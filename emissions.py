import numpy as np

def optimize_emissions(returns, max_tokens):
    """
    Dynamic Programming approach to optimize emissions across multiple pools.
    
    :param returns: A list of lists where returns[i][j] is the return of allocating j tokens to pool i.
    :param max_tokens: The total number of tokens available for allocation.
    :return: The maximum possible return and the allocation of tokens to each pool.
    """
    n_pools = len(returns)
    
    # DP table where dp[i][j] stores the maximum return possible using the first i pools with j tokens
    dp = np.zeros((n_pools + 1, max_tokens + 1))
    
    # Allocation table to reconstruct the solution
    allocation = np.zeros((n_pools + 1, max_tokens + 1), dtype=int)
    
    for i in range(1, n_pools + 1):
        for j in range(max_tokens + 1):
            dp[i][j] = dp[i-1][j]
            allocation[i][j] = 0
            for k in range(j + 1):
                current_return = returns[i-1][k] + dp[i-1][j-k]
                if current_return > dp[i][j]:
                    dp[i][j] = current_return
                    allocation[i][j] = k
    
    # Reconstructing the optimal allocation
    optimal_allocation = []
    remaining_tokens = max_tokens
    for i in range(n_pools, 0, -1):
        optimal_allocation.append(allocation[i][remaining_tokens])
        remaining_tokens -= allocation[i][remaining_tokens]
    
    optimal_allocation.reverse()
    
    return dp[n_pools][max_tokens], optimal_allocation

# Example usage:

# Returns for each pool (rows) for different token allocations (columns)
returns = [
    [0, 1, 4, 6, 7],  # Returns for pool 1
    [0, 2, 5, 7, 8],  # Returns for pool 2
    [0, 3, 6, 8, 9]   # Returns for pool 3
]

max_tokens = 4

max_return, optimal_allocation = optimize_emissions(returns, max_tokens)

print(f"Max Return: {max_return}")
print(f"Optimal Allocation: {optimal_allocation}")
