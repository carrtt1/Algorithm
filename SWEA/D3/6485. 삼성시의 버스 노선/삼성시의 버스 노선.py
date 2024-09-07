T = int(input())
for test_case in range(1, T + 1):

    totalbusstop = [0] * 5001

    buslinenum = int(input()) # 버스 노선의 갯수
    busline = [] # 노선이 어디부터 어디까지 가는지
    for _ in range(buslinenum) :
        busline.append(list(map(int, input().split())))

    targetbusstopnum = int(input()) # 찾아야 하는 정류장의 갯수
    targetbusstop = [] # 찾아야 하는 버스정류장
    for _ in range(targetbusstopnum) :
        targetbusstop.append(int(input()))

    for i in range(buslinenum) :
        for j in range(busline[i][0], busline[i][1]+1) :
            totalbusstop[j] += 1

    resultarr = []
    for i in range(targetbusstopnum) :
        resultarr.append(totalbusstop[targetbusstop[i]])

    print(f'#{test_case}', *resultarr)