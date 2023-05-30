def knapsack(weights, values, capacity):
    n = len(weights)

    # Create a (n+1) x (capacity+1) matrix to store the maximum values
    max_values = [[0] * (capacity+1) for _ in range(n+1)]

    # Compute the maximum value for all subproblems
    for i in range(1, n+1):
        for w in range(1, capacity+1):
            if weights[i-1] <= w:
                max_values[i][w] = max(values[i-1] + max_values[i-1][w-weights[i-1]], max_values[i-1][w])
            else:
                max_values[i][w] = max_values[i-1][w]

    # Determine the items included in the knapsack
    included_items = []
    i = n
    w = capacity
    while i > 0 and w > 0:
        if max_values[i][w] != max_values[i-1][w]:
            included_items.append(i-1)
            w -= weights[i-1]
        i -= 1

    return max_values[n][capacity], included_items[::-1]

# Get input from the user
n = int(input("Enter the number of items: "))
weights = []
values = []

print("Enter the weights of the items:")
for _ in range(n):
    weight = int(input())
    weights.append(weight)

print("Enter the values of the items:")
for _ in range(n):
    value = int(input())
    values.append(value)

capacity = int(input("Enter the knapsack capacity: "))

# Calculate the maximum value and included items
max_value, included_items = knapsack(weights, values, capacity)

# Print the result
print("Maximum Value:", max_value)
print("Included Items:", included_items)
