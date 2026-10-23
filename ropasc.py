import random, sys
print("Let's play ROCK, PAPER, SCISSORS")
wins=0
loses=0
ties=0
while True:
    while True:
        print("Enter your move: ")
        print("(r):Rock, (p):Paper, (s):Scissor, (q): Quit")
        usrInput=input()
        if usrInput=="q":
            sys.exit() #Here the program is left
        elif usrInput=="r":
            print("Rock versus...")
            break
        elif usrInput=="p":
            print("Paper versus...")
            break
        elif usrInput=="s":
            print("Scissor versus...")
            break
        else:
            print("Enter in what's there!")
            continue        
    computerMove=random.randint(1,3)
    if computerMove==1:
        computerMove="r"
        print("Rock")
    elif computerMove==2:
        computerMove="p"
        print("Paper")
    if computerMove==3:
        computerMove="s"
        print("Scissor")
    if usrInput==computerMove:
        print("It's a tie!")
        ties+=1
    elif (usrInput=="r" and computerMove=="p"):
        print("You lose!")
        loses+=1
    elif (usrInput=="r" and computerMove=="s"):
        print("You win!")
        wins+=1
    elif (usrInput=="p" and computerMove=="r"):
        print("You win!")
        wins+=1
    elif (usrInput=="p" and computerMove=="s"):
        print("You lose!")
        loses+=1
    elif (usrInput=="s" and computerMove=="p"):
        print("You win!")
        wins+=1
    elif (usrInput=="s" and computerMove=="r"):
        print("You lose!")
        loses+=1
    print(f"Wins: {wins}, Loses: {loses}, Ties: {ties}")
        
    
