n = int(input())  # 사진틀의 개수
m = int(input())  # 총 추천 횟수
num_list = list(map(int, input().split()))  # 추천받은 학생의 번호 목록

res_list = []  # 현재 사진틀에 게시된 학생 목록
like_list = {}  # 학생별 추천 횟수

for student in num_list:
    if student in res_list:
        like_list[student] += 1  # 이미 게시된 학생의 추천 횟수 증가
    else:
        if len(res_list) < n:
            res_list.append(student)
            like_list[student] = 1
        else:
            # 추천 횟수가 가장 적은 학생 찾기
            min_likes = min(like_list[s] for s in res_list)
            candidates = [s for s in res_list if like_list[s] == min_likes]
            
            # 그 중 가장 오래된 학생 찾기
            to_remove = candidates[0] # 기준값 임의로 설정한것임 
            for s in candidates:
                if res_list.index(s) < res_list.index(to_remove): 
                    to_remove = s
            
            res_list.remove(to_remove)
            del like_list[to_remove]
            
            res_list.append(student)
            like_list[student] = 1

# 최종 후보 학생 번호를 증가하는 순서로 출력
final_candidates = sorted(res_list)
print(" ".join(map(str, final_candidates)))