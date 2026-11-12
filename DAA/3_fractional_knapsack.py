# Fractional Knapsack: greedy by value/weight ratio
n = int(input("Number of items: "))
items = [tuple(map(float, input("value weight: ").split())) for _ in range(n)]
capacity = float(input("Capacity: "))
items.sort(key=lambda x: x[0] / x[1], reverse=True)
total = 0
for value, weight in items:
    take = min(weight, capacity)
    total += take * value / weight
    capacity -= take
    if capacity <= 0:
        break
print("Maximum value:", total)
