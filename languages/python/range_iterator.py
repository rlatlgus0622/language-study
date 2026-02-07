class NumberRange:
    def __init__(self, limit):
        if not isinstance(limit, int):
            raise TypeError("It is not integer.")
        if limit < 0:
            raise ValueError("It is not 양수")
        self.limit = limit
    def __repr__(self):
        return f"{self.__class__.__name__}(limit={self.limit})"
    
    def __iter__(self):
        pass

class EvenGen(NumberRange):
    def __iter__(self):
        for n in range(0, self.limit + 1, 2):
            yield n

class OddGen(NumberRange):
    def __iter__(self):
        for n in range(1, self.limit + 1, 2):
            yield n

# main
try:
    limit = int(input("Enter limit: "))
    even_gen = EvenGen(limit)
    odd_gen = OddGen(limit)
    
    for i in even_gen:
        print(i, end=' ')
    print("")
    for i in odd_gen:
        print(i, end=' ')

except TypeError as e:
    print(f"TypeError: {e}")
except ValueError as e:
    print(f"ValueError: {e}")