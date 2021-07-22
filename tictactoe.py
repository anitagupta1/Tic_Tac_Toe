import random
#board = [' ' for x in range(10)]

def insertLetter(l,pos):
    board[pos] = l

def space_free(pos):
    return board[pos] == ' '

def print_board(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')

def Board_full(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def is_winner(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))

def playerMove():
    run = True
    while run:
        try:
            move = int(input("please select a position to enter the X between 1 to 9 : "))
            if move > 0 and move < 10:
                if space_free(move):
                    run = False
                    insertLetter('X' , move)
                else:
                    print('Sorry, this space is occupied')
            else:
                print('please type a number between 1 and 9')

        except:                                                # if u didnt enter no then it goes into except
            print('Please type a number')

def computerMove():
    possibleMoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0  ]
    for let in ['O' , 'X']:                                     #if we didn't select that pos(move) then another person win
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if is_winner(boardcopy, let):
                move = i
                return move

    corners_open = []
    for i in possibleMoves:
        if i in [1 , 3 , 7 , 9]:
            corners_open.append(i)

    if len(corners_open) > 0:
        move = selectRandom(corners_open)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

    return 0

def selectRandom(li):
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def main():
    print("Welcome to the game!")
    print_board(board)

    while not(Board_full(board)):
        if not(is_winner(board , 'O')):
            playerMove()
            print_board(board)
        else:
            print("********************** Sorry You Loose! **********************")
            break

        if not(is_winner(board , 'X')):
            move = computerMove()
            if move!=0:
             insertLetter('O' , move)
             print('computer placed an o on position' , move , ':')
             print_board(board)
        else:
            print("*********************** You Win! ***************************")
            break

        if Board_full(board):
            print("*********************** Game Tie! ***************************")

while 1:
  board = [' ' for x in range(10)]
  print('--------------------')
  main()
  x = input("Do you want to play again? (y/n)")
  if x!='y':
      print('******************** GAME ENDED *********************')
      break


