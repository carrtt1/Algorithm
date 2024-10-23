citynum = int(input())
busnum = int(input())
inf = int(21e8)
arr = [[inf]*citynum for _ in range(citynum)]

for i in range(citynum) :
    for j in range(citynum) :
        if i == j :
            arr[i][j] = 0

for i in range(busnum) :
    st, ed, cost = map(int, input().split())
    arr[st-1][ed-1] = min(cost, arr[st-1][ed-1])

for i in range(citynum) :
    for j in range(citynum) :
        for n in range(citynum) :
            arr[j][n] = min(arr[j][n], arr[j][i]+ arr[i][n])

for i in range(citynum) :
    for j in range(citynum) :
        if arr[i][j] == inf :
            print(0, end=' ')
        else :
            print(arr[i][j], end=' ')
    print()