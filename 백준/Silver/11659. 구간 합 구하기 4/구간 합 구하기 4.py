import sys
nums, sumnums = map(int, sys.stdin.readline().split())
numsarr = list(map(int, sys.stdin.readline().split()))

nusum = []
Sum = 0
for i in range(nums) :
    Sum+= numsarr[i]
    nusum.append(Sum)

for i in range(sumnums) :
    st, ed = map(int, sys.stdin.readline().split())
    if st == 1 :
        print(nusum[ed-1])
    else :
        print(nusum[ed-1]-nusum[st-2])