coinnum, totalwon = map(int, input().split())

coins = []
for i in range(coinnum) :
    coin = int(input())
    coins.append(coin)

arr = [0] * (totalwon + 1)
arr[0] = 1

for i in coins :
    for j in range(i, totalwon+1) :
        if j-i >= 0 :
            arr[j] += arr[j-i]

print(arr[totalwon])