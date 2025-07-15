swic = 0
while swic == 0 :
    numarr = list(map(int, input()))
    
    if numarr[0] == 0 :
        swic = 1
        break
    
    num = 0

    for i in numarr :
        if i == 1 :
            num += 2
        elif i == 0 :
            num += 4
        else :
            num += 3

    num += len(numarr)-1+2
    print(num)