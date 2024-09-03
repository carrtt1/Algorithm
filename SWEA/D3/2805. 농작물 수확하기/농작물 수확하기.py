T = int(input())
for test_case in range(1, T + 1):

    farmlen = int(input())
    farm = []
    for _ in range(farmlen) :
        farm.append(list(map(int, input())))

    center = farmlen//2+1
    resultsum = 0

    st, ed = center, center
    for i in range(farmlen) :
        if i <= center-1 :
            for j in range(st-1, ed) :
                resultsum += farm[i][j]
            st -= 1
            ed += 1
        elif i > center-1 :
            for j in range(st+1, ed-2) :
                resultsum += farm[i][j]
            st += 1
            ed -= 1

    print(f'#{test_case} {resultsum}')