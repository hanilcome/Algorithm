def solution(s):
    slist = []
    for a in s:
        slist.append(a)

    answer = 1
    same = 0
    another = 0

    for a, n in enumerate(slist):
        if same == 0:
            same += 1
        elif same != another:
            if slist[0] == n:
                same += 1
            elif slist[0] != n:
                another += 1
        else:   
            answer += 1
            same = 1
            another = 0
            slist[0] = n
            
    return answer