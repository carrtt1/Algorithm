swic = 0
while swic == 0 :
    arr = list(input())
    
    if arr[0] == '#' :
        swic = 1
        break
    
    res = 0

    for i in range(len(arr)):
        if arr[i] == '~':
            res += 8 ** (len(arr)-1-i) * 0
        elif arr[i] == "\\":
            res += 8 ** (len(arr) - 1 - i) * 1
        elif arr[i] == "(":
            res += 8 ** (len(arr) - 1 - i) * 2
        elif arr[i] == "@":
            res += 8 ** (len(arr) - 1 - i) * 3
        elif arr[i] == "?":
            res += 8 ** (len(arr) - 1 - i) * 4
        elif arr[i] == ">":
            res += 8 ** (len(arr) - 1 - i) * 5
        elif arr[i] == "&":
            res += 8 ** (len(arr) - 1 - i) * 6
        elif arr[i] == "%":
            res += 8 ** (len(arr) - 1 - i) * 7
        elif arr[i] == "/":
            res += 8 ** (len(arr) - 1 - i) * -1
    print(res)