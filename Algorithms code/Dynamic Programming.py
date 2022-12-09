#what is Dynamic Programming for?
#used to solve optimization problems

# 1.break down the complex problem into complex subproblem
# 2.find optimal solution to these subproblems
# 3.store the result of subproblems-memoization
# 4.reuse them so that same subproblem is not calculated more than once
# 5.finally calculates the result of complex problem

#applicable to problems having properties of
#overlapping subproblems & optimal substructure


#approach 1: dynamic programming


memo = {}

def L(nums, i):
    if i in memo:
        return memo[i]


    if i == len(nums) - 1: 
        return 1

    max_len = 1
    for j in range(i + 1, len(nums)):
        if nums[j] > nums[i]:
            max_len = max(max_len, L(nums, j)+ 1)
        
        
    memo[i] = max_len
    return max_len

def len_of_list(nums):
    return max(L(nums, i) for i in range (len(nums)))

nums = [1, 5, 2, 4, 3]

print(len_of_list(nums))





