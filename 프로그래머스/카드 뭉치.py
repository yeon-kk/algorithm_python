from collections import deque
def solution(cards1, cards2, goal):
    answer = 'Yes'
    deque_cards1 = deque(cards1)
    deque_cards2 = deque(cards2)
    idx=0
    while(deque_cards1 or deque_cards2):            
        if(idx == len(goal)):
            break;
        if(deque_cards1 and deque_cards1[0]==goal[idx]):
            deque_cards1.popleft()
            idx+=1
        elif(deque_cards2 and deque_cards2[0]==goal[idx]):
            deque_cards2.popleft()
            idx+=1
        else:
            answer = 'No'
            break;
    if(idx != len(goal)):
        answer='No'
    return answer
