def solution(n):
    answer = []
    
    while True:
        if n % 3 == 0:
            answer.append(n%3)
            n = n//3
        else:
            answer.append(n%3)
            n = n//3
        
        if  n//3 == 1 or n//3 == 2:
            answer.append(n%3)
            answer.append(n//3)
            n = n//3
            break
        elif n == 0:
            break
        
        
    answer.reverse()

    return sum(a*3**n for n, a in enumerate(answer))