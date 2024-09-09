def solution(s):
    lst = list(map(str, s.upper()))
    for i in range(len(lst)) :
        if lst[i] == ' ' :
            continue
        else :
            if i-1 >= 0 :
                if lst[i-1] != ' ' :
                    lst[i] = lst[i].lower()
    sen = ''.join(lst)
    return sen