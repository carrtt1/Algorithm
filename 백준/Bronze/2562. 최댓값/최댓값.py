lst = []

for _ in range(9) :
    num = int(input())
    lst.append(num)

maxnum = max(lst)
numidx = lst.index(maxnum) + 1

print(maxnum)
print(numidx)