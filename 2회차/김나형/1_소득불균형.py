import sys

sys.stdin = open("_소득불균형.txt")

T = int(input())
for i in range(1,T+1):
    p = int(input())
    pay = list(map(int, input().split()))
    avg_pay = sum(pay)/p
    
    cnt = 0
    for j in pay:
        if avg_pay >= j:
            cnt += 1

    print(f'#{i} {cnt}')
