# 0/1 Knapsack using dynamic programming
n = int(input("Number of items: "))
values = list(map(int, input("Values: ").split()))
weights = list(map(int, input("Weights: ").split()))
capacity = int(input("Capacity: "))
dp = [0] * (capacity + 1)
for i in range(n):
    for c in range(capacity, weights[i] - 1, -1):
        dp[c] = max(dp[c], values[i] + dp[c - weights[i]])
print("Maximum value:", dp[capacity])
print("Time: O(nW), Space: O(W)")
