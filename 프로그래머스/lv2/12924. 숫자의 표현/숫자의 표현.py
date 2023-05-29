def solution(n):
        list = []
        sum=0
        num=0
        
        for a in range(1,n+1):
                list.append(a)

        while num<n:
                answer=0
                for a in list:
                        answer += a
                        if answer == n:
                                sum += 1
                                list.remove(list[0])
                                num += 1
                                break
                        elif answer > n:
                                list.remove(list[0]) 
                                num += 1
                                break 
                                        
        return sum