n = int(input())
quad_tree = []
for _ in range(n):
    quad_tree.append(list(map(int, input().rstrip())))


def divide(x, y, size):
    if size == 1:
        print(quad_tree[x][y], end="")
        return
    
    standard_num = quad_tree[x][y]
    
    for i in range(x, x + size):
        for j in range(y, y + size):
            if standard_num != quad_tree[i][j]:
                size //= 2
                print("(", end="")
                divide(x, y, size)
                divide(x, y+size, size)
                divide(x+size, y, size)
                divide(x+size, y+size, size)
                print(")", end="")
                return
    
    print(standard_num, end="")
    return 

divide(0, 0, n)


