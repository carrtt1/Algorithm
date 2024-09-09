def solution(brown, yellow):
    height, width = 0, 0
    for h in range(brown) :
        if h <= 2 : continue
        w = (brown - 2*(h-2))//2
        if (h-2)*(w-2) == yellow :
            height, width = h, w
            break
    answer = [width, height]
    return answer