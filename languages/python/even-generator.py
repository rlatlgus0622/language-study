# 예외 처리 및 yield 활용
# 짝수 생성기

def safe_even_generator(n):
    if not isinstance(n, int):
        raise TypeError("정수가 아닙니다.")
    if n<0:
        raise ValueError("양수를 입력하세요.")
    for i in range(0,n+1,2):
        yield i
try:
    n = int(input("값을 입력하세요: "))
    for i in safe_even_generator(n):
        print(i,end=" ")

except TypeError as e:
    print("정수가 아닙니다.")

except ValueError as e:
    print("양수를 입력하세요.")

