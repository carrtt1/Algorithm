T = int(input())
for test_case in range(1, T + 1):

    firstlen, secondlen = map(int, input().split())
    firstarr = list(map(int, input().split()))
    secondarr = list(map(int, input().split()))
    newarr = []
    resultarr = []

    sum = 0
    maxsum = -21e8
    if firstlen < secondlen :
        start = 0
        for j in range(secondlen-firstlen+1) :
            for i in range(j, j +firstlen) :
                newarr.append(secondarr[i])
            for n in range(firstlen) :
                sum += firstarr[n]*newarr[n]
            if sum > maxsum :
                maxsum = sum
            newarr = []
            sum = 0
    elif secondlen < firstlen :
        start = 0
        for j in range(firstlen - secondlen + 1):
            for i in range(j, j +secondlen):
                newarr.append(firstarr[i])
            for n in range(secondlen):
                sum += secondarr[n] * newarr[n]
            if sum > maxsum:
                maxsum = sum
            newarr = []
            sum = 0

    print(f'#{test_case} {maxsum}')