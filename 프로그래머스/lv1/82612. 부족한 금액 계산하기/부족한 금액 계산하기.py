def solution(price, money, count):
    answer = -1
    sum_list = []
    
    for a in range(1,count+1):
        sum_list.append(price*a)
        
    return sum(a for a in sum_list) - money if sum(a for a in sum_list) > money else 0