def solution(s):
    answer = True
    len_s = len(s)
    
    if len_s == 4 or len_s == 6:
        try:
            int(s)
        except ValueError:
            answer = False
    else:
        answer = False       
    return answer