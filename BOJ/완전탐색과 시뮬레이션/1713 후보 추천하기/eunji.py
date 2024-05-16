import sys

#사진틀의 개수
N = int(sys.stdin.readline())

space = []

#총 추천 횟수
M = int(sys.stdin.readline())

rec_list = list(map(int, sys.stdin.readline().split()))

stu_cnt = max(rec_list)

#추천횟수를 담을 학생 배열 생성 
stu = [0]*(stu_cnt+1)

for i in rec_list:
    #학생 사진이 사진틀에 있다면
    if i in space:
        #추천횟수 증가 
        stu[i] += 1
    else:
        #사진틀의 크기가 모두 차버렸다면
        if len(space) >= N:
            min_num = 100
            for j in space:
                if stu[j] < min_num:
                    min_stu = j
                    min_num = stu[j]

            space.remove(min_stu)
            stu[min_stu] = 0

            space.append(i)
            stu[i] += 1

        else: 
            space.append(i)
            stu[i] += 1
                
space.sort()
print(*space)