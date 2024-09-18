T = int(input())
for test_case in range(1, T + 1):
    sen = input()

    count = 0
    flag = 1
    for i in range(len(sen)) :
        if i == len(sen)-1-count :
            break
        elif sen[i] == sen[len(sen)-1-count] :
            count += 1
        elif sen[i] != sen[len(sen)-1-count] :
            flag = 0
            break

    print(f'#{test_case} {flag}')