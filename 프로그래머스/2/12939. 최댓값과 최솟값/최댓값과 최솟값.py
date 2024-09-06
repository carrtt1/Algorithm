def solution(s):
    lst = list(map(int, s.split()))
    maxv = max(lst)
    minv = min(lst)
    answer = f'{minv} {maxv}'
    return answer