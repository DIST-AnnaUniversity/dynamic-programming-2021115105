import sys

def matrix_chain_multiplication(dimensions):
    n = len(dimensions) - 1
    min_multiplications = [[0] * n for _ in range(n)]


    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            min_multiplications[i][j] = sys.maxsize
            for k in range(i, j):
                cost = min_multiplications[i][k] + min_multiplications[k + 1][j] + \
                       dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
                if cost < min_multiplications[i][j]:
                    min_multiplications[i][j] = cost

    return min_multiplications[0][n - 1]

n = int(input("Enter the number of matrices: "))
dimensions = []

print("Enter the dimensions of the matrices:")
for _ in range(n):
    dim = int(input())
    dimensions.append(dim)


min_multiplications = matrix_chain_multiplication(dimensions)


print("Minimum number of multiplications:", min_multiplications)
