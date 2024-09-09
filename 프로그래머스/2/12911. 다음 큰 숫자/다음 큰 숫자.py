def solution(n):
    answer = n
    print(bin(n)[2::])
    origincnt = bin(n)[2::].count('1')
    flag = 1

    while flag :
        answer += 1
        if bin(answer).count('1') == origincnt :
            flag = 0

    return answer