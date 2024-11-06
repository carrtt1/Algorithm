n = int(input())
arr = []
for i in range(n) :
    lst = list(map(int, input().split()))
    arr.append(lst)

visited = [0] * n
result = 21e8

def dfs(start, now, cost) :
    global result

    if start == now and 0 not in visited :
        result = min(result, cost)
        return

    if cost > result :
        return

    for i in range(n) :
        if arr[now][i] != 0 and visited[i] == 0 :
            visited[i] = 1
            dfs(start, i, cost + arr[now][i])
            visited[i] = 0

dfs(0, 0, 0)
print(result)