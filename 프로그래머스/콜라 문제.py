def solution(a, b, n):
    answer = 0
    res=0
    while(n>=a):
        res += n % a #a로 나눠지지 못한 갯수가 나머지로.
        n = (n//a)*b #a로 나눠진 몫에 b를 곱한 것 만큼 받기
        answer += n
        print(n, res) # 2,2 
        if(n<a):
            if(n+res<a):
                break
            n+=res
            res=0
    return answer