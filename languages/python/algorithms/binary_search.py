# 이진 탐색 함수 (반복문 기반, 기초적)
def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
    return -1

def binary_search_recursive(arr, target, left, right):
    pass


# main
arr = [12,45,62,100,123,145,184,193]
target = 100
target_index = binary_search_iterative(arr, target)
print(f"target: {target}, index {target_index}에 위치")
