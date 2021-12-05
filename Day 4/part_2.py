# Parse puzzle_input.txt
with open("puzzle_input.txt") as file:
    text = file.readlines()
    # Generate list of numbers
    numbers = [int(n) for n in text[0].strip().split(",")]
    # Generate bingo boards
    boards = []
    temp = []
    count = 0
    # Create each row/column and add a 0 value to sum the matches in each row/column
    for line in text[2:]:
        if count < 5:
            row = line.strip().split()
            row_nums = [int(n) for n in row]
            row_nums.append(0)
            temp.append(row_nums)
            count += 1
        else:
            count = 0
            temp += [[0,0,0,0,0,0]]
            boards.append(temp)
            temp = []

# Loops through each board, and returns the last called number and a winning board when a column or row equals 5
def get_winning_board():
     for number in numbers:
        for board in boards:
            for j, row in enumerate(board[0:5]):
                for i, cell in enumerate(row[0:5]):
                    if number == cell:
                        board[j][i] = "x"
                        row[5] += 1
                        board[5][i] += 1
                    if row[5] == 5:
                        return number, board
                    if board[5][i] == 5:
                        return number, board

# Gets last number and winning board and multiples the last called number with the sum of uncalled numbers for that board
def calculate():
    # While boards length is greater than 1, keep calling get_winning_board and remove it from the list of boards until there is one board left
    while len(boards) > 1:
        winning_board = get_winning_board()
        boards.remove(winning_board[1])
    winning_board = get_winning_board()
    last_called = winning_board[0]
    board = winning_board[1]
    unmarked = 0
    for b in board[0:5]:
        for r in b[0:5]:
            if r != "x":
                unmarked += int(r)

    score = unmarked * last_called
    print(score) #7075

calculate()