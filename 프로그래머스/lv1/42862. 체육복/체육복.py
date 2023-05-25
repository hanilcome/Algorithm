def solution(n, lost, reserve):
        answer = 0
        std = {i: 1 for i in range(1, n+1)}
        
        
        for i in lost:
                std[i] = 0
        
        reserve.sort()
        for a in range(len(reserve)):
                for r in reserve:
                        if std[r] == 0:
                                std[r] = 1
                                reserve.remove(r)
        
        for a in range(len(reserve)):
                for r in reserve:
                        print(r, reserve)
                        try:     
                                if r == 1:
                                        if std[r+1] == 0:
                                                std[r+1] = 1
                                                reserve.remove(r)
                                                print(r, reserve)
                                                break
                                elif r == n:
                                        if std[r-1] == 0:
                                                std[r-1] = 1
                                                reserve.remove(r)
                                                print(r, reserve)
                                                break
                                else:
                                        if std[r-1] == 0:
                                                std[r-1] = 1
                                                reserve.remove(r)
                                                print(r, reserve)
                                                break
                                        elif std[r+1] == 0:
                                                std[r+1] = 1
                                                reserve.remove(r)
                                                print(r, reserve)
                                                break
                        except KeyError:
                                pass

        for a in std:
                if std[a]==1:
                        answer += 1
        return answer