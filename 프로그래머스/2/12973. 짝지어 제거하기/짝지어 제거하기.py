def solution(s):
    answer = 0
    lst = list(s)
    stack = []

    while len(lst) > 0 :
        stack.append(lst.pop())
        if len(stack) <= 1 : continue
        if stack[len(stack)-1] == stack[len(stack)-2] :
            for i in range(2) :
                stack.pop()
    if len(stack) == 0 :
        answer = 1
    
    return answer