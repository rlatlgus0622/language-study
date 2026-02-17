class SimpleStack:
    def __init__(self):
        self.data = []

    def pop(self):
        try:
            return self.data.pop()
        except IndexError:
            print("Error: Stack is empty")
            return None
        
    def push(self, item):
        #정수만 받기
        if not isinstance(item, int): #isinstance 내장함수 사용
            raise TypeError(f"Only integer. Yours: {item}")
        self.data.append(item)

    def peek(self):
        if self.data:
            return self.data[-1]
        return None
    
s1 = SimpleStack()
s1.push(1)
s1.push(2)
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.peek())

