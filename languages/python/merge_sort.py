def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left_sorted = merge_sort(left_arr)
    right_sorted = merge_sort(right_arr)

    return merge(left_sorted, right_sorted) # 결론적으로 정렬된 result 리스트 반환

def merge(left_arr, right_arr):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] > right_arr[right_index]:
            result.append(right_arr[right_index])
            right_index += 1
        else:
            result.append(left_arr[left_index])
            left_index += 1    
    '''
    남아있는 모든 값들을 result array에 병합함
    파이썬에서는 슬라이싱 인덱스가 리스트의 범위를 초과하면 에러 대신 빈 리스트를 생성함
    따라서 남아있지 않은 쪽은 빈 리스트가 더해지므로 결과에 영향을 주지 않음
    '''
    result += left_arr[left_index:]
    result += right_arr[right_index:]

    return result

arr = [-1,5,4,3,2,1]
print(merge_sort(arr))

