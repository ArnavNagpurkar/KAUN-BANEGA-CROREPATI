# Welcome

print('Welcome to "KAUN BANEGA CROREPATI SEASON 9"')

# List of Questions

que = ["Which of the following gods is also known as ‘Gauri Nandan’?", "In the game of ludo the discs or tokens are of how many colours?", "Which of these are names of national parks located in Madhya Pradesh?", "Where was the BRICS summit held in 2014?", "Who wrote the introduction to the English translation of Rabindranath Tagore’s Gitanjali?", "Which of these leaders was a recipient of a gallantry award in 1987 by a state government for saving two girls from drowning?", "The wife of which of these famous sports persons was once captain of Indian volleyball team?", "The language of Lakshadweep. a Union Territory of India is?", "Which of these terms can only be used for women?", "The internation Literacy Day is observed on?" ]

# print(len(que)) 

# Winnings

win = ["2 Lakh Rupees!","5 Lakh Rupees!","10 Lakh Rupees!", "20 Lakh Rupees!", "40 Lakh Rupees!", "80 Lakh Rupees!", "1 Crore Rupees", "2 Crore Rupees!", "4 Crore Rupees!", "7 Crore Rupees!"]
# print(len(win))

#Correct Answer Then Go to Next Question

def correctAns():
    nxtInput = input("Proceed to next question? (Y/N): ")
    if nxtInput == "y" or nxtInput == "Y" or nxtInput == "Yes" or nxtInput == "yes":
        print("Next Question:-")
    else:
        print("Thank for playing! Your Money will be transfered to your bank account soon! \n Exiting...!")

# Wrong Answer Then exit

def wrongAns():
    print("Your answer is wrong! Better Luck next time. \n Exiting...!")
    exit()

# Game Start 

# Start confirm

stInput = input("Would you like to start? (Y/N): ")
if stInput == "y" or stInput == "Y" or stInput == "Yes" or stInput == "yes":
    print("Starting...!") 
    

    #Name
    name = input("Enter your full name before starting: ")
    nameUpper = name.upper()
    nameTitle = name.title()

    # Question 1

    print(que[0])
    print("Options Are: \n A.Agni \n B.Indra \n C.Ganesha \n D.Hanuman \n")
    inpQ1 = input("Enter the correct option: ")
    if inpQ1 == "C" or inpQ1 == "c" or inpQ1 == "C." or inpQ1 == "c.":
        print("Your Answer is Right! You Won", win[0])
        correctAns()
    else:
        wrongAns()
        

    # Question 2

    print(que[1])
    print("Options Are: \n A.One \n B.Four \n C.Two \n D.Three \n")
    inpQ2 = input("Enter the correct option: ")
    if inpQ2 == "B" or inpQ2 == "b" or inpQ1 == "B." or inpQ2 == "b.":
        print("Your Answer is Right! You Won", win[1])
        correctAns()
    else:
        wrongAns()

    # Question 3

    print(que[2])
    print("Options Are: \n A.Krishana and Kanhiya \n B.Ghanshyam and Murari \n C.Girdhar and Gopal \n D.Kahna and Mahadev \n")
    inpQ3 = input("Enter the correct option: ")
    if inpQ3 == "D" or inpQ3 == "d" or inpQ3 == "D." or inpQ3 == "d.":
        print("Your Answer is Right! You Won", win[2])
        correctAns()
    else:
        wrongAns()
    
    # Question 4

    print(que[3])
    print("Options Are: \n A.Brazil \n B.India \n C.Russia \n D.China \n")
    inpQ4 = input("Enter the correct option: ")
    if inpQ4 == "A" or inpQ4 == "a" or inpQ4 == "A." or inpQ4 == "a.":
        print("Your Answer is Right! You Won", win[3])
        correctAns()
    else:
        wrongAns()

    # Question 5

    print(que[4])
    print("Options Are: \n A. P.B. Shelley \n B. Alfred Tennyson \n C. W.B. Yeats \n D. T.S. Elliot \n")
    inpQ5 = input("Enter the correct option: ")
    if inpQ5 == "C" or inpQ5 =="c" or inpQ5 =="C." or inpQ5 == "c.":
        print("Your Answer is Right! You Won", win[4])
        correctAns()
    else:
        wrongAns()

    # Question 6

    print(que[5])
    print("Options Are: \n A.Anandiben Patel \n B.Vasundara Raje Scinda \n C.Uma Bharti \n D.Mamata Banerjee \n")
    inpQ6 = input("Enter the correct option: ")
    if inpQ6 == "A" or inpQ6 == "a" or inpQ6 == "A." or inpQ6 == "a.":
        print("Your Answer is Right! You Won", win[5])
        correctAns()
    else:
        wrongAns()
    
    # Question 7 

    print(que[6])
    print("Options Are: \n A.K.D. Jadhav \n B.Dhyan Chand \n C.Prakash Padukone \n D.Milkha Singh \n")
    inpQ7 = input("Enter the correct option: ")
    if inpQ7 == "D" or inpQ3 == "d" or inpQ3 == "D." or inpQ3 == "d.":
        print("Your Answer is Right! You Won", win[6])
        correctAns()
    else:
        wrongAns()

    # Question 8 

    print(que[7])
    print("Options Are: \n A.Tamil \n B.Hindi \n C.Malayalam \n D.Telugu \n")
    inpQ8 = input("Enter the correct option: ")
    if inpQ8 == "D" or inpQ7 == "d" or inpQ7 == "D." or inpQ7 == "d.":
        print("Your Answer is Right! You Won", win[7])
        correctAns()
    else:
        wrongAns()

    # Question 9

    print(que[8])
    print("Options Are: \n A.Dirghaayu \n B.Suhagan \n C.Chiranijeevi \n D.Sushil \n")
    inpQ9 = input("Enter the correct option: ")
    if inpQ9 == "B" or inpQ9 == "b" or inpQ9 == "B." or inpQ9 == "b.":
        print("Your Answer is Right! You Won", win[8])
        nxtInput = input("Proceed to next question? (Y/N): ")
        if nxtInput == "y" or nxtInput == "Y" or nxtInput == "Yes" or nxtInput == "yes":
            print("This is last and final question for 7 CRORE RUPEES! All the best!")
            print("Next Question:-")
        else:
            print("Thank for playing! Your Money will be transfered to your bank account soon! \n Exiting...!")
    else:
        wrongAns()

    # Last Question 

    print(que[9])
    print("Options Are: \n A.Sepetember 8 \n B.November 28 \n C.May 2 \n D.September 22 \n")
    inpQ10 = input("Enter the correct option: ")
    if inpQ10 == "A" or inpQ10 == "a" or inpQ10 == "A." or inpQ10 == "a.":
        print("Your answer is Right\n""You won", win[9], "and the contest. \n", nameUpper, "IS THE WINNER OF \"KAUN BANEGA CROREPATI SEASON 9\".\n", "Congrats,",nameTitle ,"you won the contest. \n Your money will be transfered to your bank account soon. \n Thank you for playing the game! \n Exiting...!")
    else:
        wrongAns()

elif stInput == "N" or stInput == "n" or stInput == "No" or stInput == "no":
    print("Exiting...!")
    exit()
else:
    print("Invalid Option!")
    print("Exiting...!")
    exit()