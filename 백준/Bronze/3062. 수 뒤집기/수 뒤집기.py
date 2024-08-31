T = int(input())
for test_case in range(1, T+1) :

    num = input()
    numr = num[::-1]
    test = int(num) + int(numr)
    sen = list(map(int, str(test)))
    # print(sen)
    # print(sen[::-1])
    flag = 0

    if sen == sen[::-1] :
        flag = 1
    else :
        pass
        
    if flag == 1 :
        print('YES')
    else :
        print('NO')