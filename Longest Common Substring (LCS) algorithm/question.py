#learn matrices in python
def longest_common_substring(str1, str2):
    # Initialize the matrix for dynamic programming
    m = len(str1)
    n = len(str2)
    matrix = [[0] * (n + 1) for _ in range(m + 1)]
    longest = 0
    end_index_str1 = 0

    # Build the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
                if matrix[i][j] > longest:
                    longest = matrix[i][j]
                    end_index_str1 = i
            else:
                matrix[i][j] = 0

    # The longest common substring
    return str1[end_index_str1 - longest:end_index_str1]

# Example texts
text1 = "I have this book I like to read"
text2 = "She has this book I like to read"

# Find the longest common substring
common_section = longest_common_substring(text1.lower(), text2.lower())
print("Longest shared common section:", common_section)
