number = 15
print(number)
stillPlaying = True
while stillPlaying:
    user_input = int(input("Your choice: "))
    if user_input == 1:
        number -= 3
        print('Computer Chose 2')
        print('There are',number,'cards left')
        if number == 0:
            print('Computer Wins!')
            stillPlaying = False
    elif user_input == 2:
        number -=3
        print('Computer Chose 1')
        print('There are',number,'cards left')
        if number == 0:
            print('Computer Wins!')            
            stillPlaying = False
    else:
        print('Invalid Number')
    
    
    
         