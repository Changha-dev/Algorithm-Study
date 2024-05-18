import copy

# 방향 정의 (동, 서, 남, 북)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 각 CCTV 종류에 따른 방향 정의
directions = [
    [],
    [[0], [1], [2], [3]],                  # 1번 CCTV
    [[0, 1], [2, 3]],                      # 2번 CCTV
    [[0, 3], [3, 1], [1, 2], [2, 0]],      # 3번 CCTV
    [[0, 1, 3], [0, 1, 2], [1, 2, 3], [0, 2, 3]],  # 4번 CCTV
    [[0, 1, 2, 3]]                         # 5번 CCTV
]

def watch(x, y, direction, office):
    for d in direction:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]
            if nx < 0 or nx >= len(office) or ny < 0 or ny >= len(office[0]) or office[nx][ny] == 6:
                break
            if office[nx][ny] == 0:
                office[nx][ny] = '#'

def dfs(depth, office):
    global min_blind_spot
    if depth == len(cctvs):
        # 사각 지대 계산
        blind_spot = sum(row.count(0) for row in office)
        min_blind_spot = min(min_blind_spot, blind_spot)
        return
    
    x, y, cctv_type = cctvs[depth]
    for direction in directions[cctv_type]:
        new_office = copy.deepcopy(office)
        watch(x, y, direction, new_office)
        dfs(depth + 1, new_office)

n, m = map(int, input().split())
office = []
cctvs = []

for i in range(n):
    row = list(map(int, input().split()))
    office.append(row)
    for j in range(m):
        if 1 <= row[j] <= 5:
            cctvs.append((i, j, row[j]))

min_blind_spot = float('inf')
dfs(0, office)
print(min_blind_spot)