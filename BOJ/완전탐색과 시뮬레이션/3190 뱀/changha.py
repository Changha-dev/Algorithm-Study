from collections import deque

n = int(input())
k = int(input())
apple_list = []
for _ in range(k):
    apple_list.append(list(map(int, input().split())))
l = int(input())
direction_list = deque([])
for _ in range(l):
    direction_list.append(list(map(str, input().split())))

# 지도 초기화 
graph = [[0] * n for _ in range(n)]
for x, y in apple_list:
    graph[x-1][y-1] = 1

# 게임 세팅 
timer = 0
snake_body = deque([[0, 0]])

# 방향 기준
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction_idx = 0

# 게임 시작 
while True:
    timer += 1

    #벽에 부딪혔을 때 
    current_x = snake_body[0][0]
    current_y = snake_body[0][1]
    next_x = current_x + dx[direction_idx]
    next_y = current_y + dy[direction_idx]
    if next_x < 0 or next_x > n-1 or next_y < 0 or next_y > n-1:
        break

    # 몸통에 부딪혔을 때 
    if [next_x, next_y] in snake_body:
        break
    
    # 방향 전환 
    if direction_list and str(timer) in direction_list[0]:
        dir_time, dir = direction_list.popleft()
        if dir == 'L':
            direction_idx -= 1
            direction_idx %= 4
        elif dir == 'D':
            direction_idx += 1 
            direction_idx %= 4
    
    # 사과 유무
    if graph[next_x][next_y] == 1:
        graph[next_x][next_y] = 0
        snake_body.appendleft([next_x, next_y])
    else:
        snake_body.appendleft([next_x, next_y])
        snake_body.pop()


print(timer)