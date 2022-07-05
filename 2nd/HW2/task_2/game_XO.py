import random
from typing import List, Tuple

"""
Game board is chosen as list of numbers for every cell.

For columns will be used remainder of 10 for chosen position.

For rows will be used integer division of chosen position by 10.
"""

PLAY_BOARD = [str(num) for num in range(1, 101)]
PLAYERS_MARKS = ["X", "O"]
player = ""
computer = ""
current_player = ""
last_position = random.choice(range(0, 99))


def display_board(board: List):
    """
    Generate game board.

    :param board: list of numbers of every cell
    """
    for i in range(100):
        if i < 9:
            print(board[i], end="  | ")
        else:
            print(board[i], end=" | ")
        if i % 10 == 9:
            print('')
            print('-- | ' * 10)


def players_input():
    """Assigns marks for computer and player."""
    global player
    global computer
    while player not in PLAYERS_MARKS:
        player = input("Choose your marker X or O ---> ").upper()
    if player == "X":
        computer = "O"
    else:
        computer = "X"


def switch_player(mark: str) -> str:
    """
    Switch player.
    :param mark: current mark after previous move
    :return: next mark
    """
    if mark == "X":
        return "O"
    return "X"


def place_marker(board: List, marker: str, position: int):
    """
    Place marker at chosen position.
    :param board: game board
    :param marker: X or O
    :param position: cell of the board
    """
    if position <= 9:
        board[position] = marker
    else:
        board[position] = " " + marker


def space_check(board, position) -> bool:
    """Returns boolean value whether the cell is free or not."""
    return board[position].strip() not in PLAYERS_MARKS  # strip is needed because we have string with space +
    # player_mark


def check_loose_condition(line: str) -> bool:
    """
    Check is input line contains XXXXX or OOOOO.
    :param line: line after last move
    :return: True if last move led to loss
    """
    answer = False
    if ("XXXXX" in line) or ("OOOOO" in line):
        answer = True
    return answer


def loosing_game_check(board: List, position: int) -> bool:
    """
    Checking condition for losing.
    :param board: game board
    :param position: chosen position
    :return: True if position lead to losing game,else - False
    """
    return check_diagonals(board, position) or \
           check_vertical(board, position) or \
           check_horizontal(board, position)


def draw_check(board: List) -> bool:
    """
    Returns bool value whether the game board is full of game marks.
    :param board: game board
    :return: bool
    """
    return len(set(board)) == 2


def winning(board: List, position: int, player_mark: str) -> bool | None:
    """
    Checking who wins the game.
    :param board: game board
    :param position: curr position
    :param player_mark: mark of current player
    :return: True if game is won by computer, else False
    """
    if loosing_game_check(board, position) and player_mark == player:
        return True

    if draw_check(board):
        return None

    return False


def get_interval_for_check(position: int) -> Tuple:
    """
    Position is position in a row or position in a column.
    Main idea - take interval [position - 4, position + 4], check boundaries and return it.
    :param position: number of row or column
    :return: interval for checking
    """
    interval_begin = 0
    interval_end = 9
    if (position - 4) >= 0:  # for columns and rows we have one rule: values of them are in range of [0, 9]
        interval_begin = position - 4

    if (position + 4) <= 9:
        interval_end = position + 4

    return interval_begin, interval_end


def check_diagonals(board: List, position: int) -> bool:
    """
    Checking diagonals and reversed diagonals for loosing.
    :param board: game board
    :param position: chosen position
    :return: True if position leads to losing game, else - False
    """
    columns, rows = position % 10, position // 10
    diag = diag_reversed = ""
    column_start, column_end = get_interval_for_check(columns)
    row_start, row_end = get_interval_for_check(rows)
    # diag is from [column_start + 10*row_start, column_end + 10*row_end]
    # diag_reversed is from [column_start + 10*row_end, column_end + 10*row_start]
    count = 0
    while ((column_start + count) <= column_end) and \
            ((row_start + count) <= row_end) and \
            ((row_end - count) >= row_start):
        diag += board[(column_start + count) + 10 * (row_start + count)].strip()
        diag_reversed += board[(column_start + count) + 10 * (row_end - count)].strip()  # we have a lot of spaces
        count += 1

    return check_loose_condition(diag) or check_loose_condition(diag_reversed)


def check_vertical(board: List, position: int) -> bool:
    """
    Checking vertical line for loosing.
    :param board: game board
    :param position: chosen position
    :return: True if position leads to losing game, else - False
    """
    row_start, row_end = get_interval_for_check(position // 10)
    vertical = ""
    count = 0
    while (row_start + count) <= row_end:
        vertical += board[position % 10 + 10 * (row_start + count)].strip()
        count += 1

    return check_loose_condition(vertical)


def check_horizontal(board: List, position: int) -> bool:
    """
    Checking horizontal line for loosing.
    :param board: game board
    :param position: chosen position
    :return: True if position leads to losing game, else - False
    """
    col_start, col_end = get_interval_for_check(position % 10)
    row = position // 10
    horizontal = ""
    count = 0
    while (col_start + count) <= col_end:
        horizontal += board[col_start + count + 10 * row].strip()
        count += 1

    return check_loose_condition(horizontal)


def get_interval_for_computer(position: int, num_of_steps: int):
    """
    Calculate range of steps for computer.
    :param position: rows or columns pos
    :param num_of_steps: depth of steps
    :return: start_point, end_point
    """
    if position >= 9 - num_of_steps:  # + 1?
        start, end = 9 - num_of_steps * 2, 9
    elif position <= num_of_steps:
        start, end = 0, num_of_steps * 2
    else:
        start, end = position - num_of_steps, position + num_of_steps

    return start, end


def minimax(board: List, comp_move: bool, position: int, curr_depth: int):
    game_res = winning(board, position, current_player)
    if game_res == True:
        return 10
    elif game_res == False:
        return -10
    elif game_res == None or curr_depth > 2:
        return 0

    columns, rows = position % 10, position // 10
    columns_start, columns_end = get_interval_for_computer(columns, 1)
    rows_start, rows_end = get_interval_for_computer(rows, 1)
    if comp_move:
        best_score = 1000000
        for x in range(columns_start, columns_end + 1):
            for y in range(rows_start, rows_end + 1):
                curr_pos = x + 10 * y
                if not (board[curr_pos] in PLAYERS_MARKS):
                    tmp_value = board[curr_pos]
                    board[curr_pos] = player
                    score = minimax(board, False, curr_pos, curr_depth + 1)
                    board[curr_pos] = tmp_value
                    best_score = min(score, best_score)
    else:
        best_score = -1000000
        for curr_pos in range(len(board)):
            if not (board[curr_pos] in PLAYERS_MARKS):
                tmp_value = board[curr_pos]
                board[curr_pos] = computer
                score = minimax(board, True, curr_pos, curr_depth + 1)
                board[curr_pos] = tmp_value
                best_score = max(score, best_score)
    return best_score


def comp_move() -> int:
    """
    Computer AI move.
    Based on: https://tproger.ru/translations/tic-tac-toe-minimax/
    """
    new_board = PLAY_BOARD.copy()  # to use in minimax
    best_score = -1000000
    moves = []
    columns, rows = last_position % 10, last_position // 10
    columns_start, columns_end = get_interval_for_computer(columns, 2)
    rows_start, rows_end = get_interval_for_computer(rows, 2)

    # checking all positions from left to right
    for x in range(columns_start, columns_end + 1):
        for y in range(rows_start, rows_end + 1):
            curr_pos = x + 10 * y
            if PLAY_BOARD[curr_pos].strip() not in PLAYERS_MARKS:  # check if curr_pos is available, strip is needed
                # because we have string with space + player_mark
                tmp_value = new_board[curr_pos]
                new_board[curr_pos] = computer
                score = minimax(new_board, True, curr_pos, 0)
                new_board[curr_pos] = tmp_value
                if score >= best_score:
                    best_score = score
                    moves.clear()  # will keep only 1 move
                    moves.append(curr_pos)
    return moves[0]


def choose_first() -> str:
    """Randomly returns the player's mark that goes first."""
    return PLAYERS_MARKS[random.choice((0, 1))]


def player_choice(board: List, player_mark: str) -> int:
    """
    Gets player's next position and check if it's appropriate to play.
    :param board: game board
    :param player_mark: player mark
    :return: bool
    """
    position = 0

    while position not in [num for num in range(1, 101)]:
        try:
            position = \
                int(input(f'Player "{player_mark}", choose your next position from 1 to 100: '))
            position -= 1
            if space_check(board, position):
                return position
            else:
                print(f'Position is busy. Please, try another position from 1 to 100.')
                position = 0
                continue
        except ValueError as exc:
            print(f'Wrong value: {exc}. Please, try again.')

    # position -= 1
    # if space_check(board, position):
    #     return position
    #
    # return False


def replay() -> bool:
    """Asks the players to play again."""
    decision = ''
    while decision not in ('y', 'n'):
        decision = input('Would you like to play again? Type "y" or "n"').lower()

    return decision == 'y'


def clear_screen():
    """Clears the game screen via adding new rows."""
    print('\n' * 100)


def main():
    global player, computer, PLAY_BOARD, PLAYERS_MARKS, current_player, last_position
    """Play game."""
    print('Welcome to Tic Tac Toe!')
    players_input()
    current_player = choose_first()
    print(f'Player with mark "{current_player}" goes first.')

    game = False

    while not game:
        display_board(PLAY_BOARD)
        print(f'Last position was {last_position + 1}')

        print(f'Turn of the player with the mark "{current_player}":')

        if current_player == computer:
            pos_to_place = comp_move()
            # if space_check(PLAY_BOARD, pos_to_place):
            place_marker(PLAY_BOARD, current_player, pos_to_place)
            # else:
            #     continue
        else:
            pos_to_place = player_choice(PLAY_BOARD, current_player)
            # if space_check(PLAY_BOARD, pos_to_place):
            place_marker(PLAY_BOARD, current_player, pos_to_place)
            # else:
            #     continue
        last_position = pos_to_place

        if winning(PLAY_BOARD, last_position, current_player):
            display_board(PLAY_BOARD)
            print(f'Player "{current_player}" has lost the game')
            game = True

            if not replay():
                break
            else:
                PLAY_BOARD = [str(num) for num in range(1, 101)]
                players_input()
                current_player = choose_first()
        else:
            current_player = switch_player(current_player)
        # clear_screen()


if __name__ == '__main__':
    main()
