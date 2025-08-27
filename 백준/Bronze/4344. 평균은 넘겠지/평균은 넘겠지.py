num = int(input())

for _ in range(num) :
    lst = list(map(int, input().split()))

    snum = 0
    for i in range(lst[0]) :
        snum += lst[i+1]

    df = snum / lst[0]
    cnt = 0

    for j in range(lst[0]) :
        if lst[j+1] > df :
            cnt += 1

    rst = cnt/lst[0] * 100
    print(f'{round(rst, 3)}%')