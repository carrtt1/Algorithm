import sys
sys.setrecursionlimit(10**5)

T = int(input())
for _ in range(1, T + 1):

    def dfs(i, j):
        directy = [0, 0, -1, 1]
        directx = [-1, 1, 0, 0]

        for n in range(4):
            dy = directy[n] + i
            dx = directx[n] + j

            if dy < 0 or dx < 0 or dy >= collen or dx >= rowlen: continue
            if ground[dy][dx] == 0: continue
            ground[dy][dx] = 0
            dfs(dy, dx)


    # 가로 길이, 세로 길이, 배추의 개수
    rowlen, collen, cabbages = map(int, input().split())

    # 0으로 채워진 배열 선언 및 초기화
    ground = [[0] * rowlen for _ in range(collen)]

    # 배추의 개수만큼 반복문을 돌려 배추의 위치에 1을 넣는다
    for _ in range(cabbages):
        x, y = map(int, input().split())
        ground[y][x] = 1

    count = 0

    for i in range(collen):
        for j in range(rowlen):
            if ground[i][j] == 1:
                count += 1
                ground[i][j] = 0
                dfs(i, j)

    print(count)