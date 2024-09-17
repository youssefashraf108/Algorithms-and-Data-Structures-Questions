# Given an array of integers, return the array with even integers removed.
# Example input: arr = [3, 2, 4, 7, 10, 6, 5]
arr = [3, 2, 4, 7, 10, 6, 5]  # Input array
arr2 = []  # List to store odd numbers

# Iterate over each element in the input array
for x in arr:
    if x % 2 != 0:  # Check if the element is odd
        arr2.append(x)  # If odd, append it to arr2

print(arr2)  # Output the array with even numbers removed
