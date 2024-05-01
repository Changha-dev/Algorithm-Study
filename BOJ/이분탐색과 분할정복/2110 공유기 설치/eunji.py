import sys

n, c = map(int, sys.stdin.readline().split())

arr = []

# 집의 좌표 값을 입력 받아 array에 추가 
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
# 집의 좌표 값 정렬
arr.sort()

start = 1 #공유기 사이의 거리 최소
end = arr[-1] - arr[0] #공유기 사이의 거리 최대 

while (start <= end):
    #현재 공유기 사이의 거리
    mid = (start+end)//2
    current = arr[0]
    count = 1

    #공유기 설치 몇 대 할 수 있는지 체크
    for i in range(1, len(arr)):
        #만약, i번째 집 좌표가 정해놓은 가장 인접한 공유기 사이의 거리보다 크거나 같다면, 설치 가능 
        if arr[i] >= current + mid:
            current = arr[i]
            count += 1
    
    #공유기 설치 수가 목표 설치 수보다 크면, 해당 거리보다 더 넓게 설치할 수 있다는 뜻이므로, 
    #공유기 사이의 거리를 늘림
    if count >= c:
        start = mid + 1
        result = mid
    #공유기 설치 수가 목표 설치 수보다 작다면, 해당 거리보다 더 좁게 설치해야된다는 뜻이므로,
    #공유기 사이의 거리를 좁힘
    else:
        end = mid - 1
print(result)
        