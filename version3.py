print("the game")
print("input 1 or 2")
total = 15
win1 = 0

while (total > 0):
  user1choice= int(input("player 1 "))
  
  if user1choice == 1:
    total -= 1
    if total == 0: 
      win1 = "Player 1 wins "
  elif user1choice == 2:
    total -= 2
    if total == 0: 
      win1 = "Player 1 wins "
      break
  print(total, " numbers left ")


  
  user2choice= int(input("player 2 "))
 
  if user2choice == 1:
    total -= 1
    if total == 0: 
      win1 = "Player 2 wins "
  elif user2choice == 2:
    total -= 2
    if total == 0: 
      win1 = "Player 2 wins "
  print(total, " numbers left ")
print("the winner is ", win1)