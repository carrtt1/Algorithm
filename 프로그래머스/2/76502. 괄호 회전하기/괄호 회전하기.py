from copy import deepcopy

def solution(s):
    lst = list(s)
    roundcnt, rightcnt = 0, 0

    while roundcnt < len(lst) :
        copylist = deepcopy(lst)
        stack = []
        while len(copylist) >= 1 :
            stack.append(copylist.pop())
            if len(stack) == 1 : continue
            if stack[len(stack)-1] == '[' :
                if stack[len(stack)-2] == ']' :
                    for i in range(2) :
                        stack.pop()
            elif stack[len(stack)-1] == '(' :
                if stack[len(stack)-2] == ')' :
                    for i in range(2) :
                        stack.pop()
            elif stack[len(stack)-1] == '{' :
                if stack[len(stack)-2] == '}' :
                    for i in range(2) :
                        stack.pop()
        if len(stack) == 0 :
            rightcnt += 1

        roundcnt += 1
        lst.append(lst.pop(0))
    return rightcnt