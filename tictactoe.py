import os    
import time    
    
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']    
player = 1    
   
########win Flags##########    
win = 1    
draw = -1    
running = 0    
stop = 1    
###########################    
game = running    
mark = 'X'    
   

def draw_board():    
    'Målar spelbrädan'
    print(" %c | %c | %c " % (board[1],board[2],board[3]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[4],board[5],board[6]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[7],board[8],board[9]))    
    print("   |   |   ")    
   

def check_position(x):
    'Kollar ifall det redan är något i rutan '    
    if(board[x] == ' '):    
        return True    
    else:    
        return False    
   

def check_win():    
    'Kollar om någon vunnit'
    global game    
    #Horizontal winning condition    
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):    
        game = win    
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):    
        game = win    
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):    
        game = win    
    #Vertical winning Condition    
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):    
        game = win    
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):    
        game = win    
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):    
        game=win    
    #Diagonal winning Condition    
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):    
        game = win    
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):    
        game=win    
    #Match Tie or draw Condition    
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):    
        game=draw    
    else:            
        game=running    
    
 
while(game == running):    
    os.system('cls')    
    draw_board()    
    if(player % 2 != 0):    
        print("Player 1's chance")    
        mark = 'X'    
    else:    
        print("Player 2's chance")    
        mark = 'O'    
    choice = int(input("Enter the position between [1-9] where you want to mark : "))    
    if(check_position(choice)):    
        board[choice] = mark    
        player+=1    
        check_win()    
    
os.system('cls')    
draw_board()    
if(game==draw):    
    print("Oavgjort")    
elif(game==win):    
    player-=1    
    if(player%2!=0):    
        print("Du vann!")    
    else:    
        print("Du förlorade.")  