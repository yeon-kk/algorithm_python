def solution(t, p):
    answer = 0
    p_len=len(p)
    end_index=len(t)-len(p)
    for i in range(end_index+1):
        result=True
        for j in range(p_len):
            t_num=int(''.join(t[i:i+j+1]))
            p_num=int(''.join(p[0:0+j+1]))
            if(t_num > p_num):
                result=False
                break
        if(result):
            answer+=1
    return answer