def solution(n, arr1, arr2):
        answer = []
        list1 = list(map(bin, arr1))
        list2 = list(map(bin, arr2))
        list3 = []
        list4 = []
        list5 = []
        list6 = ""
        
        
        for a, s in enumerate(list1):
                list3.append(list(s[2:])) 
                while len(list3[a]) != n:
                        if len(list(s[2:])) < n:
                                list3[a].insert(0,'0')
                
                
        for a,s in enumerate(list2):
                list4.append(list(s[2:]))
                while len(list4[a]) != n:
                        if len(list(s[2:])) < n:
                                list4[a].insert(0,'0')
                
                
        for a, s in enumerate(list3):
                # print(a, s, list4[a])
                for b, t in enumerate(s):
                        # print(b, t, list4[a][b])
                        if t == '1' or list4[a][b] == '1':
                                list5.append("#")
                        elif t == '0' and list4[a][b] == '0':
                                list5.append(" ")
        
        for a in list5:
                list6 += a
        
        return [list6[n*i:n*(i+1)] for i in range(n)]