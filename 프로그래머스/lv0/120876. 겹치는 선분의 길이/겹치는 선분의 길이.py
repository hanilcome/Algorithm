def solution(lines):
        answer = 0
        arr = []
        x, y, z = lines

        
        for a in lines:
                arr += a

        for i in range(min(arr), max(arr)+1):
                count = 0

                if x[0] <= i < x[1]:
                        count += 1
                if y[0] <= i < y[1]:
                        count += 1
                if z[0] <= i < z[1]:
                        count += 1

                if count >= 2:
                        answer += 1

        return answer