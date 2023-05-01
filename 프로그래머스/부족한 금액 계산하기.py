def solution(price, money, count):
    if count>1:
        result=price*((1+count)*count/2)
        return result-money if(result-money>0) else 0
    else:
        return price-money if(price-money>0) else 0