def solution(num, total):
    answer = []
    div_total = total/num

    if total%num != 0:
        for a in range(num):
            start = int(div_total) - int(num/2) + 1 + a
            answer.append(start)
    else:
        for a in range(num):
            start = int(div_total) - int(num/2) + a
            answer.append(start)
    return answer