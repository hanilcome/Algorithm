def solution(n, m):
    # 유클리드 호제법으로 풀거나 모듈 사용해서 해보자
    answer = []
    nlist = [n, m]
    nlist.sort()
    num = 0
    answer_set = []
    answer_list = []
    
    while num < 2:
        for a in range(1, nlist[num]+1):
            if nlist[num] % a == 0:
                answer.append(a)
        num += 1
    answer.sort()
    
    for a in answer:
        if answer.count(a) > 1 and a != 1:
            answer_set.append(a)
    answer = list(set(answer_set))
    
    answer.sort(reverse=True)
    
    num = 0
    if answer:
        while num < len(answer):
            for t, a in enumerate(nlist):
                if a % answer[0] == 0:
                    nlist[t] = a // answer[0]
            num += 1       
            if nlist[0] == 1:
                break 
        answer_list += answer
    else:
        answer_list.append(1)
    
    if answer:
        answer_list.append(answer[0]*nlist[0]*nlist[1])
    else:
        answer_list.append(nlist[0]*nlist[1])
    
    return [answer_list[0], answer_list[len(answer_list)-1]]