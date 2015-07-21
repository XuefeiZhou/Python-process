from random import randint

board = []
for x in range(5):
    board.append(["O"]*5)
def printboard(board):
    for x in board:
        print " ".join(x)

print "Let's play battleships!"
printboard(board)

def random_row(board):
    return randint(0, len(board) - 1)
    
def random_col(board):
    return randint(0, len(board) - 1)


ship1_row = random_row(board)
ship1_col = random_col(board)
ship2_row = random_row(board)
ship2_col = random_col(board)
while ship1_row == ship2_row and ship1_col == ship2_col:
    ship2_row = random_row(board)
    ship2_col = random_col(board)
            
print "%i %i %i %i" % (ship1_row,ship1_col,ship2_row,ship2_col)#to be delated
hit = 0
for x in range(0,4):
    print 'turn:', x + 1
    if hit != 2:
        guess_row = int(raw_input("Guess the row: "))
        guess_col = int(raw_input("Guess the col: "))
        if [guess_row,guess_col] == [ship1_row,ship1_col] or [guess_row,guess_col] == [ship2_row,ship2_col]:
            print "Congrats!"
            hit = hit + 1
            printboard(board)
        elif guess_row >= 5 or guess_col >= 5:
            print "out!"
            printboard(board)
        elif board[guess_row][guess_col] == "X":
            print "wtf?"
            printboard(board)
        else:
            board[guess_row][guess_col] = "X"
            print "wrong!"
            printboard(board)
    if hit == 2:
        print "You Won!"
        break
    if x == 3:
        print "Game over!"