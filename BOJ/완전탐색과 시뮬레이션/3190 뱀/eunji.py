import sys
from collections import deque
#보드의 크기 N
N = int(sys.stdin.readline())

#사과의 개수 K
K = int(sys.stdin.readline())

#보드 초기화
board = [[0]*(N+1) for _ in range(N+1)] 

for _ in range(K):
    y, x = map(int, sys.stdin.readline().split())
    #사과의 위치 저장
    board[y][x] = 1
# print(board)
#뱀의 방향 변환 횟수
L = int(sys.stdin.readline())

turn = []
for _ in range(L):
    x, c = map(str, sys.stdin.readline().split())
    x = int(x)
    turn.append((x,c))

#뱀의 위치를 저장할 데크
bam = deque([])

#상, 우, 하, 좌
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir = 1 #초기 방향은 오른쪽
time = 0
turn_index = 0 #변환한 횟수 

def turn_dir(dir, c): # 회전시키는 함수
    if c == 'L':
        return (dir + 1) % 4 
    else: 
        return (dir + 3) % 4

#뱀의 첫 위치
x, y = 1, 1
board[y][x] = 2
bam.append((y,x))

while True:
    x += dx[dir]
    y += dy[dir]
    #벽에 부딪히면 게임 종료 
    if y <= 0 or y > N or x <= 0 or x > N:
        time += 1
        break
    
    #자기 몸에 부딪히면 게임 종료
    if board[y][x] == 2:
        time += 1
        break
    
    #사과라면
    if board[y][x] == 1:
        #뱀이 위치한 좌표로 채워줌 
        board[y][x] = 2
        bam.append((y,x))
    elif board[y][x] == 0:
        #뱀이 위치한 좌표로 채워줌 
        board[y][x] = 2
        pop_y, pop_x = bam.popleft()
        bam.append((y,x))
        board[pop_y][pop_x] = 0
  
    #시간증가 
    time+=1
    # print("time", time, "bam", bam)

    #회전여부 결정
    if turn_index < L and turn[turn_index][0] == time:
        dir = turn_dir(dir, turn[turn_index][1])
        turn_index += 1
    
print(time)




    
    
