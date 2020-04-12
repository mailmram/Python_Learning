class DynamicArray(object):
    def __init__(self):
        self.len = 0
        self.capacity = 1
        self.A = [None] * 1
    
    def add(self, item):
        if self.len == self.capacity:
            self.resizeArray()
        self.A[self.len] = item
        print(self.A)
        self.len = self.len + 1
    
    def remove(self):
        if self.len == 0:
            print("Cannot remove item")
        self.len = self.len -1

    def resizeArray(self):
        self.capacity = self.capacity * 2
        newArray = [None] * self.capacity
        for i in range(self.len):
            newArray[i] = self.A[i]
        self.A = newArray

    def size(self):
        return self.len

    def getItem(self, index):
        if index < 0 or index >= self.len:
            print("Out of bounds")
        return self.A[index]


arr = DynamicArray()
arr.add(12)
arr.add(21)
arr.add(13)
print(arr.getItem(2))
print(arr.size())