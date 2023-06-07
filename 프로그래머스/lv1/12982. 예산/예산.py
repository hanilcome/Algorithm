def solution(d, budget):
    answer = 0
    d.sort()
    
    for a in d:
        if a <= budget:
            budget -= a
            answer += 1
    return answer