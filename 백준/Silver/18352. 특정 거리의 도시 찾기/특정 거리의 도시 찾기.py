import heapq
citynum, roadnum, minroad, start = map(int, input().split())

arr = [[] for _ in range(citynum)]
result = [21e8]*citynum
for _ in range(roadnum) :
    startcity, endcity = map(int, input().split())
    arr[startcity-1].append((1, endcity))

result[start-1] = 0
heap = [(0, start-1)]

while heap :
    nowdist, now = heapq.heappop(heap)

    if nowdist > result[now]: continue
    for distance, node in arr[now] :
        dis = nowdist + distance

        if dis < result[node-1] :
            result[node-1] = dis
            heapq.heappush(heap, (dis, node-1))
res = []
for i in range(len(result)) :
    if result[i] == minroad :
        res.append(i+1)

if len(res) == 0 :
    print(-1)
else :
    for i in range(len(res)) :
        print(res[i])