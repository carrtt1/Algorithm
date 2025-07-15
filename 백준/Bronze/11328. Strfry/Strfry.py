num = int(input())

for i in range(num) :
    astr, bstr = input().split()

    if sorted(astr) == sorted(bstr) :
        print('Possible')
    else :
        print('Impossible')