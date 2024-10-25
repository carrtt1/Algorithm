housenum = int(input())
houses = []

for i in range(housenum) :
    houses.append(list(map(int, input().split())))

for i in range(1, housenum) :
    houses[i][0] = min(houses[i-1][1], houses[i-1][2]) + houses[i][0]
    houses[i][1] = min(houses[i-1][0], houses[i - 1][2]) + houses[i][1]
    houses[i][2] = min(houses[i-1][0], houses[i - 1][1]) + houses[i][2]

print(min(houses[len(houses)-1]))