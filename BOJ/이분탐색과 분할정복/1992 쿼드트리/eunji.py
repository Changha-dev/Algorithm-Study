import sys
sys.setrecursionlimit(10**6)
#제곱 수 입력 받기 
n = int(sys.stdin.readline())

video = []

for _ in range(n):
    v = [ int(x) for x in list(sys.stdin.readline().rstrip())]
    video.append(v)


def quadtree(n, vlist):
    s = 0
    #리스트에 있는 숫자를 다 더함 
    for l in vlist:
        s += sum(l)
    
    #만약 합이 n^2라면 모든 요소가 1이라는 뜻 이므로 1 리턴
    if s == n**2:
        return '1'
    #만약 합이 0이라면 모든 요소가 0이라는 뜻 이므로 0 리턴
    if s == 0:
        return '0'
    
    half = n//2
    temp = '('
    temp += quadtree(half,[l[:half] for l in vlist[:half]]) #왼쪽 위 부분
    temp += quadtree(half,[l[half:] for l in vlist[:half]]) #왼쪽 아래 부분 
    temp += quadtree(half,[l[:half] for l in vlist[half:]]) #오른쪽 위 부분
    temp += quadtree(half,[l[half:] for l in vlist[half:]]) #오른쪽 아래 부분
    temp += ')'


    return temp

print(quadtree(n, video))


