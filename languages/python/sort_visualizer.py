from copy import copy # 리스트 생성시 얕은 복사 사용

class SortVisualizer:
    def __init__(self, data):
        self.original_data = copy(data)
        self.data = copy(data)
        print(f"정렬 할 숫자 {len(data)}개 로드 완료.")

    def reset_data(self):
        self.data = copy(self.original_data)

    def check_time(self, sort_func):
        pass
    
    def bubble_sort(self):
        pass

    def selection_sort(self):
        pass

    def insertion_sort(self):
        pass

    def quick_sort(self):
        pass

    def merge_sort(self):
        pass
