import time
import random

class SortVisualizer:
    def __init__(self, data):
        self.original_data = data[:]
        self.data = data[:]
        self.result_time = {} # 딕셔너리 활용, 정렬 함수마다 결과값 저장해서 비교
        self.data_len = len(self.original_data)
        self.swap_count = 0
        self.compare_count = 0
        print(f"정렬 할 숫자 {len(data)}개 로드 완료.")

    
    def reset(self):
        self.data = self.original_data[:]
        self.swap_count = 0
        self.compare_count = 0
    
    # 교환 시행 및 횟수 카운트 함수
    def swap(self, i, j): # 깊은복사 위해 인덱스로
        self.data[i], self.data[j] = self.data[j], self.data[i]
        self.swap_count += 1 # 교환, 이동 횟수(비용) 카운트
    
    # 비교 시행 및 횟수 카운트 함수
    def compare(self, a, b):
        self.compare_count += 1
        return a > b

    def check_time(self, sort_func):
        self.reset()
        func_name = sort_func.__name__
        print(f"{func_name} 실행")
        start_time = time.perf_counter()
        sort_func()
        end_time = time.perf_counter()
        result_time = end_time - start_time
        
        print(f"{self.original_data} -> {self.data}\n// 교환횟수: {self.swap_count}, 비교횟수: {self.compare_count}, 실행시간: {result_time:.9f}초\n")

    

    def bubble_sort(self):
        for i in range(self.data_len - 1):
            swaped = False

            for j in range(self.data_len - i - 1):
                if self.compare(self.data[j], self.data[j+1]):
                    self.swap(j, j+1)
                    swaped = True
            # 교환이 일어나지 않았다면 정렬완료 -> 종료
            if not swaped:
                break

    def selection_sort(self):
        for i in range(self.data_len-1):
            least_index = i
            for j in range(i+1, self.data_len):
                if self.compare(self.data[least_index], self.data[j]): 
                    least_index = j
            # 원래의 i가 최솟값이면 교환 안함
            if least_index != i:
                self.swap(i, least_index)


    def insertion_sort(self):
        for i in range(1, self.data_len):
            key = self.data[i]
            j = i - 1
            while j >= 0 and self.compare(self.data[j], key):
                self.data[j+1] = self.data[j]
                self.swap_count += 1
                j -= 1
            self.data[j+1] = key

    # 병합 정렬
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left_group = arr[:mid]
        right_group = arr[mid:]

        left_sorted = self.merge_sort(left_group)
        right_sorted = self.merge_sort(right_group)

        return self.merge(left_sorted, right_sorted) 
    
    def merge(self, left_arr, right_arr):
        result = []
        left_index = 0
        right_index = 0
        
        while left_index < len(left_arr) and right_index < len(right_arr):
            if self.compare(left_arr[left_index], right_arr[right_index]):
                result.append(right_arr[right_index])
                right_index += 1
            else:
                result.append(left_arr[left_index])
                left_index += 1
        
        result += left_arr[left_index:]
        result += right_arr[right_index:]
        return result

    # merge_sort가 재귀 함수이기 때문에 정렬이 모두 완료된 값을 data에 저장하기 위해서 따로 함수 구현   
    def run_merge_sort(self):
        self.data = self.merge_sort(self.data)


    # 퀵 정렬
    def quick_sort(self, start, end):
        # 원소가 1개 이하일 경우 종료
        if start >= end:
            return

        # partition 함수를 통해 피벗의 최종 위치 받아옴
        pivot_index = self.partition(start, end)

        # 피벗을 기준으로 왼쪽과 오른쪽 부분 리스트 재귀 호출
        self.quick_sort(start, pivot_index - 1)
        self.quick_sort(pivot_index + 1, end)
    
    def partition(self, start, end):
        # 피벗 설정 (중간값)
        mid = (start + end) // 2
        pivot_value = self.data[mid]

        # 피벗 end로 보내서 정렬 과정에서 방해되지 않게 함
        self.swap(mid, end)
        
        # 피벗보다 작은 값들을 앞쪽으로 모으는 과정 (Lomuto Partition Scheme 변형)
        store_index = start
        
        for i in range(start, end): # end는 피벗이 있으므로 제외
            if self.compare(pivot_value, self.data[i]):
                self.swap(store_index, i)
                store_index += 1
        
        # 맨 뒤에 숨겨뒀던 피벗을 자신의 제자리(store_index)로 이동
        self.swap(store_index, end)
        
        # 피벗 최종 위치 반환
        return store_index

    # 실행용 래퍼 함수 (외부에서 호출할 때 인자 없이 호출하기 위해)
    def run_quick_sort(self):
        self.quick_sort(0, self.data_len - 1)


arr = [random.randint(-9, 9) for i in range(100)]
sv1 = SortVisualizer(arr)
sv1.check_time(sv1.bubble_sort) # 괄호 붙이면 함수가 실행되기에, 괄호를 붙이지 않은 함수 객체 자체를 인수로 해야함
sv1.check_time(sv1.selection_sort)
sv1.check_time(sv1.insertion_sort)
sv1.check_time(sv1.run_merge_sort)
sv1.check_time(sv1.run_quick_sort)