limittime = int(input())
stack = []
result = 0
for i in range(limittime) :
    arr = list(map(int, input().split()))
    if arr[0] == 0 :
        if stack :
            time, score = stack.pop()
            if time > 0 :
                if time == 1 :
                    result += score
                else :
                    stack.append((time-1, score))
    else :
        newtask = arr[0]
        score = arr[1]
        time = arr[2]
        if time-1 == 0 :
            result += score
        else :
            stack.append((time-1, score))

print(result)