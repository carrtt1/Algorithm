import sys
from collections import deque

row, col = map(int, sys.stdin.readline().split())
arr = []
for _ in range(col) :
    arr.append(list(map(int, sys.stdin.readline().split())))

directy = [0, 0, -1, 1]
directx = [1, -1, 0, 0]
q = deque()

for i in range(col):
    for j in range(row):
        if arr[i][j] == 1 :
            q.append((i, j))

while q:
    nowy, nowx = q.popleft()

    for i in range(4):
        dy = directy[i] + nowy
        dx = directx[i] + nowx

        if dy < 0 or dx < 0 or dy >= col or dx >= row: continue
        if arr[dy][dx] == -1 or arr[dy][dx] > 0: continue
        arr[dy][dx] = arr[nowy][nowx] + 1
        q.append((dy, dx))

flag = 0

for i in range(col) :
    if 0 in arr[i] : flag = 1
Max = -21e8
for i in range(col) :
    for j in range(row):
        Max = max(Max, arr[i][j])
if flag == 1 :
    print(-1)
else :
    print(Max-1)