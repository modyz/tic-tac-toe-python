#any game works as follow capture the player input
#process the game state
#render the game board
import os
#declaring the global variables needed
game_board     = {0:'1',1:'2',2:'3',3:'4',4:'5',5:'6',6:'7',7:'8',8:'9'}
current_player = 0 #seting the player as the first player
Game_state = {'player_one'    : True  ,
              'draw'          : False ,
              'running'       : True  ,
              'invalid_input' : False ,
              'place_taken'   : False ,
              'player_won'    : 0     }



def draw():
    #this function is resposible to draw the game
    #first clear the screen and then draw the new board state
    clear_screen()
    print("-------------")
    print("| {pos1} | {pos2} | {pos3} |".format(pos1 = game_board[0] , pos2 = game_board[1] , pos3 = game_board[2]))
    print("-------------")
    print("| {pos4} | {pos5} | {pos6} |".format(pos4 = game_board[3] , pos5 = game_board[4] , pos6 = game_board[5]))
    print("-------------")
    print("| {pos7} | {pos8} | {pos9} |".format(pos7 = game_board[6] , pos8 = game_board[7] , pos9 = game_board[8]))
    print("-------------")
    print("\n")
    if Game_state['player_won'] == 1:
        print("player one won the game !!!! \n")
    elif Game_state['player_won'] == 2:
        print("player two has won the game !!!! \n")
    elif Game_state['draw']:
        print('Draw!!!')

def clear_screen():
    #this function is resposible for clearing the current screen and draw the latest state of the game
    os.system("cls")

def handle_input():
    #this function is responsibe for capturing the user input
    position = input("enter the desired position: ")
    validate_input(int(position))

def validate_input(position):
    #setting game board game state enum to global to make sure that we are affecting the global one
    global Game_state
    global game_board
    #this function is resposible for checking if the player's input is valid
    #not in a taken place 
    #inside the range of the positions
    #1:check if in range
    if 1 <= position <= 9:
        #2: check if the place is already taken
        if (game_board[position-1] == 'X' or game_board[position-1] == 'O'):
            Game_state['place_taken'] = True
        else:
            #we ran all the checks and everything is ok!! 
            process_game_board(position-1)
    else:
        Game_state['invalid_input']   = True


def process_game_board(position):
    global game_board
    global Game_state
    #this function is responsible of adding the player choice on the board and check if a player won or
    #there is a draw in the game
    if(Game_state['player_one']):
        game_board[position] = 'X'
        
        
    else:
        game_board[position] = 'O'
        
    
    #check if a player won or not
    row_index = 0 
    col_index = 0
    while(row_index < 7):
        #this loop is responsible for checking if one of the players won by completing a row
        if (game_board[row_index] == game_board[row_index+1] == game_board[row_index+2]):
            Game_state['running'] = False
            if(Game_state['player_one']):
                Game_state['player_won']= 1
            else:
                Game_state['player_won'] = 2
            draw() # calling the draw function to draw the last input before printing the player won
        row_index += 3 

    while(col_index<3):
       
        #this loop checks if one of the players won by completing a column
        if (game_board[col_index] == game_board[col_index+3] == game_board[col_index+6]):
            Game_state['running'] = False
            if(Game_state['player_one']):
                Game_state['player_won'] = 1
            else:
                Game_state['player_won'] = 2
            draw() # adding a draw call here to draw the last state
        col_index += 1
    
    #checking for the win by a diagonal
    if (game_board[0] == game_board[4] == game_board[8] or game_board[2] == game_board[4] == game_board[6]):
        Game_state['running'] = False
        if(Game_state['player_one']):
            Game_state['player_won'] = 1
        else:
            Game_state['player_won'] = 2
        draw() # adding a draw call here to draw the last state

    #check if the game is a draw 
    if (all(value == 'X' or value == 'O' for value in game_board.values())):
        Game_state['running'] = False
        Game_state['draw']    = True
        draw()
    Game_state['player_one'] = not Game_state['player_one']


while(Game_state['running']):
    #this is the game loop that will keep running as long as no player won or there is a draw
    draw() #calling the draw function to draw the game
    handle_input() #handeling the input from the player

