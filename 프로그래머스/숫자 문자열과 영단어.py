def solution(s):
    s=list(s)
    answer = ''
    numbers={'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    find_num=''
    num=['0','1','2','3','4','5','6','7','8','9']
    while s:
        tmp_num = s.pop(0)
        if(tmp_num not in num):
            find_num += tmp_num
            if(numbers.get(find_num)):
                answer+=(str(numbers[find_num]))
                find_num=''
        else:
            answer+=tmp_num
    return int(answer)
