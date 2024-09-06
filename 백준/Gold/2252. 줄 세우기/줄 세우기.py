from collections import deque
import sys

students, totalcnt = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(students+1)]
acc = [0] * (students+1)

for i in range(totalcnt) :
    sa, sb = map(int, sys.stdin.readline().split())
    arr[sa].append(sb)
    acc[sb] += 1

used = [0] * (students+1)
q = deque()

for i in range(1, students+1) :
    if acc[i] == 0 :
        used[i] = 1
        q.append(i)
        
result = []

while q :
    now = q.popleft()
    result.append(now)
    for i in arr[now] :
        if used[i] == 0 :
            if acc[i] == 1 :
                used[i] = 1
                acc[i] -= 1
                q.append(i)
            else :
                acc[i] -= 1

print(*result)