import sys
sys.setrecursionlimit(10**7)

arrlen = int(input())
arr = []
for i in range(arrlen) :
    arr.append(list(map(int, input().split())))

def dfs(sty, stx, water) :
    visited[sty][stx] = 1
    for i in range(4) :
        dy = sty + directy[i]
        dx = stx + directx[i]

        if dy < 0 or dx < 0 or dy >= arrlen or dx >= arrlen : continue
        if visited[dy][dx] == 1 : continue
        if arr[dy][dx] <= water : continue

        dfs(dy, dx, water)

directx = [0, 0, 1, -1]
directy = [1, -1, 0, 0]

maxground = 0 # 가장 많은 땅

# 수위 조절 반복문
for n in range(101) :
    count = 0
    # 방문 체크
    visited = [[0]*arrlen for _ in range(arrlen)]
    for i in range(arrlen) :
        for j in range(arrlen) :
            if arr[i][j] > n and visited[i][j] == 0 :
                count += 1
                dfs(i, j, n)

    maxground = max(count, maxground)

print(maxground)