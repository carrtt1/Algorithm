from copy import deepcopy

def solution(want, number, discount):
    answer = 0

    for i in range(len(discount)-9) :
        wcnt = deepcopy(number)
        search = discount[i:i+10]
        for j in range(10) :
            if search[j] not in want : break
            else :
                idx = want.index(search[j])
                if wcnt[idx] == 0 : break
                wcnt[idx] -= 1
        if sum(wcnt) == 0 :
            answer += 1

    return answer