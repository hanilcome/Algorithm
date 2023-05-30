def solution(bin1, bin2):
    answer = ''
    sum = 0
    n = 1
    share = 0
    if bin1 == '0' and bin2 == '0':
        answer += '0'
        
    if bin1 != '0' or bin2 != '0':
        for s in range(len(bin1)-1, -1,-1):
            sum += int(bin1[s])*n
            n = n*2

        n = 1   
        for s in range(len(bin2)-1, -1,-1):
            sum += int(bin2[s])*n
            n = n*2
            
            
        while(share != 1):
            share = sum // 2
            rest = sum % 2
            sum = share
            answer += str(rest)
            
        answer += str(share)
            
    
    return answer[::-1]