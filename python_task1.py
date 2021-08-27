import random
def num_of_overs(overs): #function defined for input overs
 n = overs * 36
 com_score = random.randint(0, 36) #computer score
 return com_score
 
 
def play(): #fuction defined for player
 play_num = int(input("Enter a number to bat : "))
 com_num = random.randint(0,6)
 print("Computer's number", com_num)
 return play_num, com_num
 
def result(play_num, com_num, total, comp_score): #function defined for result
 if play_num == com_num:
    print(" Total runs scored", total)
    print("You are Out. Computer Won the game")
    return 0;
    
 else:
   total = total + play_num
   print("Total score", total)
 if total > comp_score:
    print("You won the game")
    return 0;
 else:
   return total
 
total = 0 
overs = int(input("Enter number of overs :"))
comp_score = num_of_overs(overs)
print("Computer has scored", comp_score,"runs. Your Target is", comp_score + 1)
for i in range(overs):
 for j in range(6):
    print("Over", i+1, "Ball", j+1)
    play_num, com_num = play()
    total = result(play_num, com_num, total, comp_score)
 if total == 0:
    break
 if(total == comp_score):
   print(" Match tied")
 else:
    print("Overs completed. Computer won the game")