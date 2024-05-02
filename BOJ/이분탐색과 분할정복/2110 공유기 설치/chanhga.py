# 어떻게 하는거야
# 공유기 
# 가장 인접한 두 공유기 사이의 거리를 가능한 한 크게

# 

n, c = map(int, input().split())
li = []
for _ in range(n):
    li.append(int(input()))

li.sort()

start, end = 1, li[-1] - li[0]
res = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 1
    current = li[0]

    for i in range(1, len(li)):
        if li[i] - current >= mid:
            cnt += 1
            current = li[i]
    
    if cnt >= c:
        start = mid + 1
        res = mid
    else:
        end = mid - 1
print(res)