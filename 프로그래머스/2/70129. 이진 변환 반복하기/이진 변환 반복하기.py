def solution(s):
    cnt = 0
    zerorem = 0

    while len(s) != 1 :
        cnt += 1
        lst = list(map(str, s))
        onecnt = lst.count('1')
        zerocnt = lst.count('0')
        zerorem += zerocnt
        s = bin(onecnt)[2::]

    answer = [cnt, zerorem]

    return answer