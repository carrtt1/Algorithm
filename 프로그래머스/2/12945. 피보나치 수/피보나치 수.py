import sys
sys.setrecursionlimit(10**7)

def solution(n):
    fibbo = [0, 1]

    for i in range(2, n+1) :
        fibbo.append(fibbo[i-1] + fibbo[i-2])

    res = fibbo[n]

    answer = res % 1234567
    return answer