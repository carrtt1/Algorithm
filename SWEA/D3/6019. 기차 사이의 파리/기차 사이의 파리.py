T = int(input())
for test_case in range(1,T+1):
    between, ta, tb, pari = map(int, input().split())
    result = (between / (ta + tb)) * pari
    print(f'#{test_case}{result: .10f}')