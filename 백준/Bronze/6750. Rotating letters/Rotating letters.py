lst = list(input())
yesstr = ['I', 'O', 'S', 'H', 'Z', 'X', 'N']
cnt = 0
for i in lst :
    if i in yesstr :
        cnt += 1

if cnt == len(lst) :
    print('YES')
else :
    print('NO')