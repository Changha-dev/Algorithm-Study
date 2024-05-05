import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
budget = int(sys.stdin.readline())

li.sort()

# 상한액을 지정했을 떄 
# low 일 경우, high일 경우로 생각해라!?

low, high = 0, max(li)
res = 0

while low <= high:
    mid = (low + high) // 2
    tmp_sum = 0
    for cur in li:
        tmp_sum += min(cur, mid)
    # tmp_sum = sum(min(cur, mid) for cur in li)

    if tmp_sum <= budget:
        low = mid + 1
        res = mid
    elif tmp_sum > budget:
        high = mid - 1
print(res)