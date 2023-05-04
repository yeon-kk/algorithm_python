def solution(arr):
    answer = []
    for idx in range(1,len(arr),1):
        print(idx)
        if arr[idx-1]!=arr[idx]:
            answer.append(arr[idx])
    return answer