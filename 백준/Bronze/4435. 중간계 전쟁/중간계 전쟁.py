num = int(input())

for i in range(num) :
    gandarp = list(map(int, input().split()))
    sauron = list(map(int, input().split()))

    ganarr = [1, 2, 3, 3, 4, 10]
    sauarr = [1, 2, 2, 2, 3, 5, 10]
    gandrst, sourrst = 0, 0

    for j in range(6) :
        if gandarp[j] == 0 : pass
        else :
            gandrst += gandarp[j] * ganarr[j]
    for z in range(7) :
        if sauron[z] == 0 : pass
        else :
            sourrst += sauron[z] * sauarr[z]
    if gandrst > sourrst :
        print(f'Battle {i+1}: Good triumphs over Evil')
    elif gandrst < sourrst :
        print(f'Battle {i+1}: Evil eradicates all trace of Good')
    else :
        print(f'Battle {i+1}: No victor on this battle field')