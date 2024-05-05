
import sys

n = int(sys.stdin.readline())

stars = [[' ']*2*n for _ in range(n)]

def recursion(i, j, size):
    #사이즈가 3일 경우, 첫번째 별 인덱스를 기준으로 별찍기 
    if size == 3:
        stars[i][j] = '*'
        stars[i+1][j-1] = stars[i+1][j+1] = '*'
        for k in range(-2, 3):
            stars[i+2][j+k] = '*'
    else:
        #이전상태 
        newSize = size // 2
        #삼각형 3개 분할하여 각각의 첫번째 별 인덱스를 지정해줌 
        recursion(i, j, newSize)
        recursion(i + newSize, j - newSize, newSize)
        recursion(i + newSize, j + newSize, newSize)

recursion(0, n - 1, n)

#별 출력
for star in stars:
    print("".join(star))



