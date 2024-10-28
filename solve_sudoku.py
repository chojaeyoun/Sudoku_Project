def is_valid(board, row, col, num): # 3가지 규칙 체크 함수
    # 해당 숫자가 같은 행에 있는지 확인
    # 1. 행 중복 숫자가 있는지
    if num in board[row]:
        return False
    # 2. 열 중복 숫자가 있는지
    if num in [board[i][col] for i in range(9)]:
        return False
    # 3. 3 X 3 박스에 중복 숫자가 있는지
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False
    return True   

def find_empty_location(board): # 빈 값을 찾는 함수
    # 비어있는 위치를 찾음
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None
            

def solve_sudoku(board):

    empty_loc = find_empty_location(board)

    if not empty_loc:
        return True # 다풀었다.
    
    # 빈 위치가 있으면,
    row, col = empty_loc

    for num in range(1, 10):
        # 3가지 규칙이 맞을 때,
        if is_valid(board, row, col, num):
            board[row][col] = num

            # 재귀(Recursive) 함수#
            if solve_sudoku(board):
                return True
            
            board[row][col] = 0  # 풀 수 없는 스도쿠가 입력으로 들어오지 못하게
            #####################
    return False


print("초기 스도쿠 퍼즐:")
print_board(board)
print("\n해결된 스도쿠 퍼즐:")

if solve_sudoku(board):
    print_board(board)
else:
    print("해결할 수 없는 스도쿠 퍼즐입니다.")