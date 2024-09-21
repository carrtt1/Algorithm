T = int(input())
for test_case in range(1, T + 1):
    arrlen = int(input())

    arr = list(map(int, input().split()))

    maxvalue, maxi = 0, 0
    minvalue, mini = 101, 0
    for i in range(arrlen) :
        if arr[i] >= maxvalue :
            maxvalue = arr[i]
            maxi = i

    for i in range(arrlen-1, -1, -1) :
        if arr[i] <= minvalue :
            minvalue = arr[i]
            mini = i
            
    if maxi > mini :
        print(f'#{test_case} {maxi-mini}')
    elif mini > maxi :
        print(f'#{test_case} {mini-maxi}')