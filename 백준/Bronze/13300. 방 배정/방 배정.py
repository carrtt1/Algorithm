student, roommax = map(int, input().split())

arr = [[0, 0, 0, 0, 0, 0] for _ in range(2)]

for i in range(student) :
    gen, grade = map(int, input().split())

    if gen == 0 :
        arr[0][grade-1] += 1
    elif gen == 1 :
        arr[1][grade-1] += 1

cnt = 0

for i in range(2) :
    for j in range(6) :
        if arr[i][j] == 0 : pass
        elif arr[i][j] > roommax :
            cnt += arr[i][j] // roommax
            if arr[i][j] % roommax > 0 :
                cnt += 1
        else :
            cnt += 1

print(cnt)