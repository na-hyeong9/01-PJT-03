import sys

sys.stdin = open("_문자열의거울상.txt")

T = int(input())
for i in range(1, T+1):
    word = list(input()[::-1])

    rev = []
    for j in range(len(word)):
        if word[j] == 'p':
            rev.append('q') 
        elif word[j] == 'q':
            rev.append('p')
        elif word[j] == 'b':
            rev.append('d')
        elif word[j] == 'd':
            rev.append('b')


    rev_word = ''.join(rev)
    print(f'#{i} {rev_word}')