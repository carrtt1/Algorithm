def dfs(level):
    global Max

    if level == changecnt:
        Max = max(Max, int(''.join(arr)))
        return

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            if [level, int(''.join(arr))] not in visited:
                visited.append([level, int(''.join(arr))])
                dfs(level + 1)
            arr[i], arr[j] = arr[j], arr[i]

T = int(input())
for test_case in range(1, T + 1):
    num, changecnt = map(str, input().split())
    changecnt = int(changecnt)
    arr = list(str(num))
    visited = []
    Max = -21e8

    dfs(0)
    print(f'#{test_case} {Max}')