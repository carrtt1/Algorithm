str1 = list(input())
str2 = list(input())
cnt = 0
aarr = [0] * 26
barr = [0] * 26

for i in str1 :
    aarr[ord(i) - 97] += 1
for j in str2 :
    barr[ord(j) - 97] += 1

for z in range(26) :
    cnt += abs(aarr[z] - barr[z])

print(cnt)