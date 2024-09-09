def solution(n):
    answer = 0
    for i in range(n, 0, -1) :
        level, Sum = i+1, i
        while Sum < n :
            Sum = Sum+level
            level += 1
        if Sum == n :
            answer += 1
    return answer