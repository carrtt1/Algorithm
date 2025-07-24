roomnum = list(map(int, input()))

numset = [0]*10

for i in roomnum :
    if i == 6 or i == 9 :
        if numset[6] < numset[9] :
            numset[6] += 1
        else :
            numset[9] += 1
    else :
        numset[i] += 1

print(max(numset))