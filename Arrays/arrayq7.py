#7) Find the missing number
#[0,1,2,3,5]
#output: 4 
arr = [2,4,1,8,6,3,7]
n = len(arr)+1
def find_missing(arr,n):
    sum = (n*(n+1))//2
    total = 0
    for x in arr:
        total += x 
    return sum-total

print(find_missing(arr,n))