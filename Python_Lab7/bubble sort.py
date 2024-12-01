class BubbleSort:
    def __init__(self, array):
        self.array = array

    def sort(self):
        n = len(self.array)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
        return self.array

# Example
arr = BubbleSort([64, 34, 25, 12, 22, 11, 90])
print(arr.sort())
