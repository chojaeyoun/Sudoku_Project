def print_board(board):
    for row in board:
        print(" ".join(map(str, row)), end="\n")    
        ## map(str, row) row에 있는 숫자를 문자열로 변경   
        ## ",".join() 문자열을 이어 붙여서 출력
board = initialize_board()
print_board(board)