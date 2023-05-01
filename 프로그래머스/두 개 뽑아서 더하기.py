def solution(numbers):
    answer = []
    length=len(numbers)
    for i in range(length):
        num1=numbers[i]
        for j in range(i+1,length):
            res=num1+numbers[j]
            if res not in answer:
                answer.append(res)
    answer.sort()
    return answer