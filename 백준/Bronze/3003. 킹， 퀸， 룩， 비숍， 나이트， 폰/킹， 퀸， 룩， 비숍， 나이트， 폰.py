lst = list(map(int, input().split()))

chess = [1, 1, 2, 2, 2, 8]
rst = [0, 0, 0, 0, 0, 0]
for i in range(6) :
    if chess[i] == lst[i] :
        rst[i] = 0
    else :
        rst[i] = chess[i] - lst[i]

print(*rst)