import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) > 1 :
        temp1 = heapq.heappop(scoville)
        if temp1 < K :
            answer += 1
        temp2 = heapq.heappop(scoville)
        heapq.heappush(scoville, temp1 + temp2*2)
    
    now = heapq.heappop(scoville)
    if now < K :
        answer = -1
        
    return answer