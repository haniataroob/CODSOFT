import random   
options = ["ROCK","PAPER","SCISSORS"]
while(1):
    print("###### WELCOME TO ROUNDS ######\n")
    choice=input("CHOOSE->ROCK,PAPER,SCISSORS:\n")
    computer_choice=random.choice(options)
    print("Computer chose:", computer_choice)
    if(choice==computer_choice):
        print("Match TIE")
    elif (choice=="ROCK" and computer_choice=="SCISSORS"):
        print("you WON!!")
    elif (choice=="PAPER" and computer_choice=="ROCK"):
        print("you WON!!")
    elif (choice=="SCISSORS" and computer_choice=="PAPER"):
        print("you WON!!")
    else:
        print("COMPUTER WINS!!")

        
