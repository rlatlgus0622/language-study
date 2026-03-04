class GcdAlgorithm:
    # 브루트포트(완전탐색): a, b 둘다 나눠지는 수를 계속 찾아서 result에 저장, 마지막에 저장된 수가 가장 큼 -> 최대공약수
    def gcd_bruteforce(self, a, b):
        result = 1
        for i in range(2, min(a,b) + 1):
            if a % i == 0 and b % i == 0:
                result = i
        return result

    # 유클리드 알고리즘(뺄셈): a, b가 같아질 때까지 큰 수에서 작은 수를 뺌, 두 수가 같아지면 최대공약수
    def gcd_subtraction(self, a, b):
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        return a

    # 유클리드 알고리즘(반복문): a를 b로 나눈 나머지를 구하고, (a, b) → (b, a%b) 로 계속 교체, b가 0이 되는 순간의 a가 최대공약수
    def gcd_iterative(self, a, b):
        while b > 0:
            a, b = b, a % b
        return a

    # 유클리드 알고리즘(재귀): gcd(a, b) = gcd(b, a % b) 점화식을 재귀, b가 0일때 a가 최대공약수
    def gcd_recursive(self, a, b):
        if b == 0:
            return a
        return self.gcd_recursive(b, a % b)


# main
a, b = map(int, input("a, b를 입력하세요: ").split())
gcd = GcdAlgorithm()

print(gcd.gcd_bruteforce(a,b))
print(gcd.gcd_subtraction(a,b))
print(gcd.gcd_iterative(a,b))
print(gcd.gcd_recursive(a,b))