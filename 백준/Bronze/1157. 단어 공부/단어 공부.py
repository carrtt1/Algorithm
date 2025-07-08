arr = list(input().upper())

fndlst = list(set(arr))
lst = []

for i in fndlst :
    num = arr.count(i)
    lst.append(num)

if lst.count(max(lst)) >= 2 :
    print('?')
else :
    print(fndlst[lst.index(max(lst))])