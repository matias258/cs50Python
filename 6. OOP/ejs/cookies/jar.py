class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Cant have less than 0 cookies in the jar")
        if capacity > 12:
            raise ValueError("Too many cookies in the jar")
        self._capacity = 12
        self._size = 0
        

    def __str__(self):
        return f"There are {self._size} cookies in the jar"

    def deposit(self, n):
        self._size += n
        if self._size > self._capacity:
            self._size -= n
            raise ValueError("Too many cookies in the jar")
            

    def withdraw(self, n):
        self._size -= n
        if self._size < 0:
            self._size += n
            raise ValueError("Cant have less cookies in the jar")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
