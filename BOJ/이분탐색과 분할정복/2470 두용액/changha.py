n = int(input())
li = list(map(int, input().split()))

li.sort()

start = 0
end = len(li)-1

prev = float('inf') 
res = (0, 0)

while start < end:
    cur = (li[start] + li[end])
    mid = (start + end) // 2

    if abs(cur) < abs(prev):
        prev = cur
        # 이때 결과 저장
        res = (li[start], li[end])

    if cur < 0:
        start += 1
    elif cur > 0:
        end -= 1
    else:
        break

print(res[0], res[1])