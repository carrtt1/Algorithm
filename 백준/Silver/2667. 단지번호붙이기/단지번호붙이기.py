import sys
sys.setrecursionlimit(10**7)
from collections import deque

arrlen = int(input())

arr = []
for i in range(arrlen) :
    arr.append(list(map(int, input())))

def bfs(y, x) :
    global Max
    q = deque()
    q.append((y, x))
    while q :
        sty, stx = q.popleft()
        for i in range(4) :
            dy = sty + directy[i]
            dx = stx + directx[i]

            if 0 <= dy < arrlen and 0 <= dx < arrlen and visited[dy][dx] == 0 :
                if arr[dy][dx] != 0 :
                    visited[dy][dx] = 1
                    Max += 1
                    q.append((dy, dx))

directy = [0, 0, 1, -1]
directx = [1, -1, 0, 0]
result = []
visited = [[0]*arrlen for _ in range(arrlen)]
cnt = 0
for i in range(arrlen) :
    for j in range(arrlen) :
        if arr[i][j] == 1 and visited[i][j] == 0 :
            Max = 0
            cnt += 1
            visited[i][j] = 1
            bfs(i, j)
            result.append(Max+1)
result.sort()

print(cnt)
for i in range(len(result)) :
    print(result[i])