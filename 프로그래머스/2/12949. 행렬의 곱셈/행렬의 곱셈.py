def solution(arr1, arr2):
    arrlen = len(arr2[0])
    answer = [[0]*arrlen for _ in range(len(arr1))]
    lists = []
    
    for i in range(len(arr1)): 
        for j in range(arrlen): 
            for n in range(len(arr1[0])): 
                answer[i][j] += arr1[i][n] * arr2[n][j]
                
    return answer