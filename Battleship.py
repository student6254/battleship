from random import random, randint
import string
 
hit_board = []
enemy_board = []
player_board = []
for i in range(10):
    hit_board.append(["0"] * 10)
    enemy_board.append(["0"] * 10)
    player_board.append(["0"] * 10)
 
def print_board(board, title):
    print(title)
    print("    A B C D E F G H I J")
    n = 1
    for row in board:
        if n == 10:
            print(str(n) + " |" + " ".join(row))
        else:
            print(str(n) + "  |" + " ".join(row))
        n += 1
print_board(hit_board, "Hit Board")
 
class Ship:
    def __init__(self, name, size, player):
        self.length = size
        self.name = name
        self.positions = []
        self.direction = (int)(random() * 2) * 90
        self.damage = 0
       
        if player == 2:
            row = 0
            col = 0
            not_valid_position = True
            while not_valid_position:
                not_valid_position = False
                #choose a random position
                #horizontal
                if self.direction == 0:
                    row = randint(0, (len(hit_board) - 1))
                    col = randint(0, (len(hit_board[0]) - 1) - self.length)
                    for i in range(self.length):
                        if enemy_board[row][col + i] == "1":
                            not_valid_position = True
                            break
                #vertical
                elif self.direction == 90:
                    row = randint(0, (len(hit_board) - 1) - self.length)
                    col = randint(0, (len(hit_board[0]) - 1))
                    for i in range(self.length):
                        if enemy_board[row + i][col] == "1":
                            not_valid_position = True
                            break
            if self.direction == 0:
                for i in range(self.length):
                    enemy_board[row][col + i] = "1"
                    self.positions.append((row, col + i))
            elif self.direction == 90:
                for i in range(self.length):
                    enemy_board[row +i][col] = "1"
                    self.positions.append((row + i, col))
                   
        elif player == 1:
            not_valid_position = True
            while not_valid_position:
                not_valid_position = False
               
                row = -1
                while row < 1 or row > 10:
                    row = input("Enter row: ")
                    if not row.isdigit():
                        print("Enter a number")
                        row = -1
                    else :
                        row = int(row)
                col = " "
                while (ord(col) < 65 or ord(col) > 74) and (ord(col) < 97 or ord(col) > 106):
                    col = input("Enter column: ")
                    if not col.isalpha():
                        print("Enter a letter")
                        col = " "
                       
                if ord(col) > 64 and ord(col) < 75:
                    col = ord(col) - 64
                elif ord(col) > 96 and ord(col) < 107:
                    col = ord(col) - 96
                col -= 1
                row -= 1
               
                direction = -1
                while direction != 0 and direction != 90:
                    direction = input("Enter direction degree (0 for right, 90 for down): ")
                    if not direction.isdigit():
                        print("Enter a number")
                        direction = -1
                    else :
                        direction = int(direction)
                self.direction = direction
               
               
                #horizontal
                if self.direction == 0:
                    if col + self.length > 9:
                        not_valid_position = True
                        print("Out of bounds")
                        break
                    for i in range(self.length):
                        if player_board[row][col + i] == "1":
                            not_valid_position = True
                            print("There is already a ship there.")
                            break
                #vertical
                elif self.direction == 90:
                    if row + self.length > 9:
                        not_valid_position = True
                        print("Out of bounds")
                        break
                    for i in range(self.length):
                        if player_board[row + i][col] == "1":
                            not_valid_position = True
                            print("There is already a ship there.")
                            break
            if self.direction == 0 and not_valid_position == False:
                for i in range(self.length):
                    player_board[row][col + i] = "1"
                    self.positions.append((row, col + i))
            elif self.direction == 90 and not_valid_position == False:
                for i in range(self.length):
                    player_board[row +i][col] = "1"
                    self.positions.append((row + i, col))
 
ships = []
ships.append(Ship("destroyer", 2, 2))
ships.append(Ship("submarine", 3, 2))
ships.append(Ship("cruiser", 3, 2))
ships.append(Ship("battleship", 4, 2))
ships.append(Ship("carrier", 5, 2))
#print_board(enemy_board, "Enemy Board")
 
player_ships = []
player_ships.append(Ship("destroyer", 2, 1))
 
def main():
    player = 1
    columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    while (len(ships) != 0 and len(player_ships) != 0):
        print_board(hit_board, "hit board")
        if player == 1:
            print("Your turn")
            valid_position = False
            while not valid_position:
                guess_row = -1
                while guess_row < 1 or guess_row > 10:
                    guess_row = input("Enter row: ")
                    if not guess_row.isdigit():
                        print("Enter a number")
                        guess_row = -1
                    else :
                        guess_row = int(guess_row)
                guess_col = " "
                while (ord(guess_col) < 65 or ord(guess_col) > 74) and (ord(guess_col) < 97 or ord(guess_col) > 106):
                    guess_col = input("Enter column: ")
                    if not guess_col.isalpha():
                        print("Enter a letter")
                        guess_col = " "
                       
                if guess_row < 1 or guess_row > 10 or ((ord(guess_col) < 65 or ord(guess_col) > 74) and (ord(guess_col) < 97 or ord(guess_col) > 106)):
                    print("Invalid input")
                    continue
                if ord(guess_col) > 64 and ord(guess_col) < 75:
                    guess_col = ord(guess_col) - 64
                elif ord(guess_col) > 96 and ord(guess_col) < 107:
                    guess_col = ord(guess_col) - 96
                guess_col -= 1
                guess_row -= 1
               
                if hit_board[guess_row][guess_col] != "0":
                    print("You already tried that position.")
                    valid_position = False
                else:
                    valid_position = True
                    hit = False
                    for ship in ships:
                        for position in ship.positions:
                            if position[0] == guess_row and position[1] == guess_col:
                                hit = True
                                ship.damage += 1
                                if ship.damage == ship.length:
                                    print("You sunk the " + ship.name)
                                    ships.remove(ship)
                                hit_board[guess_row][guess_col] = "X"
                                break
                        if hit == True:
                            break
                    if hit == False:
                        hit_board[guess_row][guess_col] = "Y"
            player = 2
        elif player == 2:
            print("Computer's turn")
            valid_position = False
            while(not valid_position):
                guess_row = randint(0, 9)
                guess_col = randint(0, 9)
                #random.choice(string.letters)
               
                if player_board[guess_row][guess_col] != "0":
                    valid_position = False
                else:
                    valid_position = True
                    hit = False
                    for ship in player_ships:
                        for position in ship.positions:
                            if position[0] == guess_row and position[1] == guess_col:
                                hit = True
                                ship.damage += 1
                                if ship.damage == ship.length:
                                    print("You sunk the " + ship.name)
                                    ships.remove(ship)
                                player_board[guess_row][guess_col] = "X"
                                break
                        if hit == True:
                            break
                    if hit == False:
                        player_board[guess_row][guess_col] = "Y"
           
            print("Computer fires at " + str(guess_row+1) + ", " + columns[guess_col])
            print_board(player_board, "Your board")
            player = 1
    print("You win!")
main()