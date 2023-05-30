#To find the Longest common subsequence 
def longest_common_subsequence(str1, str2):
    m = len(str1)
    n = len(str2)

    lcs_lengths = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                lcs_lengths[i][j] = lcs_lengths[i-1][j-1] + 1
            else:
                lcs_lengths[i][j] = max(lcs_lengths[i-1][j], lcs_lengths[i][j-1])

    lcs = ""
    i = m
    j = n
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            lcs = str1[i-1] + lcs
            i -= 1
            j -= 1
        elif lcs_lengths[i-1][j] > lcs_lengths[i][j-1]:
            i -= 1
        else:
            j -= 1

    return lcs

# Test the algorithm
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

lcs = longest_common_subsequence(str1, str2)
print("Longest Common Subsequence:", lcs)
