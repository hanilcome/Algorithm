def solution(x):
        answer = True
        sum = 0
        nlist = list(str(x))
        for a in nlist:
                sum += int(a)
        if x % sum != 0:
                answer = False
        return answer