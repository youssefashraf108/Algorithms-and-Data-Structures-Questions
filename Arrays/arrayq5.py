def move_zeros(arr, n):
    j = 0
    for i in range(n):
        if arr[i] !=0 and arr[j] == 0:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        if arr[j] != 0:
            j += 1
# Example usage:
arr = [0, 1, 0, 4, 12]
n = len(arr)
move_zeros(arr, n)
print(arr)
