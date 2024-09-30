T = int(input())
for test_case in range(1, T+1) :

    fieldlen = int(input())
    arr = []

    for _ in range(fieldlen) :
        arr.append(list(input()))

    for i in range(fieldlen) :
        for j in range(fieldlen) :
            if arr[i][j] == 'X' :
                sty = i
                stx = j
                break

    originsty, originstx = sty, stx

    totalcommand = int(input())

    directy = [-1, 0, 1, 0] # 시계 방향 상우하좌
    directx = [0, 1, 0, -1]

    result = []

    for i in range(totalcommand) :
        idx = 0
        sty, stx = originsty, originstx
        command, cmdlst = map(str, input().split())
        cmdlst = list(cmdlst)

        for n in range(int(command)) :
            if cmdlst[n] == 'A' :
                if sty+directy[idx] < 0 or stx+directx[idx] < 0 or sty+directy[idx] >= fieldlen or stx+directx[idx] >= fieldlen: continue
                if arr[sty+directy[idx]][stx+directx[idx]] == 'T' : continue
                sty += directy[idx]
                stx += directx[idx]
            elif cmdlst[n] == 'R' :
                idx+=1
                if idx == 4 :
                    idx = 0
            elif cmdlst[n] == 'L' :
                idx-=1
                if idx < 0 :
                    idx = 3

        if arr[sty][stx] == 'Y' :
            result.append(1)
        else :
            result.append(0)

    print(f'#{test_case}', *result)