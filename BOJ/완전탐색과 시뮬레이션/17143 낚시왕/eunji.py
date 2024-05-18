import sys

#격자판의 크기 R,C 상어의 수 M
R, C, M = map(int, sys.stdin.readline().split())

#상, 하, 우, 좌 
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

#상어의 위치 저장 배열
board = [[0]*(C+1) for _ in range(R+1)]

sharp = []
for _ in range(M):
    #상어의 위치, 속력, 이동방향, 크기 
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    #상어의 위치에 상어의 크기를 저장 
    board[r][c] = z
    #상어 배열에 위치, 속력, 이동방향 저장
    sharp.append((r, c, s, d, z))


cnt = 0
#1번 프로세스 
#낚시왕이 이동할 수 있는 횟수는 C번
for i in range(1, C+1):
    #2번 프로세스 
    #해당 열의 행에서 처음만난 상어를 잡기(땅과 제일 가까움)
    for j in range(1, R+1):
        #값이 0보다 크면 상어가 있는 것 
        if board[j][i] > 0:
            cnt += board[j][i]
            board[j][i] = 0
            # 잡힌 상어를 sharp에서 제거
            sharp = [(r, c, s, d, z) for r, c, s, d, z in sharp if not (r == j and c == i)]
            break
    
    #3번 프로세스
    for i in range(len(sharp)):
        r, c, s, d, z = sharp[i]

        #만약 r이 0이라면, 큰 상어에게 잡아먹힌 상어임 
        if r==0:
            continue
        else: 
            board[r][c] = 0
       
        nx, ny = r, c
        # 상어 이동 처리 (속도를 최적화하기 위해 이동 거리를 조정)
        if d <= 2:  # 상하 이동
            s %= (R-1) * 2
            for _ in range(s):
                if nx == 1: d = 2
                if nx == R: d = 1
                nx += dx[d-1]
        else:  # 좌우 이동
            s %= (C-1) * 2
            for _ in range(s):
                if ny == 1: d = 3
                if ny == C: d = 4
                ny += dy[d-1]

        # print(d, r, c)
        #해당 위치의 값보다 현재 상어의 크기가 크다면 상어 이동완료 
        if z > board[nx][ny]:
            sharp[i] = (nx, ny, s, d, z)
            board[nx][ny] = z
        else: 
            sharp[i] = (0, 0, s, d, z)
        
            
print(cnt)