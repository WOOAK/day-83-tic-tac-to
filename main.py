holder = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
board = """
_____________
|Tic|Tac|Toe|
_____________
|Tic|Tac|Toe|
_____________
|Tic|Tac|Toe|
_____________
"""

print(board)
# winning possibility:
# 0,1,2
# 3,4,5
# 6,7,8
# 0,3,6
# 1,4,7
# 2,5,8
# 0,4,8
# 2,4,6

# 0: (1,2),(3,6),(4,8)
# 1: (0,2),(4,7)
# 2: (0,1),(5,8),(4,6)
# 3: (4,5),(0,6)
# 4: (3,5),(1,7),(0,8),(2,6)
# 5: (3,4),(2,8)
# 6: (7,8),(0,3),(2,4)
# 7: (6,8),(1,4)
# 8: (6,7),(2,5),(0,4)


winning_combination = {
    0:[(1,2),(3,6),(4,8)],
    1:[(0,2),(4,7)],
    2:[(0,1),(5,8),(4,6)],
    3:[(4,5),(0,6)],
    4:[(3,5),(1,7),(0,8),(2,6)],
    5:[(3,4),(2,8)],
    6:[(7,8),(0,3),(2,4)],
    7:[(6,8),(1,4)],
    8:[(6,7),(2,5),(0,4)]
}

# print(winning_combination[0][0][1])
def checkBoard(player,location):
    winned = False
    list_of_winning = winning_combination[location]
    for position in list_of_winning:
        if holder[position[0]] == player and holder[position[1]] == player:
            winned = True
            return  winned


def firstPlayer():
    locationX = int(input("First player's turn (X): Please input your location (1 to 9 unoccupied cell)"))
    if holder[locationX - 1] == ' ':
        holder[locationX - 1] = 'X'
        return locationX - 1
    else:
        print("The cell is occupied. Please choose another")
        return firstPlayer()

def secondPlayer():
    locationO = int(input("Second player's turn (O): Please input your location (1 to 9 unoccupied cell)"))
    if holder[locationO - 1] == ' ':
        holder[locationO - 1] = 'O'
        return locationO - 1
    else:
        print("The cell is occupied. Please choose another")
        return secondPlayer()

def displayBoard():
    board = f"""
    _____________
    | {holder[0]} | {holder[1]} | {holder[2]} |
    _____________
    | {holder[3]} | {holder[4]} | {holder[5]} |
    _____________
    | {holder[6]} | {holder[7]} | {holder[8]} |
    _____________
    """
    print(board)

end_game = False
turns = 0
while end_game == False:
    location = firstPlayer()
    player = 'X'
    player1_win = checkBoard(player,location)
    displayBoard()
    turns += 1
    if player1_win:
        print("First player win")
        end_game=True
        break
    if turns == 9:
        print("The game is a tie")
        end_game=True
        break
    location = secondPlayer()
    player = 'O'
    player2_win = checkBoard(player, location)
    displayBoard()
    turns += 1
    if player2_win:
        print("Second player win")
        end_game= True
        break








