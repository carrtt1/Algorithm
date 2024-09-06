def dfs(level, idx, result):
    global Max

    if result <= Max:
        return

    if level == task:
        Max = max(Max, result)
        return

    for i in range(task):
        if comp[i] == 1: continue
        comp[i] = 1
        res = result * (arr[idx][i]*0.01)
        dfs(level + 1, idx+1, res)
        comp[i] = 0

T = int(input())
for test_case in range(1, T + 1):

    task = int(input())
    arr = []
    for i in range(task) :
        arr.append(list(map(int, input().split())))

    comp = [0] * task
    Max = -21e8

    dfs(0,0,1)
    print(f'#{test_case} {Max*100:.6f}')