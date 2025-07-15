swic = 0
while swic == 0 :
    nstr = list(input().upper())
    if nstr[0] == '#' :
        swic = 1
        break

    cnt = 0
    
    cnt += nstr.count('A')
    cnt += nstr.count('E')
    cnt += nstr.count('I')
    cnt += nstr.count('O')
    cnt += nstr.count('U')

    print(cnt)