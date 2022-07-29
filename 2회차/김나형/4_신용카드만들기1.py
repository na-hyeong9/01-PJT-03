import sys

sys.stdin = open("_신용카드만들기1.txt")

T = int(input())
for i in range(1, T + 1):
    card_n = list(map(int, input().split()))
    
    sum_n = 0
    for j in range(1, len(card_n) + 1):
        if j % 2 == 0:
            sum_n += card_n[j-1]
        else:
            sum_n += card_n[j-1] * 2
    if sum_n % 10 == 0:
        print(f'#{i} 0')
    else:
        print(f'#{i} {10 - (sum_n % 10)}') 

