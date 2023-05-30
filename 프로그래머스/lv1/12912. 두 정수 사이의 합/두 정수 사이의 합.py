def solution(a, b):
        sum = 0
        temp = 0
        if a > b:
                temp = a
                a = b
                b = temp
        for s in range(a, b+1):
                sum += s
        return sum