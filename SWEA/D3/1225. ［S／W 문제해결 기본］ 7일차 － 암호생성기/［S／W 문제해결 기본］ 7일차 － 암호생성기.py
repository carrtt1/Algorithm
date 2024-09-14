from collections import deque

for _ in range(1, 11):

    test_case = int(input())
    lst = list(map(int, input().split()))
    q = deque()

    for i in range(8) :
        q.append(lst[i])

    resultarr = []
    n=1

    while q :
        lastnum = q.popleft()
        if lastnum-n <= 0 :
            q.append(0)
            break
        q.append(lastnum-n)
        n+=1
        if n == 6 :
            n = 1

    print(f'#{test_case}', *q)