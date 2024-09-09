def solution(n):
    answer = n
    origincnt = bin(n).count('1')
    flag = 1

    while flag :
        answer += 1
        if bin(answer).count('1') == origincnt :
            flag = 0

    return answer