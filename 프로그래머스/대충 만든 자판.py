
key = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0,'N': 0, 'O': 0, 'P': 0, 'Q': 0,'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

def matching(keymap):
    global key
    for item in keymap:
        for index, x  in enumerate(item):
            if(key[x]==0):
                key[x]=index+1
            else:
                key[x] = min(key[x],index+1)

def finding(targets):
    global key
    answer =[]
    for item in targets:
        cnt=0
        for x in item:
            if(key[x]==0):
                cnt=-1
                break
            else:
                cnt+=key[x]
        answer.append(cnt)
    return answer

def solution(keymap, targets):
    matching(keymap)
    answer = finding(targets)
    return answer
