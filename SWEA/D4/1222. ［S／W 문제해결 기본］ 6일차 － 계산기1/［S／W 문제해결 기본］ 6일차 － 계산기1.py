for test_case in range(1, 11):
    senlen = int(input())
    sen = list(map(str, input()))

    while '+' in sen :
        sen.remove('+')

    sum = 0
    for i in range(len(sen)) :
        sum += int(sen[i])

    print(f'#{test_case} {sum}')