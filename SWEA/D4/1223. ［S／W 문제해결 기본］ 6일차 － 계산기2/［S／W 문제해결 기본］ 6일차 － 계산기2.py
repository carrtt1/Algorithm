for test_case in range(1, 11):

    senlen = int(input())
    sen = list(map(str, input()))

    stack = []

    while len(sen) > 0 :
        stack.append(sen.pop())
        if len(stack) <= 1 : continue
        if stack[len(stack)-1] == '*' :
            stack.append(sen.pop())
            value = int(stack[len(stack)-1]) * int(stack[len(stack)-3])
            for _ in range(2) :
                stack.pop()
            stack[len(stack)-1] = value

    while '+' in stack :
        stack.remove('+')

    result = 0
    for i in range(len(stack)) :
        result += int(stack[i])

    print(f'#{test_case} {result}')