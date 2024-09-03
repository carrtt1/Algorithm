bingo = []

for _ in range(5) :
    bingo.append(list(map(int, input().split())))

delnumlst = []
bingocount, downcount, upcount = 0, 0, 0

for _ in range(5) :
    delnumlst.append(list(map(int, input().split())))

def searchline(y, x) :
    global bingocount, downcount, upcount
    lst = []
    # 세로
    for i in range(5) :
        lst.append(bingo[i][x])
        if lst == [0, 0, 0, 0, 0] :
            bingocount += 1
    lst = []
    # 가로
    for i in range(5) :
        lst.append(bingo[y][i])
        if lst == [0, 0, 0, 0, 0] :
            bingocount += 1
    lst = []
    #우상향대각선
    if upcount == 0 :
        for i in range(5) :
            lst.append(bingo[i][4-i])
        if lst == [0, 0, 0, 0, 0]:
            upcount += 1
        lst = []
    # 우하향대각선
    if downcount == 0 :
        for i in range(5) :
            lst.append(bingo[i][i])
        if lst == [0, 0, 0, 0, 0]:
            downcount += 1
        lst = []

def findbingo(num) :
    for i in range(5) :
        for j in range(5) :
            if num == bingo[i][j] :
                bingo[i][j] = 0
                searchline(i, j) # 빙고 된 라인 개수 세는 함수
                return

count, result = 0, 0
for i in range(5) :
    for j in range(5) :
        count += 1
        findbingo(delnumlst[i][j]) # 빙고판에서 부른 값을 찾는 함수
        if bingocount+upcount+downcount >= 3 :
            if result == 0 and count > result :
                result = count
                break

print(result)