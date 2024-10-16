import sys
from collections import deque
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def bfs1(sty, stx) :
    q = deque()
    q.append((sty, stx))
    visited[sty][stx] = 1

    while q :
        y, x = q.popleft()

        for i in range(4) :
            dy = directy[i] + y
            dx = directx[i] + x

            if 0 <= dy < arrlen and 0 <= dx < arrlen and not visited[dy][dx] :
                if arr[y][x] == arr[dy][dx] :
                    q.append((dy, dx))
                    visited[dy][dx] = 1

arrlen = int(input())

arr = []
for i in range(arrlen) :
    arr.append(list(map(str, input())))

directy = [0, 0, 1, -1]
directx = [1, -1, 0, 0]
visited = [[0] * arrlen for _ in range(arrlen)]

countv, count = 0, 0

for i in range(arrlen) :
    for j in range(arrlen) :
        if visited[i][j] == 0 :
            bfs1(i, j)
            count += 1

for i in range(arrlen) :
    for j in range(arrlen) :
        if arr[i][j] == 'R' :
            arr[i][j] = 'G'

visited = [[0] * arrlen for _ in range(arrlen)]

for i in range(arrlen) :
    for j in range(arrlen) :
        if visited[i][j] == 0 :
            bfs1(i, j)
            countv += 1

print(count, countv)