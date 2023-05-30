def solution(a, b):
        sum = 0
        if a > b:
                a, b = b, a
        for s in range(a, b+1):
            if a == b:
                sum = a
            else:
                sum += s
        return sum