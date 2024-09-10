people = int(input())
arr = list(map(int, input().split()))
arr.sort()
resultarr = [0]*people
Sum = 0
for i in range(people) :
    Sum+=arr[i]
    resultarr[i] = Sum

print(sum(resultarr))