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
    # 한 줄 씩 입력 받기
    lst = list(map(int, input().strip().split()))

    # arr 입력이 없을 경우 다음 케이스로 넘어가는 거니까 case 번호 1 늘리기
    # 코드 검사 다 건너 뛰게 continue 넣기
    if len(lst) == 0:
        case += 1
        continue

    # 리스트에 음수가 두 번 연속 들어오면 while문 강제 종료
    for i in range(len(lst)-1) :
        if lst[i] < 0 and lst[i+1] < 0 :
            turnoff = 1
            break
    if turnoff == 1 : break

    # 한줄 입력 받아서 arr에 계속 값 더해주기
    for i in range(len(lst)) :
        # 만약 더하는데 두 번 연속 0일 경우 0 하나 추가하고 추가 그만하기
        if lst[i] == 0 and lst[i+1] == 0 :
            arr.append(0)
            break
        arr.append(lst[i])

    # 0이 입력 되면 한 케이스 입력이 다 끝난 거니까 검사 시작
    if 0 in arr :
        answer = 0
        search = [0] * (max(arr)+1)
        parents = []
        values = []
        cntarr = []
        # print(arr)
        for i in range(len(arr)) :
            if i%2 == 0 and arr[i] not in parents and arr[i] != 0 :
                parents.append(arr[i])
            if i%2 == 1 :
                if arr[i] not in values :
                    values.append(arr[i])
                # print(arr[i-1], arr[i])
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

        # 검사가 끝나면 다음 케이스 검사하게 arr 초기화
        arr = []