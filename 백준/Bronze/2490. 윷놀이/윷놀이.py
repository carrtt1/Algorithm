for _ in range(3) :
    lst = list(map(int, input().split()))

    yut = ['E', 'A', 'B', 'C', 'D']
    cnt = lst.count(0)

    print(yut[cnt])