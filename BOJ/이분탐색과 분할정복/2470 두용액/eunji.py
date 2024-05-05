import sys

#전체 용액의 수
n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split(' ')))

arr.sort()




#모두 음수일 경우 
if arr[0] < 0 and arr[n-1] < 0:
    print(arr[-2], arr[-1])
#모두 양수일 경우 
elif arr[0] > 0 and arr[n-1] > 0:
    print(arr[0], arr[1])
else: 
    start = 0
    end = n-1
    result = abs(arr[start]+ arr[end])
    final = [arr[start], arr[end]]

    while start <= end:
        r = abs(arr[start]+ arr[end])
        if(r < result):
            result = r
            final = [arr[start], arr[end]]
            if result == 0:
                break
        #합이 음수면, 왼쪽 인덱스 증가 
        if arr[start]+ arr[end] < 0:
            start += 1
        else: 
            end -= 1

print(final[0], final[1])

    
    
        