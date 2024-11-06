import sys
sys.setrecursionlimit(10000)

def dfs(y, x) :
    for i in range(4) :
        dy = directy[i] + y
        dx = directx[i] + x

        if dy < 0 or dx < 0 or dy >= col or dx >= row : continue
        if arr[dy][dx] == '.' : continue
        arr[dy][dx] = '.'
        dfs(dy, dx)

test_case = int(input())
for _ in range(test_case) :
    col, row = map(int, input().split())
    arr = []
    for i in range(col) :
        lst = list(map(str, input()))
        arr.append(lst)

    cnt = 0
    directy = [0, 0, 1, -1]
    directx = [-1, 1, 0, 0]
    for i in range(col) :
        for j in range(row) :
            if arr[i][j] == '#' :
                cnt += 1
                dfs(i, j)

    print(cnt)