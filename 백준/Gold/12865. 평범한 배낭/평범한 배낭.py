n,k=map(int,input().split())
# 패딩값 넣은 배열선언
knapsack=[[0 for _ in range (k+1)] for _ in range(n+1)]
# 아이템 입력
item=[[0,0]]
for i in range(1,n+1):
    item.append(list(map(int,input().split())))

for i in range(1,n+1):  # 아이템의 개수
    for j in range(1,k+1): # 가방에 담을 수 있는 무게
        weight=item[i][0] # 아이템의 무게
        value=item[i][1]  # 아이템 만족도
        if j < weight: # 가방에 해당 아이템을 담을 수 없다면...
            knapsack[i][j]=knapsack[i-1][j]  # 사전단계에서 얻었던 값으로 update
        else: # j무게에 해당 물건을 넣을 수 있는 경우
            knapsack[i][j]=max(knapsack[i-1][j], value+knapsack[i-1][j-weight])
            # 사전 단계에서 얻은 최대치 vs 물건 하나 담았을떄 만족도 + 남은 무게에 대한 만족도의 최대값 
print(knapsack[n][k])