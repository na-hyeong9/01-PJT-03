from re import L
import sys

sys.stdin = open("_최빈수구하기.txt")


T = int(input())

for i in range(T):
    tc = int(input())
    score_li = list(map(int, input().split()))

    score_cnt = [0] * 101

    for i in score_li:
        score_cnt[i] += 1

    max_score = 0
    for j in range(len(score_cnt)):
        if score_cnt[j] >= max_score:
            max_score = score_cnt[j]
            score_idex = j
    print(f'#{tc} {score_idex}')


        
    


