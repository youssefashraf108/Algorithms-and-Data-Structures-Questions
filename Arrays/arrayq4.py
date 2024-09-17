#find second maximum value in an array
#arr = [12,34,2,34,33,1]
#output: 33
class ArrayManipulator:
    def __init__(self, array):
        self.array = array
    
    def findSecondMax(self):
        secondMax = float('-inf')
        max_val = float('-inf')
        for x in self.array:
            if x > max_val:
                secondMax = max_val
                max_val = x
            elif x > secondMax and x != max_val:
                secondMax = x
        return max_val, secondMax
    
    def __str__(self):
        max_val, secondMax = self.findSecondMax()
        return f"Largest integer: {max_val}\nSecond Largest Integer: {secondMax}"
        
    
# Example usage:
def main():
    arr = [12, 34, 2, 34, 33, 1]
    array_manipulator = ArrayManipulator(arr)
    print(array_manipulator)

if __name__ == '__main__':
    main()





