# Program Capable of displaying questions to the user like KBC. Use List Data type to store the questions and their Correct Answer. Display the final Amount the person is taking home after playing the game. 

username = input("Enter your Name : ")
place = input ("Enter Your Address : ")
print(" \n Hi !!" , username ,"Welcome To The Game")

# Game Rules 
rules = """ \n Rules to be followed :
    1. You have 5 Questions.  
    2. Each Question has Different rewards.  
    3. No Helplines are available. 
    4. One Wrong Answer you will get eliminated.
    5. On Elimination you will get most recent game price."""
print(rules.title()) # Capitalize the 1st letter in each word

start = " \n Let The Game Begins"
print(start)

# Display Question Number and Reward
def ques (num , amt) :
    print("*".center(100 , "*"))
    print("Question " , num)
    print("Reward : " , amt)
    return "\n" 

# On Winning The Game
def win (winAmt) :
    print("Congratulation !!" , username)
    print(username , "From" ,place , "Won" ,winAmt)
    return "\n"

# On Entering Wrong answer
def loss (winAmt) :
    print("Your Answer Is Wrong !!")
    print("Try Again !!")
    print("You Won",winAmt)
    return "\n"

# On Entering Right answer
def proceed (winAmt) :
    print("Your Answer Is Right !!")
    print("You Won",winAmt)
    print("\nNext Question >> ")
    return "\n"

# Quiz Starts Here !!

# Question  1
print(ques(1 , "Rs 10000"))
ques1 = ["Total Letters in English Alphabet" , "26" , "16" , "27" , "17" ]

for i in ques1 :      # Runs a loop for indexes of above list
    print(i)

print("Enter Your Answer :")
ans1 = input("")
if (ans1 == ques1[1]) :
    print(proceed ("Rs 10000"))
else :
    print(loss("Rs 0"))
    print("Correct Answer is " , ques1[1])
    exit(1)

# Question  2
print(ques(2 , "Rs 20000"))
ques2 = ["Total Planets in Our Solar System" , "9" , "7" , "8" , "10" ]

for j in ques2 :
    print(j)

print("Enter Your Answer :")
ans2 = input("")
if (ans2 == ques2[3]) :
    print(proceed ("Rs 20000"))
else :
    print(loss("Rs 10000"))
    print("Correct Answer is " , ques2[3])
    exit(2)

# Question  3
print(ques(3 , "Rs 50000"))
ques3 = ["Total Number of Days in a Week" , "9" , "7" , "8" , "10" ]

for k in ques3 :
    print(k)

print("Enter Your Answer :")
ans3 = input("")
if (ans3 == ques3[2]) :
    print(proceed ("Rs 50000"))
else :
    print(loss("Rs 20000"))
    print("Correct Answer is " , ques3[2])
    exit(3)

# Question  4
print(ques(4 , "Rs 70000"))
ques4 = ["Name the 7th Month in the Year " , "JULY" , "AUGUST" , "MARCH" , "DECEMBER" ]

for l in ques4 :
    print(l)

print("Enter Your Answer :")
ans4 = input("")
if (ans4 == ques4[1]) :
    print(proceed ("Rs 70000"))
else :
    print(loss("Rs 50000"))
    print("Correct Answer is " , ques4[1])
    exit(4)

# Question  5
print(ques(5 , "Rs 100000"))
ques5 = ["Which is the National Game of India ?" , "Cricket" , "Hockey" , "Badminton" , "None of Above" ]

for m in ques5 :
    print(m)

print("Enter Your Answer :")
ans5 = input("")
if (ans5 == ques5[2]) :
    win ("Rs 100000")
else :
    print(loss("Rs 70000"))
    print("Correct Answer is " , ques5[2])
    exit(5)

print("The End".center(150 , "*"))

# Quiz Ends !!