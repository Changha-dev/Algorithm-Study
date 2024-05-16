# 모든 경우를 탐색해봐야 함 
# 1개, 2개, 3개, .... N개
# 이부분에서 어떻게 해야 할 지 몰랐음
# combination을 이용하면 됨.


import itertools

n = int(input())
ingredients_tuple = []
# 리스트 초기화 
for _ in range(n):
    ingredients_tuple.append(tuple(map(int, input().split())))

small_res = 1000000000
for i in range(1, n+1):
            
    for subset in itertools.combinations(ingredients_tuple, i):
        sour = 1
        bitter = 0

        for a, b in subset:
            sour *= a
            bitter += b
        
        small_res = min(abs(sour-bitter), small_res)

print(small_res)






