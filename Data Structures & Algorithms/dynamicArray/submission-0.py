class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity must be greater than 0")

        self._capacity = capacity
        self._size = 0
        self._arr = [0] * capacity

    def get(self, i: int) -> int:
        return self._arr[i]

    def set(self, i: int, n: int) -> None:
        self._arr[i] = n

    def pushback(self, n: int) -> None:
        if self._size == self._capacity:
            self.resize()
        self._arr[self._size] = n
        self._size += 1

    def popback(self) -> int:
        val = self._arr[self._size - 1]
        self._size -= 1
        return val

    def resize(self) -> None:
        new_capacity = self._capacity * 2
        new_arr = [0] * new_capacity
        for i in range(self._size):
            new_arr[i] = self._arr[i]
        self._arr = new_arr
        self._capacity = new_capacity

    def getSize(self) -> int:
        return self._size
    
    def getCapacity(self) -> int:
        return self._capacity