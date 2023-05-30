def solution(a, b):
        sum = 0
        temp = 0
        if a > b:
                a, b = b, a
        for s in range(a, b+1):
                sum += s
        return sum