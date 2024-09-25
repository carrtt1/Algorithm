T = int(input())
for test_case in range(1, T + 1):

    numlen = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    resultarr = []
    st = 0

    for _ in range(5) :
        maxvalue, minvalue = 0, 21e8
        for i in range(st, len(arr)-st) :
            if arr[i] > maxvalue :
                maxvalue = arr[i]
            if arr[i] < minvalue :
                minvalue = arr[i]
        st += 1
        resultarr.append(maxvalue)
        resultarr.append(minvalue)

    print(f'#{test_case}', *resultarr)