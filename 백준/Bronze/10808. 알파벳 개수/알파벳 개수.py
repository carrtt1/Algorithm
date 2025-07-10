lst = list(input())
alphalst = [0] * 26

for i in lst :
    idx = ord(i)-97
    alphalst[idx] += 1

print(*alphalst)