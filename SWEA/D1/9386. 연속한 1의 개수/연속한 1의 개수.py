T = int(input())
for test_case in range(1, T + 1):
    arrlen = int(input())
    arr = list(map(int, input()))
    resultarr = []

    for i in range(arrlen) :
        if arr[i] == 0 :
            count = 0
            resultarr.append(count)
        elif arr[i] == 1 :
            count += 1
            resultarr.append(count)

    print(f'#{test_case} {max(resultarr)}')