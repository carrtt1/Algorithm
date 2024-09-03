import sys
from collections import deque
nodenum = int(sys.stdin.readline())
arr = [[] for _ in range(nodenum+1)]

for i in range(nodenum - 1):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

parents = [0] * (nodenum+1)
q = deque()
q.append((1,1))

while q :
    par, now = q.popleft()
    parents[now] = par
    for i in range(len(arr[now])):
        if parents[arr[now][i]]: continue
        q.append((now, arr[now][i]))

for i in range(2, len(parents)):
    print(parents[i])