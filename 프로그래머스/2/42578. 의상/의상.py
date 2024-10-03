def solution(clothes):
    answer = 1
    itemname = []
    itemcnt = []

    for i in range(len(clothes)) :
        if clothes[i][1] not in itemname :
            itemname.append(clothes[i][1])
            itemcnt.append(1)
        elif clothes[i][1] in itemname :
            itemcnt[itemname.index(clothes[i][1])] += 1

    
    for i in range(len(itemcnt)) :
        answer *= itemcnt[i]+1

    answer -= 1
    return answer