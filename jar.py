import sys

class Jar:
    # Initialize jar with capacity 12
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    # Initialize string of cookie emoji for size in jar
    def __str__(self):
        return "🍪" * self.size

    # If user deposits cookies, add n to size. Do not allow exceed of capacity
    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Deposit exceeds capacity")
        self.size = self.size + n

    # If user withdraws cookies, subtract n from size. Do not allow past 0
    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Withdraw exceeds current size")
        self.size = self.size - n


    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError("Capacity cannot be less than 1")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self._capacity:
            raise ValueError("Current size cannot exceed capacity")
        self._size = size


def main():
    jar = Jar()
    print(jar)
    jar.deposit(5)
    print(jar)
    jar.withdraw(4)
    print(jar)

if __name__ == "__main__":
    main()



