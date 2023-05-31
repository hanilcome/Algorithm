def solution(array, commands):
    sort_num = []
    for a in commands:
        answer = []
        for i in range(a[0], a[1]+1):
            answer.append(array[i-1])
        answer.sort()
        sort_num += [answer[a[2]-1]]

    return sort_num