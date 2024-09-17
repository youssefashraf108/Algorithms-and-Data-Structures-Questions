#how to resize an array in python 
def resize(arr,capacity):
    temp = [0] * capacity
    for i in range(len(arr)):
        temp[i] = arr[i]
    arr = temp
    return arr 
arr = [5,9,3,10]
print(resize(arr,len(arr)*2))