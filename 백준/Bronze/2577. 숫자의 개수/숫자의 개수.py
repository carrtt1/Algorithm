num1 = int(input())
num2 = int(input())
num3 = int(input())

rstnum = num1 * num2 * num3
arr = list(map(int, str(rstnum)))

numarr = [0] * 10

for i in arr :
    cnt = arr.count(i)
    numarr[i] = cnt

for i in range(10) :
    print(numarr[i])