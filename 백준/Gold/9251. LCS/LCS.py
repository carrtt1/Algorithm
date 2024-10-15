sen1 = input()
sen2 = input()

def lcs(sen1, sen2) :
    len1, len2 = len(sen1), len(sen2)
    arr = [[0]*(len2+1) for _ in range(len1+1)]

    maxvalue = 0
    for i in range(1, len1+1) :
        for j in range(1, len2+1) :
            if sen1[i-1] == sen2[j-1] :
                arr[i][j] = arr[i-1][j-1]+1
                maxvalue = max(maxvalue, arr[i][j])
            else :
                arr[i][j] = max(arr[i-1][j], arr[i][j-1])
                maxvalue = max(maxvalue, arr[i][j])
    return maxvalue


maxvalue = lcs(sen1, sen2)
print(maxvalue)