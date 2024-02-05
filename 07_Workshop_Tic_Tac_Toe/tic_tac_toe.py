import speech_recognition as sr

from collections import deque
from pyfiglet import Figlet


def get_name(player_number):
    while True:
        with sr.Microphone() as source:
            r = sr.Recognizer()
            print(f"Player {player_number} please say your name: ")

            audio = r.record(source, duration=3)
            print("Recognizing...")

            try:
                return r.recognize_google(audio)
            except sr.exceptions.UnknownValueError:
                print("Please say your name again!")


def check_for_win():
    player_name, player_symbol = players[0].values()

    first_diagonal_win = all([board[i][i] == player_symbol for i in range(SIZE)])
    second_diagonal_win = all([board[i][SIZE - i - 1] == player_symbol for i in range(SIZE)])

    row_win = any([all([el == player_symbol for el in row]) for row in board])
    col_win = any([all([board[r][c] == player_symbol for r in range(SIZE)]) for c in range(SIZE)])

    if any([first_diagonal_win, second_diagonal_win, row_win, col_win]):
        print_board()
        print(f"{player_name} won!")

        raise SystemExit


def place_symbol(row, col):
    board[row][col] = players[0]["symbol"]

    check_for_win()
    print_board()

    if turns == SIZE * SIZE:
        print("Draw!")
        raise SystemExit

    players.rotate()


def choose_position():
    global turns

    while True:
        try:
            position = int(input(f"{players[0]['name']} choose a free position [1-{SIZE * SIZE}]: "))
            row, col = (position - 1) // SIZE, (position - 1) % SIZE
        except ValueError:
            print_select_a_valid_position_message()
            continue

        if 1 <= position <= SIZE * SIZE and board[row][col] == " ":
            turns += 1
            place_symbol(row, col)
        else:
            print_select_a_valid_position_message()


def print_select_a_valid_position_message():
    print(f"{players[0]['name']}, please select a valid position!")


def print_board():
    [print(f"| {' | '.join(row)} |") for row in board]


def print_game_state():
    print("This is the numeration of the board: ")
    print_board()

    for row in range(SIZE):
        for col in range(SIZE):
            board[row][col] = " "



def start():

    f = Figlet(font='slant')
    print(f.renderText('Welcome to Tic Tac Toe'))

    player_one_name = get_name(1)
    player_two_name = get_name(2)

    while True:
        player_one_symbol = input(f"{player_one_name}, would you like to play with X or O?: ").upper()

        if player_one_symbol not in ["X", "O"]:
            print(f"{player_one_name}, please select a valid option!")
        else:
            break

    player_two_symbol = "O" if player_one_symbol == "X" else "X"

    players.append({"name": player_one_name, "symbol": player_one_symbol})
    players.append({"name": player_two_name, "symbol": player_two_symbol})

    print_game_state()
    choose_position()


SIZE = 3
turns = 0

board = [[str(r + c) for c in range(SIZE)] for r in range(1, SIZE * SIZE + 1, SIZE)]
players = deque()

start()

# for mac
# brew install portaudio
# brew install flac

# pip3 install pyaudio
# pip install SpeechRecognition pydub
# pip3 install pyfiglet
