""""
Avoid plagarisim
- detect the two most likely books that might have plagrisim 
    longest shared commen section of the text 

"I have this book i like to read"
"She has this book i like to read" 
"""
def longest_common_substring(text1, text2):
    # Split the texts into words
    words1 = text1.split()
    words2 = text2.split()

    # Create a matrix to store the lengths of longest common suffixes
    lcs_matrix = [[0] * (len(words2) + 1) for _ in range(len(words1) + 1)]
    longest_length = 0
    lcs_end_index = 0

    # Iterate through both texts and populate the matrix
    for i in range(1, len(words1) + 1):
        for j in range(1, len(words2) + 1):
            if words1[i - 1] == words2[j - 1]:  # Compare words
                lcs_matrix[i][j] = lcs_matrix[i - 1][j - 1] + 1
                if lcs_matrix[i][j] > longest_length:
                    longest_length = lcs_matrix[i][j]
                    lcs_end_index = i

    # Extract the longest common substring
    longest_common_section = words1[lcs_end_index - longest_length: lcs_end_index]
    
    return " ".join(longest_common_section)

# Example texts
text1 = "I have this book I like to read"
text2 = "She has this book I like to read"

# Find and print the longest common substring
common_section = longest_common_substring(text1, text2)
print(f"Longest common section: '{common_section}'")
