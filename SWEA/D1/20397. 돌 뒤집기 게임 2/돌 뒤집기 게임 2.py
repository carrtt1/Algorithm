T = int(input())
for test_case in range(1, T + 1):

    stonelen, changecnt = map(int, input().split())

    origin = list(map(int, input().split()))
    for i in range(changecnt):
        target, chgstone = map(int, input().split())
        for j in range(1, chgstone+1):
            if target-1-j<0 or target-1+j>=stonelen: continue
            if origin[target-1-j] == origin[target-1+j] :
                if origin[target - 1 - j] == 1 :
                    origin[target - 1 - j], origin[target - 1 + j] = 0, 0
                elif origin[target - 1 + j] == 0 :
                    origin[target - 1 - j], origin[target - 1 + j] = 1, 1

    print(f'#{test_case}', *origin)