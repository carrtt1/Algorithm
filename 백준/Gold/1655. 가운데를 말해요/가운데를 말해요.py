import heapq
import sys

n = int(sys.stdin.readline())

smheap = []
lgheap = []
for i in range(n):
    num = int(sys.stdin.readline())

    if len(smheap) == len(lgheap):
        heapq.heappush(smheap, -num)
    else:
        heapq.heappush(lgheap, num)

    if lgheap and lgheap[0] < -smheap[0]:
        leftvalue = heapq.heappop(smheap)
        rightvalue = heapq.heappop(lgheap)

        heapq.heappush(smheap, -rightvalue)
        heapq.heappush(lgheap, -leftvalue)

    print(-smheap[0])