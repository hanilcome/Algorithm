def solution(quiz):
    answer = []
    for s in range(len(quiz)):
        print(quiz[s])
        test = quiz[s].split(" ")
        print(test)
        
        if test[1]=="-":
            print(int(test[0])-int(test[2]) == int(test[4]))
            if (int(test[0])-int(test[2]) == int(test[4])):
                answer.append("O")
            else:
                answer.append("X")
        elif test[1]=="+":
            print(int(test[0])+int(test[2]) == int(test[4]))
            if (int(test[0])+int(test[2]) == int(test[4])):
                answer.append("O")
            else:
                answer.append("X")
    
    
    return answer