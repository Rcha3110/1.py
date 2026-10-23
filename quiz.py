print("Welcome to the game WILDER KBC \n I hope you are well aware of the rules of the game\n Ok for those who don't know --\n ")
print("This game is all about answering the right questions... and if you fail you will end up out of the game with the amount you get!")
print("Let's begin the game")
question=["Who's the most beautiful girl in this world?\n a. Aarcha\t b. Rhea\n c.Arya\t d.Manheer",
          "When was Aarcha born?\n a. 28th July, 2004\t b. 31st February,2004\n c. 29th October, 2005\t d. 31st October, 2004", 
          "Aarcha is familiar with which European Language?\n a. French\t b. Spanish\n c. Italian\t d. German",
            "What is Aarcha's current weight?\n a. 58kg\t b.55kg\n c. I lost weight 😭\t d.33kg", "Her height?\n a.148cm\t b.156cm\n "
            "c.153cm\t d.169cm", "What's her meantime snack?\n a.Beer\t b.Coke\n c.Coffee\t d.Milk",
            "What's her favorite season?\n a.Summer\t b.Rainy\n c.Autumn\t d.Winter",
            "Her favorite game?\n a.Arm Wrestling\t b.Football\n c.Cricket\t d.Skating",
            "How many years of driving experience she has?\n a. 9yrs\t b. 6yrs\n c. 2yrs\t d. 6months",
            "She's inspired to which person?\n a. Her sister \t b. Herself \n c. Ghanta inspo mah brain is fried\t d. Him"]
answer=["a","d","b","c","c","d","a","b","a","c"]
reward=[1000,2000,5000,10000,20000,40000,80000,120000,9000000,10000000]
for i in range(len(question)):
    print("Question is: ",question[i])
    guesss=str(input("Answer any one (a-d): ")).strip().lower()
    if guesss ==answer[i]:
        print("Your answer is right!")
        print(f"Your reward is : ",reward[i], " euros")
    else:
        print("You're a loser")
        print(f"You managed to earn",reward[i]," euros")
        break
print("Game over!")
