import sys

class Jar:
    # Initialize jar with capacity 12
    def __init__(self, capacity=12):
        if capacity > 0:
            self._capacity = capacity
            self._size = 0

    # Initialize string of cookie emoji for size in jar
    def __str__(self):
        return "🍪" * self._size

    # If user deposits cookies, add n to size. Dojar not allow exceed of capacity
    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError("Deposit exceeds capacity")
        else:
            self._size += n

    # If user withdraws cookies, subtract n from size. Do not allow past 0
    def withdraw(self, n):
        if n > self._size:
            raise ValueError("Withdraw exceeds current size")
        else:
            self._size -= n


    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self, size):
        if size < 0 or size > self._capacity:
            raise ValueError
        self._size = size
        return self._size

def main():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(4)
    print(jar)

if __name__ == "__main__":
    main()



