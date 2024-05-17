import sys

def find_min_diff(idx, cur_s, cur_b):
    global min_diff
    #모든 재료에 대한 탐색 종료
    if idx == N:
        #적어도 하나의 재료가 선택되었을 때 
        if cur_s != 1:
            min_diff = min(min_diff, abs(cur_s - cur_b))
        return
    
    #재료를 선택하는 경우
    next_s, next_b = ing[idx]
    find_min_diff(idx + 1, cur_s * next_s, cur_b + next_b)

    #재료를 선택하지 않는 경우
    find_min_diff(idx + 1, cur_s, cur_b)


#재료의 개수 N
N = int(sys.stdin.readline())

ing = []
for _ in range(N):
    s, b = map(int, sys.stdin.readline().split())
    ing.append((s,b))

min_diff = float('inf')

#탐색 시작
find_min_diff(0,1,0)

print(min_diff)


