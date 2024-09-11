def solution(people, limit):
    cnt = 0
    people.sort(reverse=True)
    st, ed = 0, len(people) - 1
    while st <= ed:
        if people[ed] + people[st] <= limit :
            ed -= 1
        st += 1
        cnt += 1
    return cnt