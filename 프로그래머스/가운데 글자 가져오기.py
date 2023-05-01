def solution(s):
    cnt=len(s)%2
    idx=len(s)//2
    if(cnt==0):
        return s[idx-1:idx+1]        
    else:
        return s[idx]        
