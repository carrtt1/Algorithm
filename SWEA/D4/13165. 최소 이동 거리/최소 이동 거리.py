import heapq
T = int(input())
for test_case in range(1, T + 1):

    finalend, roadnum = map(int, input().split())
    arr = [[] for _ in range(finalend+1)]

    for i in range(roadnum) :
        st, ed, dist = map(int, input().split())
        arr[st].append((dist, ed))

    result = [21e8] * (finalend+1)
    result[0] = 0
    heap = [(0, 0)]

    while heap :
        distance, now = heapq.heappop(heap)

        if distance > result[now] : continue

        for ndist, n in arr[now] :
            res = result[n]
            newdist = ndist + distance

            if res > newdist :
                result[n] = newdist
                heapq.heappush(heap, (newdist, n))

    print(f'#{test_case} {result[len(result)-1]}')