lst = []

for _ in range(10) :
    num = int(input())
    pernum = num % 42
    if pernum not in lst :
        lst.append(pernum)

print(len(lst))