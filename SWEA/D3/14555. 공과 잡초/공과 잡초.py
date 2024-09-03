T = int(input())
for test_case in range(1, T + 1):

    sen = list(map(str, input()))
    
    count = 0
    
    for i in range(len(sen)) :
        if i+1 > len(sen) : break
        if sen[i] == '(' :
            if sen[i+1] == ')' or sen[i+1] == '|' :
                count += 1
                sen[i], sen[i+1] = '.', '.'
        if sen[i] == ')' :
            if sen[i-1] == '|' :
                count += 1
                sen[i], sen[i-1] = '.', '.'
    
    print(f'#{test_case} {count}')