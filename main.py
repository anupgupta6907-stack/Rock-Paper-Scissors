
# r= rock
# p= paper
# s= scissors

import random
computer = random.randint(1,3)


yourchoice =input("Enter your choice :")
gamedict = { "r":1 ,"p":2,"s":3}
you= gamedict[yourchoice]
reversedict = { 1:"rock", 2: "paper" , 3:"scissors"}
print(f"Computer chose {reversedict[computer]} \n You chose {reversedict[you]}")
if (computer == you):
    print("It's a draw !")
else:
    if (computer == 1 and you == 2): 
        print (" You win !")
    elif (computer == 1 and you == 3):  
        print ( " You lose !")  
    elif (computer == 2 and you == 1): 
        print ( " You lose !")     
    elif (computer == 2 and you == 3):  
        print (" You win !")  
    elif (computer == 3 and you == 1): 
        print (" You win !")   
    elif (computer == 3 and you == 2):  
        print ( " You lose !")    
    else:
        print(" OOPS! Something went wrong") 
