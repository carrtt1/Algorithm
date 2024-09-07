T = int(input())
for test_case in range(1, T + 1):

    boxlen = int(input())
    arr = list(map(int, input().split()))
    resultarr = []

    # 박스 길이만큼 반복
    for i in range(boxlen):
        # 좌표 박스보다 작은 박스의 갯수를 담을 count 선언 및 초기화
        count = 0
        # i 좌표 박스랑 비교하기 위한 반복문
        for j in range(i + 1, boxlen):
            # 만약 좌표 박스가 반복문 박스보다 크다면
            if arr[i] > arr[j]:
                # count에 1을 더함
               count += 1
        # count한 수를 resultarr 배열에 넣음
        resultarr.append(count)
    # resultarr의 최댓값 출력
    print(f'#{test_case} {max(resultarr)}')