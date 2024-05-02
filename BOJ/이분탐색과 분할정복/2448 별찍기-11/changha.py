n = int(input())


# 분할정복
# 3개짜리가 기준
# 3개가 아니면 3의 배수일텐데 계속 나누면서 재귀로 하면됨 
# 현재, 왼쪽 아래, 오른쪽 아래 -> 이렇게 나누면 됨




# 별을 담을 빈 배열을 만들어 놓는다. 
stars = [[' ']*2*n for _ in range(n)]


def recursion(i, j, size):
    if size == 3:
        stars[i][j] = '*'
        stars[i+1][j-1] = '*'
        stars[i+1][j+1] = '*'
        for k in range(-2, 3):
            stars[i+2][j-k] = '*'

    else:
        newSize = size//2
        recursion(i, j, newSize)
        recursion(i + newSize, j - newSize, newSize)
        recursion(i + newSize, j + newSize, newSize)

recursion(0, n-1, n)
for star in stars:
    print("".join(star))



