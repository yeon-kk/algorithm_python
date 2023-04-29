cnt=0
def dfs(idx,num,sum,number):
    global cnt
    if(num==3 and sum==0):
        cnt+=1
        return
    for i in range(idx,len(number)):
        dfs(i+1,num+1,sum+number[i],number)

def solution(number):
    global cnt
    dfs(0,0,0,number)
    return cnt