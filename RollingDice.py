import random
diceNum = [1,2,3,4,5,6]
while True:
  print random.choice(diceNum)
  inputChoice = raw_input("Do you want to roll the Dice ?")
  if(inputChoice.lower() == 'yes') :
    continue 
  else :
    break
