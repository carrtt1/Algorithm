num = int(input())

arr = []

for i in range(1, num+1) :
    arr.append(str(i))

resultarr = []

for i in range(num) :
    cntthree = arr[i].count('3')
    cntsix = arr[i].count('6')
    cntnine = arr[i].count('9')
    if cntthree+cntsix+cntnine > 0 :
        resultarr.append('-'*(cntthree+cntsix+cntnine))
    else :
        resultarr.append(arr[i])

for i in range(len(resultarr)) :
    print(resultarr[i], end=' ')