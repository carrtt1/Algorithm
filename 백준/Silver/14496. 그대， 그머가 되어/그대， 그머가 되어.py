import heapq

st, ed = map(int, input().split())
totallen, changenum = map(int, input().split())

change = [[] for _ in range(totallen)]

for _ in range(changenum) :
    chst, ched = map(int, input().split())
    change[chst-1].append((1, ched))
    change[ched-1].append((1, chst))

result = [21e8] * totallen

result[st-1] = 0
heap = [(0, st-1)]

while heap :
    distance, now = heapq.heappop(heap)

    if distance > result[now] : continue

    for dis, node in change[now] :

        cdist = dis + distance

        if cdist < result[node-1] :
            result[node-1] = cdist
            heapq.heappush(heap, (cdist, node-1))

if result[ed-1] == 21e8 :
    print(-1)
else :
    print(result[ed-1])