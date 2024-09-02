import sys
col, row = map(int, sys.stdin.readline().split())
arr = []
for _ in range(col) :
    arr.append(list(map(str, sys.stdin.readline())))

visited = [0]*26
directy = [0, 0, 1, -1]
directx = [-1, 1, 0, 0]
lenmax = -21e8
def dfs(y, x, len):
    global lenmax
    lenmax = max(lenmax, len)

    for i in range(4):
        dy = directy[i]+y
        dx = directx[i]+x

        if dy<0 or dx<0 or dy>=col or dx>=row: continue
        if visited[ord(arr[dy][dx])-65] : continue
        visited[ord(arr[dy][dx])-65] = 1
        dfs(dy, dx, len+1)
        visited[ord(arr[dy][dx])-65] = 0

visited[ord(arr[0][0])-65] = 1
dfs(0, 0, 1)
print(lenmax)