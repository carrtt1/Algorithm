
def dfs(y,x,level,dir):
    global Max_level
    if y==endy and x==endx:
        Max_level=max(Max_level,level)
        return

    for i in range(dir,4):
        dy=directy[i]+y
        dx=directx[i]+x
        if dy<0 or dy>n-1 or dx<0 or dx>n-1:continue
        if used[arr[dy][dx]]!=0: continue
        used[arr[dy][dx]]=1
        dfs(dy,dx,level+1,i)
        used[arr[dy][dx]]=0

testcase=int(input())
for tc in range(1,testcase+1):
    ans=0
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    used=[0]*101
    Max_level=-21e8
    directy = [1, 1, -1, -1]
    directx = [1, -1, -1, 1]
    for i in range(n):
        for j in range(n):
            if (i==0 or i==n-1)and(j==0 or j==n-1): continue
            endy=i+1
            endx=j-1
            used[arr[i][j]]=1
            dfs(i,j,0,0)
            used = [0] * 101

    if Max_level<3: print(f'#{tc} {-1}')
    else: print(f'#{tc} {Max_level+1}')
