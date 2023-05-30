def solution(n_list, n):
    n_ = []
    list_n = []
    a = 0
    num = 0

    while (a < len(n_list)//n):
        for i in range(1, n+1):
            n_.append(n_list[num])
            num += 1
        a += 1
        list_n.append(n_)
        n_ = []
    return list_n