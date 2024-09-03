import sys
from collections import deque

# bfs를 위한 선언
q = deque()

# 도착해야 하는 값
edy, edx = map(int, sys.stdin.readline().split())
arr = [] # 미로

# 탐색해야 하는 미로
for _ in range(edy) :
    arr.append(list(map(int, sys.stdin.readline().strip())))

# 방문 체크 배열
visited = [[0]*edx for _ in range(edy)]

# idx를 탐색해야 하므로 -1
edy -= 1
edx -= 1
# 최솟값을 구하기 위한 값
Min = 21e8
# 방향 탐색을 위한 배열
directy = [0, 0, -1, 1]
directx = [-1, 1, 0, 0]

# stack에 sty, stx, level 값을 넣는다
q.append([0, 0, 1])

while q :
    sty, stx, level = q.popleft()

    if sty == edy and stx == edx :
        Min = min(Min, level)
        # break

    for i in range(4) :
        dy = directy[i] + sty
        dx = directx[i] + stx

        if dy < 0 or dx < 0 or dy > edy or dx > edx: continue
        if arr[dy][dx] == 0 : continue
        if visited[dy][dx] == 1 : continue
        visited[dy][dx] = 1
        q.append([dy, dx, level+1])

print(Min)