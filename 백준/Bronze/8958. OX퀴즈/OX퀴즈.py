num = int(input())

for _ in range(num) :
    lst = list(input())

    rst, cnt = 0, 0

    for i in range(len(lst)) :
        if lst[i] == 'O' :
            cnt += 1
            rst += cnt
        else :
            cnt = 0

    print(rst)