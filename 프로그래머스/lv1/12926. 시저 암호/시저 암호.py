def solution(s, n):
        low = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
        up = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
        answer=''
        
        
        for a, i in enumerate(s):
                if i in low:
                        if low.index(i)+n*2 > 50:
                                # print(low[n*2-2])
                                answer += low[(low.index(i)+n*2)-52]
                        else:
                                # print(low[low.index(i)+n*2])
                                answer += low[low.index(i)+n*2]
                if i in up:
                        if up.index(i)+n*2 > 50:
                                # print(low[n*2-2])
                                answer += up[(up.index(i)+n*2)-52]
                        else:
                                # print(low[low.index(i)+n*2])
                                answer += up[up.index(i)+n*2]
                if i == " ":
                        answer += " "
                                
        return answer