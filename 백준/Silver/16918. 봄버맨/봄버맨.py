from collections import deque
from sys import stdin
r, c, n = map(int, stdin.readline().split())

arr = []
for _ in range(r):
    arr.append(list(stdin.readline().strip()))

def bfs(q):
    while q:
        y, x = q.popleft()
        arr[y][x] = '.'
        for l in range(4):
            dy = directy[l] + y
            dx = directx[l] + x
            if 0 <= dx < c and 0 <= dy < r and arr[dy][dx] == 'O':
                arr[dy][dx] = '.'

q = deque()
directy = [-1, 1, 0, 0]
directx = [0, 0, -1, 1]

if n == 1:
    for g in arr:
        print(*g, sep='')
else:
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 'O':
                q.append((i, j))
    for k in range(1,n):
        if (k+1) % 2 == 0:
            for i in range(r):
                for j in range(c):
                    if arr[i][j] == '.':
                        arr[i][j] = 'O'
            if (k+1) == n:
                for g in arr:
                    print(*g, sep='')
        else:
            bfs(q)
            for i in range(r):
                for j in range(c):
                    if arr[i][j] == 'O':
                        q.append((i, j))
            if (k+1) == n:
                for g in arr:
                    print(*g, sep='')