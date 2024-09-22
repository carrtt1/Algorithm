for test_case in range(1, 11):
    dump = int(input())
    arr = list(map(int, input().split()))

    for i in range(dump) :
        maxvalue, maxj = 0, 0
        minvalue, minj = 1001, 0
        for j in range(100) :
            if arr[j] >= maxvalue :
                maxvalue = arr[j]
                maxj = j
            if arr[j] <= minvalue :
                minvalue = arr[j]
                minj = j
        arr[maxj]-=1
        arr[minj]+=1

    resultmax, resultmin = 0, 1001
    for i in range(100) :
        if arr[i] >= resultmax :
            resultmax = arr[i]
        if arr[i] <= resultmin :
            resultmin = arr[i]

    result = resultmax - resultmin

    print(f'#{test_case} {result}')