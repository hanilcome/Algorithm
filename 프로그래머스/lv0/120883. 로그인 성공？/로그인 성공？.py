def solution(id_pw, db):
    answer = ''

    for a in db:
        if id_pw[0] == a[0]:
            if id_pw[1] == a[1]:
                answer = "login"
                break
            else:
                answer = "wrong pw"
                break
        else:
            answer = "fail"
        
    return answer