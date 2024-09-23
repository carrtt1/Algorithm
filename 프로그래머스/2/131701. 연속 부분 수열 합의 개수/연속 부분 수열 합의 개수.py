def solution(elements):
    result = []
    arr = elements * 2

    for i in range(1, len(elements)) :
        for j in range(1, len(arr)) :
            result.append(sum(arr[j:j+i]))
    
    return len(list(set(result)))+1