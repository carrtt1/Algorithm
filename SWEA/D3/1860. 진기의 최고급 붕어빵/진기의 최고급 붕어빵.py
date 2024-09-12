T = int(input())
for test_case in range(1, T + 1):

    people, bongsecond, bong = map(int, input().split())
    guest = list(map(int, input().split()))
    second = 0
    compbong = 0
    flag = 0
    if 0 in guest :
        flag = 1
    else :
        while second <= guest[people-1] :
            second += 1
            if second%bongsecond == 0 :
                compbong += bong
            if second in guest :
                compbong -= 1

            if compbong < 0 :
                flag = 1
                break

    if flag :
        print(f'#{test_case} Impossible')
    else :
        print(f'#{test_case} Possible')