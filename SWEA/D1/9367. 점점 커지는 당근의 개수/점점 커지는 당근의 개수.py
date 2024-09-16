T = int(input())
for test_case in range(1, T + 1):

    carrotnum = int(input())
    carrotbox = list(map(int, input().split()))

    count = 1
    counts = []
    for i in range(carrotnum-1) :
        if carrotbox[i+1] > carrotbox[i] :
            count += 1
            counts.append(count)
        else :
            counts.append(count)
            count = 1

    print(f'#{test_case} {max(counts)}')