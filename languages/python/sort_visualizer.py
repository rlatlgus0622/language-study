from copy import copy # 리스트 생성시 얕은 복사 사용
import time

class SortVisualizer:
    def __init__(self, data):
        self.original_data = copy(data)
        self.data = copy(data)
        self.data_len = len(self.original_data)
        self.swap_count = 0 
        print(f"정렬 할 숫자 {len(data)}개 로드 완료.")

    
    def reset(self):
        self.data = copy(self.original_data)
        self.swap_count = 0
    
    def swap(self, i, j): # 깊은복사 위해 인덱스로
        self.data[i], self.data[j] = self.data[j], self.data[i]
        self.swap_count += 1 # 교환, 이동 횟수(비용) 카운트

    def check_time(self, sort_func):
        pass
    

    def bubble_sort(self):
        for i in range(self.data_len - 1):
            for j in range(self.data_len - i - 1):
                if self.data[j] > self.data[j+1]:
                    self.swap(j, j+1)


    def selection_sort(self):
        for i in range(self.data_len-1):
            least_index = i
            for j in range(i+1, self.data_len):
                if self.data[least_index] > self.data[j]: 
                    least_index = j
            self.swap(i, least_index)


    def insertion_sort(self):
        for i in range(1, self.data_len):
            key = self.data[i]
            j = i - 1
            while j >= 0 and self.data[j] > key:
                self.data[j+1] = self.data[j]
                self.swap_count += 1
                j -= 1
            self.data[j+1] = key


    def quick_sort(self):
        pass


    def merge_sort(self):
        pass

sv1 = SortVisualizer([-1, 5, 4, 3, 2, 1, 6])
sv1.selection_sort()
print(f"{sv1.original_data}->{sv1.data}, swap count: {sv1.swap_count}")