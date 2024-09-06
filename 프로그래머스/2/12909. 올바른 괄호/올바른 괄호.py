def solution(s):
    flag = True
    lst = list(s)

    stack = []
    lst = list(reversed(lst))
    stack.append(lst.pop())

    while lst :
        stack.append(lst.pop())
        if stack[len(stack)-1] == ')' :
            if len(stack) == 1 :
                flag = False
                break
            if stack[len(stack)-2] == '(' :
                for _ in range(2) :
                    stack.pop()

    if len(stack) > 0 :
        flag = False

    return flag