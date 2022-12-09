#! python

import os

class Board:
    def __init__(self, size = 3):
        self.size = size
        self.range1 = list(range(0, self.size ** 2))

    def view(self):
        os.system('cls') # чистит только терминал
        for i in range(self.size):
            print(' | '.join(self.cells[i * self.size: (i + 1) * self.size]))
            if i < self.size -1:
                print('-+-'.join(['-'] * self.size))

    def reset(self):
        self.cells = [" "] * self.size ** 2

    def update(self, cell_num, player):
        if cell_num not in self.range1:
            print('Not in range')
            return True
        elif self.cells[cell_num] == " ":
            self.cells[cell_num] = player
            mistake = False
            return mistake
        else:
            print('Already taken')
            return True

    def is_winner(self, player):
        # check lines
        for i in range(self.size):
            winner = True
            for j in range(self.size):
                if self.cells[i * self.size + j] != player:
                    winner = False
            if winner:
                return winner
        # check columns
        for i in range(self.size):
            winner = True
            for j in range(self.size):
                if self.cells[j * self.size + i] != player:
                    winner = False
            if winner:
                return winner
        # check diagonal
        winner = True
        for i in range(self.size):
            if self.cells[i * self.size + i] != player:
                winner = False
        if winner:
            return winner
        winner = True
        for i in range(self.size):
            if self.cells[(i + 1)* self.size - i - 1] != player:
                winner = False
        if winner:
            return winner
        return False

    def is_tie(self):
        used_cells = 0
        for cell in self.cells:
            if cell != " ":
                used_cells += 1
            if used_cells == 9:
                return True
            else:
                return False



def start_game():
    print("XY game")

def refresh_shield():
    os.system("cls")
    start_game()
    board.view()

if __name__ == '__main__':
    size = int(input('Size of your board: '))
    board = Board(size = size)
    board.reset()
    os.system('cls')
    while True:
        refresh_shield()
        mistake = True
        while mistake == True:
            print('\nTime for player X, choose 0 -', size ** 2 -1)
            x = int(input())
            mistake = board.update(x, "X")
        refresh_shield()

        if board.is_winner("X"):
            print('\nPlayer X win! \n')
            play_again = input("Next round? (Y/N) >").upper()
            if play_again == "Y":
                board.reset()
                continue
            else:
                break

        if board.is_tie():
            print('\nTie game! \n')
            play_again = input("Next round? (Y/N) >").upper()
            if play_again == "Y":
                board.reset()
                continue
            else:
                break

        mistake = True
        while mistake == True:
            print('\nTime for player 0, choose 0 -', size ** 2 - 1)
            y = int(input())
            mistake = board.update(y, "0")

        if board.is_winner("0"):
            print('\nPlayer 0 win! \n')
            play_again = input("Next round? (Y/N) >").upper()
            if play_again == "Y":
                board.reset()
                continue
            else:
                break

        if board.is_tie():
            print('\nTie game! \n')
            play_again = input("Next round? (Y/N) >").upper()
            if play_again == "Y":
                board.reset()
                continue
            else:
                break