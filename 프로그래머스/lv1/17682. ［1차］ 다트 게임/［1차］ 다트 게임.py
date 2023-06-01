def solution(dartResult):
    dict = {'S': '*1', 'D':'*2', 'T':'*3'}
    sum_list = []
    number = ''
    idx = 0
    for a in dartResult:
        try:
            if int(a) or a == '0':
                number += a

        except ValueError:
            if a == '*':
                sum_list[idx-1] = sum_list[idx-1]*2
                
                if idx > 1:
                    sum_list[idx-2] = sum_list[idx-2]*2
            elif a == '#':  
                sum_list[idx-1] = sum_list[idx-1]*(-1)
            else:
                sum_list.append(eval(f'int(number)*{dict[a]}'))
                idx += 1
                number = ''
                
    return sum(a for a in sum_list)