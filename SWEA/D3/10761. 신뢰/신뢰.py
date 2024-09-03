T = int(input())
for test_case in range(1, T + 1):

    lst = list(map(str, input().split()))

    buttonnum = 0
    turn = []
    inputturn = []

    for i in range(len(lst)) :
        if i == 0 :
            buttonnum = int(lst[i])
        if i % 2 == 1 :
            inputturn.append(lst[i])
        if i % 2 == 0 and i != 0 :
            inputturn.append(int(lst[i]))
            turn.append(inputturn)
            inputturn = []

    turn.reverse()
    second = 0
    Bnow = 1
    Onow = 1
    target = turn.pop()

    while len(turn) >= 0 :
        second += 1

        if target[0] == 'B' :
            for i in range(len(turn)-1, -1, -1):
                if turn[i][0] == 'O':
                    if Onow < turn[i][1]:
                        Onow += 1
                        break
                    elif Onow > turn[i][1]:
                        Onow -= 1
                        break
                    elif Onow == turn[i][1]:
                        break

            if Bnow < target[1] :
                Bnow += 1
            elif Bnow > target[1] :
                Bnow -= 1
            elif Bnow == target[1] :
                if len(turn) == 0 : break
                target = turn.pop()

        else :
            for i in range(len(turn)-1, -1, -1) :
                if turn[i][0] == 'B' :
                    if Bnow < turn[i][1] :
                        Bnow += 1
                        break
                    elif Bnow > turn[i][1] : 
                        Bnow -= 1
                        break
                    elif Bnow == turn[i][1] : 
                        break

            if Onow < target[1]:
                Onow += 1
            elif Onow > target[1]:
                Onow -= 1
            elif Onow == target[1]:
                if len(turn) == 0: break
                target = turn.pop()

    print(f'#{test_case} {second}')