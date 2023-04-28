def solution(s):
    answer = []
    s_list=list(s)
    s_set = set(s_list)
    s_dict = {}
    for item in s_set:
        s_dict[item]= -1
    for index, item in enumerate(s_list):
        if(s_dict[item]==-1):
            answer.append(s_dict[item])
        else:
            answer.append(index-s_dict[item])
        s_dict[item] = index
    return answer
