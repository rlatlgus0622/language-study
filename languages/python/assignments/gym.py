from typing import (
    Set,
    List,
    Dict,
    Optional,
    Generator,
)


def hello_world() -> str:
    """
        "Hello, world!"를 반환하는 함수.

        Returns:
            result (str): 지정된 문자열
    """
    result = ""
    # TODO: 여기를 구현
    # ====================
    result = "Hello, world!"
    # ====================
    return result


def list_sum(values: List[int]) -> int:
    """
        리스트의 모든 요소를 더하여 반환하는 함수.
        크기가 0인 리스트인 경우 0을 반환.

        Args:
            values (list): 1 이상, 100 이하의 정수 최대 100개로 이뤄진 리스트

        Returns:
            result (int): 리스트의 모든 요소를 더한 값
    """
    result = 0
    # TODO: 여기를 구현
    # ====================
    for n in values:
        result += n

    # sum() 사용하면 더 간단
    # ====================
    return result


def jaccard_similarity(set1: Set[int], set2: Set[int]) -> float:
    """
        두 집합의 Jaccard 유사도를 계산하는 함수.
        Jaccard 유사도는 두 집합의 교집합의 크기를 두 집합의 합집합의 크기로 나눈 값.
        합집합의 크기가 0인 경우 0.0을 반환.

        Args:
            set1 (set): 1 이상, 100 이하의 정수로 이뤄진 집합
            set2 (set): 1 이상, 100 이하의 정수로 이뤄진 집합

        Returns:
            result (float): 두 집합의 Jaccard 유사도
    """
    result = 0.0
    # TODO: 여기를 구현
    # ====================
    if len(set1 | set2) > 0: # 공집합일때 제외
        result = len(set1 & set2) / len(set1 | set2)
    # ====================
    return result


def key_max(dictionary: Dict[str, int]) -> Optional[str]:
    """
        사전에서 값이 가장 큰 키를 반환하는 함수.
        크기가 0인 사전의 경우 None을 반환.

        Args:
            dictionary (dict): 서로 다른 문자열 키와 1 이상, 100 이하의 서로 다른 정수 값으로 이뤄진 사전

        Returns:
            result (str): 사전에서 값이 가장 큰 키
    """
    result = None
    # TODO: 여기를 구현
    # ====================
    max_key = None
    max_value = 0 # args가 1이상, 100이하이기 때문에 0으로 설정함
    for key, value in dictionary.items():
        if value > max_value:
            max_key = key
            max_value = value
    result = max_key
    # max() 사용하면 더 간단
    # ====================
    return result


def generate_factors(value: int) -> Generator[int, None, None]:
    """
        주어진 정수의 약수를 오름차순으로 산출(yield)하는 함수.

        Args:
            value (int): 1 이상, 100 이하의 정수

        Yields:
            factor (int): 주어진 정수의 약수
    """
    # TODO: 여기를 구현
    # ====================
    for n in range(1, value+1):
        if value % n == 0:
            yield n
    # ====================


def fizzbuzz(value: int) -> List[str]:
    """
        주어진 정수 이하에 대해, FizzBuzz 결과를 반환하는 함수.
        3의 배수는 "Fizz", 5의 배수는 "Buzz", 3과 5의 배수는 "FizzBuzz", 그 외는 정수를 문자열로 변환.

        Args:
            value (int): 15 이상, 100 이하의 정수

        Returns:
            results (list): 주어진 정수의 FizzBuzz 결과
    """
    results: List[str] = []
    # TODO: 여기를 구현
    # ====================
    if not (value >= 15 and value <= 100):
        raise ValueError("value는 15 이상, 100 이하의 정수여야 함")
    
    for n in range(1, value+1):
        if n % 3 == 0 and n % 5 == 0:
            results.append("FizzBuzz")
        elif n % 3 == 0:
            results.append("Fizz")
        elif n % 5 == 0:
            results.append("Buzz")
        else:
            results.append(str(n))
    # ====================
    return results


def is_prime(value: int) -> Optional[bool]:
    """
        주어진 정수가 소수인지 판별하는 함수.

        Args:
            value (int): 1 이상, 10000000 이하의 정수

        Returns:
            result (bool): 주어진 정수가 소수인지 여부
    """
    result = None
    # TODO: 여기를 구현
    # ====================
    if value < 2: 
        result = False
    elif value == 2: 
        result = True
    elif value % 2 == 0: 
        result = False
    else:
        result = True
        for n in range(3, int(value**0.5)+1, 2):
            if value % n == 0: 
                result = False
                break
    # ====================
    return result


def generate_primes(value: int) -> Generator[int, None, None]:
    """
        주어진 정수 이하의 소수를 오름차순으로 산출(yield)하는 함수.

        Args:
            value (int): 1 이상, 10000000 이하의 정수

        Yields:
            prime (int): 주어진 정수 이하의 소수
    """
    # TODO: 여기를 구현
    # ====================
    for i in range(2, value + 1):
        if is_prime(i):
            yield i
    # ====================


if __name__ == '__main__':
    """
        이 공간을 활용하여 여러분만의 테스트 코드를 작성해보세요.
        `python practice.py` 명령어를 통해 테스트 할 수 있습니다.
        아래는 예시입니다.
    """
    assert list_sum([100]) == 100
        
    assert jaccard_similarity({1, 2}, {3, 4}) == 0.0
    assert jaccard_similarity(set(), set()) == 0.0
        
    assert key_max({}) == None
 
    assert list(generate_factors(6)) == [1, 2, 3, 6]
    assert list(generate_factors(1)) == [1]
        
    fb_result = fizzbuzz(15)
    assert fb_result[2] == "Fizz"
    assert fb_result[4] == "Buzz"     
    assert fb_result[14] == "FizzBuzz"
         
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(4) == False
    assert is_prime(9999992) == False
        
    assert list(generate_primes(10)) == [2, 3, 5, 7]
    assert list(generate_primes(1)) == []    
