game_session = True
piece_count = 15
user_turn = True

print("Welcome to my sick twisted game. You go first...")
#ez_mode = input("By the way, do you want me to go easy, you big baby? (YES)")
#if ez_mode.upper() == 'YES':
#    ez_mode = True

while game_session == True:
    user_turn = True
    user_take = input("Take 1 or 2. ")
    if int(user_take) == 1:
        piece_count -=1
        print("You took 1. so I'll take 2. ")
        piece_count -=2
        user_turn = False
        
    elif int(user_take) == 2:
        piece_count -=2
        print("You took 2, so I'll take 1. ")
        piece_count -=1
        user_turn = False
    
    else:
        print("That's nonsense, say '1' or '2', foolish human!")
    
    print("Piece count is:", piece_count)
    if piece_count <= 0:
        game_session = False
    
    
    
if user_turn == False:
    print("You lose, kihihihi!")
else:
    print("I lose? This wasn't supposed to happen...!")
    

  