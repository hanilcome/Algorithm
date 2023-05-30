def solution(s):
        answer = ''
        print(s.split(" "))
        n=1
        for a in s.split(" "):
                for i, j in enumerate(a):
                        if i == 0 or i%2 == 0:
                                answer += j.upper()
                        else:
                                answer += j.lower()
                if n<len(s.split(" ")):
                        answer += " "
                        n += 1
                                
        return answer