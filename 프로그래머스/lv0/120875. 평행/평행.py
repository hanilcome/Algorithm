def solution(dots):
        x, y, z, r = dots
        answer = 0
        
        for a in range(3):
                if abs(x[0]-y[0])/abs(x[1]-y[1]) == abs(z[0]-r[0])/abs(z[1]-r[1]):
                        answer = 1
                        break
                if abs(x[0]-z[0])/abs(x[1]-z[1]) == abs(y[0]-r[0])/abs(y[1]-r[1]):
                        answer = 1
                        break
                if abs(x[0]-r[0])/abs(x[1]-r[1]) == abs(y[0]-z[0])/abs(y[1]-z[1]):
                        answer = 1
                        break
                
        return answer