yul, num = map(int, input().split())
lst = list(map(int, input().split()))
rst = []

for i in range(yul) :
    if lst[i] < num :
        rst.append(lst[i])

print(*rst)