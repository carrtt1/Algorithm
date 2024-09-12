T = int(input())
for test_case in range(1, T + 1):

    people, pap = map(int, input().split())
    arr = [0] * (people + 1)
    lst = list(map(int, input().split()))

    def findboss(member) :
        if arr[member] == 0 :
            return member
        ret = findboss(arr[member])
        arr[member] = ret
        return ret

    def union(a, b) :
        ba, bb = findboss(a), findboss(b)
        if ba == bb :
            return
        arr[bb] = ba

    for i in range(1, len(lst)) :
        if i%2 == 1 :
            union(lst[i], lst[i-1])
    result = [0] * (people+1)
    for i in range(1, len(arr)) :
            res = findboss(i)
            result[i] = res

    print(f'#{test_case} {len(list(set(result)))-1}')