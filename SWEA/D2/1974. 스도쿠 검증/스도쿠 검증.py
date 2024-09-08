T = int(input())
for test_case in range(1, T + 1):

    # arr에 값넣기
    arr = []
    for _ in range(9) :
        arr.append(list(map(int, input().split())))
    
    sqresultarr = []

    # 네모의 합을 구해 내보내는 함수
    def culsum(i, j) :
        sum = 0
        dx = [-1, 1, 0, 0, -1, 1, 1, -1] # 상하좌우왼위부터시계방향
        dy = [0, 0, -1, 1, -1, -1, 1, 1]
        for n in range(8) :
            dxx = i+dx[n]
            dyy = j+dy[n]
            if dyy<0 or dyy>8 or dxx<0 or dxx>8 :
                continue
            sum += arr[dxx][dyy]
        sum = sum + arr[i][j]
        return sum

    for i in range(1, 9, 3) :
        for j in range(1, 9, 3) :
            # 좌표 계산 함수
            sum = culsum(i, j)
            # 만약 네모 안의 합이 45가 아니라면 0
            if sum != 45 :
                sqresultarr.append(0)
            else :
                sqresultarr.append(1)

    # 가로 합 구하기
    rowarr = []

    for i in range(9) :
        rowsum = 0
        for j in range(9) :
            rowsum += arr[i][j]
        if rowsum != 45 :
            rowarr.append(0)
        else :
            rowarr.append(1)

    # 세로 합 구하기
    colarr = []

    for i in range(9) :
        colsum = 0
        for j in range(9) :
            colsum += arr[j][i]
        if colsum != 45 :
            colarr.append(0)
        else :
            colarr.append(1)

    resultvalue = 1
    for i in range(9) :
        if sqresultarr[i] == 0 or rowarr[i] == 0 or colarr[i] == 0 :
            resultvalue = 0
            break

    print(f'#{test_case} {resultvalue}')