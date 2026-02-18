# heap: 데이터에서 최댓값 최솟값 쉽게 찾아낼 수 있음
import heapq

heap = [] # 여기서 heap[0]은 무조건 최솟값

heapq.heappush(heap, 4)
heapq.heappush(heap, 10)
heapq.heappush(heap, 8)

print(f"현재 heap: {heap}") 

min = heapq.heappop(heap)
print(f"꺼낸 최솟값: {min}, 남은 힙: {heap}")

# Max heap 구현 예정
