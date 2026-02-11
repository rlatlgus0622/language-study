def quick_sort(arr, left, right):
    if left < right:
        p = partition(arr, left, right)
        # 재귀 함수
        quick_sort(arr, left, p-1)
        quick_sort(arr, p+1, right)
    return arr

# pivot을 기준으로 작은 수는 왼쪽, 큰수는 오른쪽으로 나누는 함수
def partition(arr, left, right):
    pivot = arr[right] # 가장 오른쪽에 있는 수를 pivot으로 설정
    i = left - 1 
    
    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j] # pivot보다 작은 수 왼쪽으로

    # pivot을 작은 그룹 바로 다음으로 위치
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i+1


# main
original_arr = [6, 5, 3, 1, 8, 7, 2, 4]
sorted_arr = quick_sort(original_arr[:], 0, len(original_arr)-1)
print(f"정렬 전: {original_arr}")
print(f"정렬 후: {sorted_arr}")