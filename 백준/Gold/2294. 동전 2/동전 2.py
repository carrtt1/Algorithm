n,k=map(int,input().split())
coin=[]
for i in range(n):
    value=int(input())
    coin.append(value)

coin.sort()
arr=[10001]*(k+1)
arr[0]=0
for i in range(n):
    start=coin[i]
    for j in range(start,k+1):
        arr[j]=min(arr[j],arr[j-start]+1)

if arr[k]>=10001:
    print(-1)
else:
    print(arr[k])