subject = int(input())
lst = list(map(int, input().split()))

mxnum = max(lst)

for i in range(subject) :
    lst[i] = lst[i] / mxnum * 100

sumrst = sum(lst)

print(sumrst/subject)