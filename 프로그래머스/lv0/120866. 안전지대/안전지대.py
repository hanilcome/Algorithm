def solution(board):
    # 1을 먼저 찾는다.
    # 인접한곳을 2로 바꾼다.
    # 0의 개수를 센다.
    answer = len(board)*len(board)
    
    for x, row in enumerate(board):
        for y, length in enumerate(row):
            if board[x][y] == 1:
                answer -= 1
                for i in range(x-1, x+2):
                    for j in range(y-1, y+2):
                        if 0 <= i < len(board) and 0 <= j < len(board):
                            if board[i][j] != 1 and board[i][j] != 2:
                                board[i][j] = 2
                                answer -= 1  

                
    return answer