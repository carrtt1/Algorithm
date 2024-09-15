T = int(input())
for test_case in range(1, T + 1):
    box, work = map(int, input().split())
    arr = [0]*box
    for i in range(1, work+1) :
        st, ed = map(int, input().split())
        for j in range(st, ed+1) :
            arr[j-1] = i
    print(f'#{test_case}', *arr)