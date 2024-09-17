class ArrayManipulator:
    def __init__(self, array):
        self.array = array

    def smallest(self):
        smallest = self.array[0]
        for x in self.array:
            if smallest > x:
                smallest = x
        return smallest
    
    def __str__(self):
        return f"Smallest integer: {self.smallest()}"
    
def main():
    arr = [5, 9, 3, 15, 1, 2]
    array_manipulator = ArrayManipulator(arr)
    print(array_manipulator)

if __name__ == '__main__':
    main()
