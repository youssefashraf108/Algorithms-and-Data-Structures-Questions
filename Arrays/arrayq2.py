class ArrayManipulator:
    def __init__(self, array):
        self.array = array

    def reverse(self):
        start = 0
        end = len(self.array) - 1
        while start < end: 
            # Swap elements at start and end indices
            temp = self.array[start]
            self.array[start] = self.array[end]
            self.array[end] = temp
            # Move towards the middle
            start += 1
            end -= 1

    def __str__(self):
        return str(self.array)

def main():
    arr = [2, 11, 5, 10, 7, 8]
    manipulator = ArrayManipulator(arr)
    print("Original array:", manipulator)
    manipulator.reverse()
    print("Reversed array:", manipulator)

if __name__ == '__main__':
    main()

