import sys
from collections import deque

directy = [0, 0, 1, -1, -1, -1, 1, 1]
directx = [1, -1, 0, 0, -1, 1, -1, 1]

def bfs(y, x) :
    q=deque()
    q.append((y, x))

    while q:
        sy, sx = q.popleft()
        # arr[sy][sx] = 0
        for i in range(8):
            dy = directy[i]+sy
            dx = directx[i]+sx

            if dy<0 or dx<0 or dy>=col or dx>=row : continue
            if arr[dy][dx] == 0 : continue
            arr[dy][dx] = 0
            q.append((dy, dx))

while 1:
    row, col = map(int, sys.stdin.readline().split())
    if row == 0 and col == 0 : break

    arr = []
    cnt = 0

    for _ in range(col):
        arr.append(list(map(int, sys.stdin.readline().split())))

    for i in range(col):
        for j in range(row):
            if arr[i][j] == 1:
                cnt+= 1
                bfs(i, j)
    print(cnt)