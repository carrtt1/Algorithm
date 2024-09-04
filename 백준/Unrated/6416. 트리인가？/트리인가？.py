case = 1
arr = []
turnoff = 0

def findboss(num) :
    if not search[num] :
        return num
    ret = findboss(search[num])
    search[num] = ret
    return ret

def union(a, b) :
    global flag
    fa = findboss(a)
    fb = findboss(b)

    if fa == fb :
        return 1
    search[fb] = fa

while 1 :
    lst = list(map(int, input().strip().split()))

    if len(lst) == 0:
        case += 1
        continue

    for i in range(len(lst)-1) :
        if lst[i] < 0 and lst[i+1] < 0 :
            turnoff = 1
            break
    if turnoff == 1 : break

    for i in range(len(lst)) :
        if lst[i] == 0 and lst[i+1] == 0 :
            arr.append(0)
            break
        arr.append(lst[i])

    if 0 in arr :
        answer = 0
        search = [0] * (max(arr)+1)
        parents = []
        values = []
        cntarr = []
        for i in range(len(arr)) :
            if i%2 == 0 and arr[i] not in parents and arr[i] != 0 :
                parents.append(arr[i])
            if i%2 == 1 :
                if arr[i] not in values :
                    values.append(arr[i])
                ret = union(arr[i-1], arr[i])
                if ret :
                    answer = 1
                    break
                    
        for i in range(len(parents)) :
            cnt = 0
            if parents[i] in values :
                cnt += 1
            cntarr.append(cnt)

        if cntarr.count(0) > 1 :
            answer = 1
            
        if answer :
            print(f'Case {case} is not a tree.')
        else :
            print(f'Case {case} is a tree.')
            
        arr = []