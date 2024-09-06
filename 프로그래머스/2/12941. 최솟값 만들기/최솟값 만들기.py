def solution(A,B):
    arrA = sorted(A)
    arrB = sorted(B, reverse=True)
    Sum = 0
    for i in range(len(arrA)) :
        Sum += arrA[i]*arrB[i]
    return Sum