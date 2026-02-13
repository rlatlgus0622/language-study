import copy

# 원본 데이터: 리스트 안에 리스트가 있는 구조 (이중 리스트)
original = [1, [2, 3], 4]

print(f"원본 주소: {id(original)}")
print(f"내부 리스트 주소: {id(original[1])}\n")

# 단순 할당 (=)
assigned = original

# 얕은 복사 ([:], copy.copy, list() 생성자)
shallow = original[:] 
# 또는 shallow = copy.copy(original)

# 깊은 복사 (copy.deepcopy)
deep = copy.deepcopy(original)

# --- 데이터 조작 시작 ---
original[0] = 999       # 겉에 있는 값 변경 (불변 객체인 정수 교체)
original[1][0] = 777    # 안에 있는 리스트(가변 객체)의 값 변경

# --- 결과 확인 ---
print("--- 조작 후 결과 ---")
print(f"Original: {original} (원본)")
print(f"Assigned: {assigned} (단순 할당: 원본과 100% 동일)")
print(f"Shallow : {shallow}  (얕은 복사: 겉은 독립, 속(리스트)은 공유됨)")
print(f"Deep    : {deep}     (깊은 복사: 완벽하게 독립)")