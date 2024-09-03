T = int(input())
for test_case in range(1, T + 1):

    num = int(input())

    arr = [0] * 10
    sum = 0
    count = 0

    while sum < 10 :
        count += 1
        culnum = num * count
        for i in range(len(str(culnum))) :
            if arr[int(str(culnum)[i])] == 1 :
                pass
            elif arr[int(str(culnum)[i])] == 0 :
                arr[int(str(culnum)[i])] = 1
        for i in range(10) :
            sum += arr[i]
        if sum < 10 :
            sum = 0
    if sum == 10 :
        print(f'#{test_case} {culnum}')