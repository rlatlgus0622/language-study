import math

from typing import (
    Any,
    Iterator,
)

from abc import (
    ABC,
    abstractmethod,
)


EPS = 1e-6


class VectorError(Exception):

    pass


class InvalidScalarTypeError(VectorError):

    pass


class InvalidVectorTypeError(VectorError):

    pass


class NormalizingZeroVectorError(VectorError):

    pass


class Vector(ABC):

    @abstractmethod
    def __len__(self) -> int:
        pass

    @abstractmethod
    def __iter__(self) -> Iterator[float]:
        pass

    @abstractmethod
    def __eq__(self, other: 'Vector') -> bool:  # type: ignore
        pass

    @abstractmethod
    def __ne__(self, other: 'Vector') -> bool:  # type: ignore
        pass

    @abstractmethod
    def __add__(self, other: 'Vector') -> 'Vector':
        pass

    @abstractmethod
    def __sub__(self, other: 'Vector') -> 'Vector':
        pass

    @abstractmethod
    def __mul__(self, scalar: float) -> 'Vector':
        pass

    @abstractmethod
    def __rmul__(self, scalar: float) -> 'Vector':
        pass

    @abstractmethod
    def __matmul__(self, other: 'Vector') -> float:
        pass

    @abstractmethod
    def norm(self) -> float:
        pass

    @abstractmethod
    def normalize(self) -> 'Vector':
        pass

    @abstractmethod
    def distance(self, other: 'Vector') -> float:
        pass


class Vector2D(Vector):
    """
        Attributes:
            x (float): x 좌표
            y (float): y 좌표
    """

    def __init__(self, x: float, y: float) -> None:
        """
            2차원 벡터를 초기화하는 생성자.

            Args:
                x (float): x 좌표
                y (float): y 좌표

            Example:
                v = Vector2D(1, 2)
                assert v.x == 1
                assert v.y == 2
        """
        # TODO: 여기를 구현
        # ====================

        # ====================

    def __len__(self) -> int:
        """
            벡터의 차원을 반환하는 함수.

            Returns:
                result (int): 벡터의 차원

            Example:
                v = Vector2D(1, 2)
                assert len(v) == 2
        """
        result: float
        # TODO: 여기를 구현
        # ====================

        # ====================
        return result

    def __eq__(self, other: 'Vector2D') -> bool:  # type: ignore
        """
            두 벡터가 같은지 판별하는 함수.

            Args:
                other (Vector2D): 다른 벡터

            Returns:
                result (bool): 두 벡터가 같은지 여부

            Example:
                v = Vector2D(1, 2)
                u = Vector2D(1, 2)
                assert v == u
        """
        result: bool
        # TODO: 여기를 구현
        # ====================

        # ====================
        return result

    def __ne__(self, other: 'Vector2D') -> bool:  # type: ignore
        """
            두 벡터가 같지 않은지 판별하는 함수.

            Args:
                other (Vector2D): 다른 벡터

            Returns:
                result (bool): 두 벡터가 같지 않은지 여부

            Example:
                v = Vector2D(1, 2)
                u = Vector2D(3, 4)
                assert v != u
        """
        result: bool
        # TODO: 여기를 구현
        # ====================

        # ====================
        return result

    def __iter__(self) -> Iterator[float]:
        """
            벡터의 원소를 산출하는 이터레이터.

            Example:
                v = Vector2D(1, 2)
                es = [e for e in v]
                assert es == [1, 2]
        """
        # TODO: 여기를 구현
        # ====================

        # ====================

    def __add__(self, other: 'Vector2D') -> 'Vector2D':  # type: ignore
        """
            벡터의 덧셈을 계산하는 함수.
            두 벡터 (x, y), (a, b)의 덧셈은 (x + a, y + b)로 계산됩니다.

            Args:
                other (Vector2D): 다른 벡터

            Raises:
                InvalidVectorTypeError: `other`가 `Vector2D` 타입이 아닌 경우

            Returns:
                vector (Vector2D): 두 벡터의 덧셈

            Example:
                v = Vector2D(1, 2)
                u = Vector2D(3, 4)
                w = v + u
                assert w == Vector2D(4, 6)
        """
        vector: 'Vector2D'
        # TODO: 여기를 구현
        # ====================

        # ====================
        return vector

    def __sub__(self, other: 'Vector2D') -> 'Vector2D':  # type: ignore
        """
            벡터의 뺄셈을 계산하는 함수.
            두 벡터 (x, y), (a, b)의 뺄셈은 (x - a, y - b)로 계산됩니다.

            Args:
                other (Vector2D): 다른 벡터

            Raises:
                InvalidVectorTypeError: `other`가 `Vector2D` 타입이 아닌 경우

            Returns:
                vector (Vector2D): 두 벡터의 뺄셈

            Example:
                v = Vector2D(1, 2)
                u = Vector2D(2, 1)
                w = v - u
                assert w == Vector2D(-1, 1)
        """
        vector: 'Vector2D'
        # TODO: 여기를 구현
        # ====================

        # ====================
        return vector

    def __mul__(self, scalar: float) -> 'Vector2D':
        """
            벡터 v, 스칼라 s에 대해 스칼라 곱 vs를 계산하는 함수.

            Args:
                scalar (float): 스칼라

            Raises:
                InvalidScalarTypeError: `scalar`가 `int` 혹은 `float` 타입이 아닌 경우

            Returns:
                vector (Vector2D): 스칼라가 곱해진 벡터

            Example:
                v = Vector2D(1, 1)
                u = v * 2
                assert u == Vector2D(2, 2)
        """
        vector: 'Vector2D'
        # TODO: 여기를 구현
        # ====================

        # ====================
        return vector

    def __rmul__(self, scalar: float) -> 'Vector2D':
        """
            벡터 v, 스칼라 s에 대해 스칼라 곱 sv를 계산하는 함수.

            Args:
                scalar (float): 스칼라

            Raises:
                InvalidScalarTypeError: `scalar`가 `int` 혹은 `float` 타입이 아닌 경우

            Returns:
                vector (Vector2D): 스칼라가 곱해진 벡터

            Example:
                v = Vector2D(1, 1)
                u = 2 * v
                assert u == Vector2D(2, 2)
        """
        vector: 'Vector2D'
        # TODO: 여기를 구현
        # ====================

        # ====================
        return vector

    def __matmul__(self, other: 'Vector2D') -> float:  # type: ignore
        """
            벡터의 내적(inner product)을 계산하는 함수.
            두 벡터 (x, y), (a, b)의 내적 <(x, y), (a, b)>는 xa + yb로 계산됩니다.

            Args:
                other (Vector2D): 다른 벡터

            Raises:
                InvalidVectorTypeError: `other`가 `Vector2D` 타입이 아닌 경우

            Returns:
                result (float): 두 벡터의 내적

            Example:
                v = Vector2D(1, 2)
                u = Vector2D(3, 4)
                s = v @ u
                assert abs(s - 11.0) < EPS
        """
        result: float
        # TODO: 여기를 구현
        # ====================

        # ====================
        return result

    def norm(self) -> float:
        """
            벡터의 크기(norm)를 계산하는 함수.
            벡터 (x, y)의 크기 ||(x, y)||는 √(x² + y²)로 계산됩니다.
            혹은, √((x, y) @ (x, y))로도 계산할 수 있습니다.

            Returns:
                result (float): 벡터의 크기

            Example:
                v = Vector2D(3, 4)
                s = v.norm()
                assert abs(s - 5.0) < EPS
        """
        result: float
        # TODO: 여기를 구현
        # ====================

        # ====================
        return result

    def normalize(self) -> 'Vector2D':
        """
            벡터를 정규화하는 함수.
            벡터의 정규화는 벡터를 그 자신의 크기로 나누어 크기를 1로 만드는 것입니다.
            `float` 값이 0인지 판별할때는 `abs(value - 0.0) < EPS`를 사용하는 것이 안전합니다.

            Returns:
                vector (Vector2D): 정규화된 벡터

            Raises:
                NormalizingZeroVectorError: 벡터의 크기가 0인 경우.

            Example:
                v = Vector2D(3, 4)
                u = v.normalize()
                s = u.norm()
                assert abs(s - 1.0) < EPS
        """
        vector: 'Vector2D'
        # TODO: 여기를 구현
        # ====================

        # ====================
        return vector

    def distance(self, other: 'Vector2D') -> float:  # type: ignore
        """
            벡터의 거리를 계산하는 함수.
            두 벡터 (x, y), (a, b)의 거리 d((x, y), (a, b))는 √((x - a)² + (y - b)²)로 계산됩니다.
            혹은, ||(x, y) - (a, b)||로도 계산할 수 있습니다.

            Args:
                other (Vector2D): 다른 벡터

            Raises:
                InvalidVectorTypeError: `other`가 `Vector2D` 타입이 아닌 경우

            Returns:
                result (float): 두 벡터의 거리

            Example:
                v = Vector2D(0, 0)
                u = Vector2D(3, 4)
                s = v.distance(u)
                assert abs(s - 5.0) < EPS
        """
        result: float
        # TODO: 여기를 구현
        # ====================

        # ====================
        return result

    def reflect(self, other: 'Vector2D') -> 'Vector2D':
        """
            벡터의 반사를 계산하는 함수.
            벡터 v와 정규화된 법선 벡터 u에 대해, 벡터 v의 반사는 v - 2<v, u>u로 계산됩니다.

            Args:
                other (Vector2D): 다른 벡터

            Raises:
                InvalidVectorTypeError: `other`가 `Vector2D` 타입이 아닌 경우
                NormalizingZeroVectorError: 벡터의 크기가 0인 경우.

            Returns:
                vector (Vector2D): 반사된 벡터

            Example:
                v = Vector2D(1, 2)
                u = Vector2D(0, 3)
                w = v.reflect(u)
                assert w == Vector2D(1, -1)
        """
        vector: 'Vector2D'
        # TODO: 여기를 구현
        # ====================

        # ====================
        return vector

    def cross(self, other: 'Vector2D') -> float:
        """
            2차원 벡터의 외적(cross product)을 계산하는 함수.
            두 벡터 (x, y), (a, b)의 외적은 xb - ya로 계산됩니다.

            Args:
                other (Vector2D): 다른 벡터

            Raises:
                InvalidVectorTypeError: `other`가 `Vector2D` 타입이 아닌 경우

            Returns:
                result (float): 두 벡터의 외적

            Example:
                v = Vector2D(2, 1)
                u = Vector2D(1, 2)
                s = v.cross(u)
                assert abs(s - 3.0) < EPS
        """
        result: float
        # TODO: 여기를 구현
        # ====================

        # ====================
        return result


class Vector3D(Vector):
    """
        Attributes:
            x (float): x 좌표
            y (float): y 좌표
            z (float): z 좌표
    """

    def __init__(self, x: float, y: float, z: float) -> None:
        """
            3차원 벡터를 초기화하는 생성자.

            Args:
                x (float): x 좌표
                y (float): y 좌표
                z (float): z 좌표
        """
        # TODO: 여기를 구현
        # ====================

        # ====================

    def __len__(self) -> int:
        """
            벡터의 차원을 반환하는 함수.

            Returns:
                result (int): 벡터의 차원
        """
        result: float
        # TODO: 여기를 구현
        # ====================

        # ====================
        return result

    def __eq__(self, other: 'Vector3D') -> bool:  # type: ignore
        """
            두 벡터가 같은지 판별하는 함수.

            Args:
                other (Vector3D): 다른 벡터

            Returns:
                result (bool): 두 벡터가 같은지 여부
        """
        result: bool
        # TODO: 여기를 구현
        # ====================

        # ====================
        return result

    def __ne__(self, other: 'Vector3D') -> bool:  # type: ignore
        """
            두 벡터가 같지 않은지 판별하는 함수.

            Args:
                other (Vector3D): 다른 벡터

            Returns:
                result (bool): 두 벡터가 같지 않은지 여부
        """
        result: bool
        # TODO: 여기를 구현
        # ====================

        # ====================
        return result

    def __iter__(self) -> Iterator[float]:
        """
            벡터의 원소를 산출하는 이터레이터.
        """
        # TODO: 여기를 구현
        # ====================

        # ====================

    def __add__(self, other: 'Vector3D') -> 'Vector3D':  # type: ignore
        """
            벡터의 덧셈을 계산하는 함수.

            Args:
                other (Vector3D): 다른 벡터

            Raises:
                InvalidVectorTypeError: `other`가 `Vector3D` 타입이 아닌 경우

            Returns:
                vector (Vector3D): 두 벡터의 덧셈
        """
        vector: 'Vector3D'
        # TODO: 여기를 구현
        # ====================

        # ====================
        return vector

    def __sub__(self, other: 'Vector3D') -> 'Vector3D':  # type: ignore
        """
            벡터의 뺄셈을 계산하는 함수.

            Args:
                other (Vector3D): 다른 벡터

            Raises:
                InvalidVectorTypeError: `other`가 `Vector3D` 타입이 아닌 경우

            Returns:
                vector (Vector3D): 두 벡터의 뺄셈
        """
        vector: 'Vector3D'
        # TODO: 여기를 구현
        # ====================

        # ====================
        return vector

    def __mul__(self, scalar: float) -> 'Vector3D':
        """
            벡터 v, 스칼라 s에 대해 스칼라 곱 vs를 계산하는 함수.

            Args:
                scalar (float): 스칼라

            Raises:
                InvalidScalarTypeError: `scalar`가 `int` 혹은 `float` 타입이 아닌 경우

            Returns:
                vector (Vector3D): 스칼라가 곱해진 벡터
        """
        vector: 'Vector3D'
        # TODO: 여기를 구현
        # ====================

        # ====================
        return vector

    def __rmul__(self, scalar: float) -> 'Vector3D':
        """
            벡터 v, 스칼라 s에 대해 스칼라 곱 sv를 계산하는 함수.

            Args:
                scalar (float): 스칼라

            Raises:
                InvalidScalarTypeError: `scalar`가 `int` 혹은 `float` 타입이 아닌 경우

            Returns:
                vector (Vector3D): 스칼라가 곱해진 벡터
        """
        vector: 'Vector3D'
        # TODO: 여기를 구현
        # ====================

        # ====================
        return vector

    def __matmul__(self, other: 'Vector3D') -> float:  # type: ignore
        """
            벡터의 내적(inner product)을 계산하는 함수.

            Args:
                other (Vector3D): 다른 벡터

            Raises:
                InvalidVectorTypeError: `other`가 `Vector3D` 타입이 아닌 경우

            Returns:
                result (float): 두 벡터의 내적
        """
        result: float
        # TODO: 여기를 구현
        # ====================

        # ====================
        return result

    def norm(self) -> float:
        """
            벡터의 크기(norm)를 계산하는 함수.

            Returns:
                result (float): 벡터의 크기
        """
        result: float
        # TODO: 여기를 구현
        # ====================

        # ====================
        return result

    def normalize(self) -> 'Vector3D':
        """
            벡터를 정규화하는 함수.

            Returns:
                vector (Vector3D): 정규화된 벡터
        """
        vector: 'Vector3D'
        # TODO: 여기를 구현
        # ====================

        # ====================
        return vector

    def distance(self, other: 'Vector3D') -> float:  # type: ignore
        """
            벡터의 거리를 계산하는 함수.

            Args:
                other (Vector3D): 다른 벡터

            Raises:
                InvalidVectorTypeError: `other`가 `Vector3D` 타입이 아닌 경우

            Returns:
                result (float): 두 벡터의 거리
        """
        result: float
        # TODO: 여기를 구현
        # ====================

        # ====================
        return result

    def reflect(self, other: 'Vector3D') -> 'Vector3D':
        """
            벡터의 반사를 계산하는 함수.

            Args:
                other (Vector3D): 다른 벡터

            Raises:
                InvalidVectorTypeError: `other`가 `Vector3D` 타입이 아닌 경우
                NormalizingZeroVectorError: 벡터의 크기가 0인 경우.

            Returns:
                vector (Vector3D): 반사된 벡터
        """
        vector: 'Vector3D'
        # TODO: 여기를 구현
        # ====================

        # ====================
        return vector

    def cross(self, other: 'Vector3D') -> 'Vector3D':
        """
            3차원 벡터의 외적(cross product)을 계산하는 함수.
            두 벡터 (x, y, z), (a, b, c)의 외적은 (yc - zb, za - xc, xb - ya)로 계산됩니다.

            Args:
                other (Vector3D): 다른 벡터

            Raises:
                InvalidVectorTypeError: `other`가 `Vector3D` 타입이 아닌 경우

            Returns:
                vector (Vector3D): 두 벡터의 외적

            Example:
                v = Vector3D(1, 2, 3)
                u = Vector3D(4, 5, 6)
                w = v.cross(u)
                assert w == Vector3D(-3, 6, -3)
        """
        vector: 'Vector3D'
        # TODO: 여기를 구현
        # ====================

        # ====================
        return vector


if __name__ == '__main__':
    """
        이 공간을 활용하여 여러분만의 테스트 코드를 작성해보세요.
        `python vector.py` 명령어를 통해 테스트 할 수 있습니다.
        아래는 예시입니다.
    """
    assert len(Vector2D(0, 0)) == 2