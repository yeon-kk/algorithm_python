def solution(lottos, win_nums):
    lottos.sort()
    win_nums.sort()
    win_cnt=0
    zero_cnt=0
    for item in lottos:
        if item==0:
            zero_cnt+=1
            continue
        if item in win_nums:
            win_cnt+=1
    result = win_cnt+zero_cnt
    # 1등 : win 6, win_cnt+zero_cnt 6
    # 2등: win 5, win_cnt+zero_cnt 5
    # 6등: win 1,0, win_cnt+zero_cnt 1,0
    win_result=0
    lose_result=0
    if(result>1):
        win_result=7-result
    else:
        win_result=6
    if(win_cnt>1):
        lose_result=7-win_cnt
    else:
        lose_result=6

    answer =[win_result , lose_result]
    
    
    return answer
print(solution([44, 1, 0, 0, 31, 25],	[31, 10, 45, 1, 6, 19]))