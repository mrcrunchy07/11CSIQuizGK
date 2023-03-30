
#Variables or dictionary
answer = [ #The correct answers
  "Fe","2010","Edmund Hillary","Blue Whale","Luigi","Vermicelli","Jupiter","Ambush","11","Mongolia"
]

qq = [ #The questions
  "Q1 What is the symbol for Iron? ",
  "Q2 When was the tv show Adventure time created? ",
  "Q3 Who was the first person to climb the top of Mt Everest?  ",
  "Q4 What is the largest mammal? ","Q5 Who is super Mario's brother? ",
  "Q6 What type of pasta has the name meaning 'little worms'? ",
  "Q7 What is the 5th planet away from the sun? ",
  "Q8 What is a group of tigers called? ",
  "Q9 How many herbs & spices for KFC recipe? ",
  "Q10 What country listed has no sea boarder? "
]

choices = [ #The multi choices
  "Choices: In  Au  Ir  Fe ","Choices: 2014  2010  1991  2018 ",
  "Choices: Edmund Hillary  Juerg Marmet  Ernest Rutherford  John Cena ",
  "Choices: Elephant  Blue Whale  Gorilla  Giraffe ","Choices: Louis  Luigi  Luisa  None ",
  "Choices: Vermicelli  Vermiblu  Crostini  Vermilunghi ","Choices: Earth  Mars  Jupiter  Venus ",
  "Choices: Stripede  Pride  Coalition  Ambush ",
  "Choices: 2  6  20  11 ",
  "Choices: Poland  Rome  Iran  Mongolia "
]

def shift():
  print(" ") #For a new line so it looks neat in the output


def questions():
  score = 0 #sets score to 0
  while score <10:
    shift()
    print(qq[0]) #prints the question that is in the array
    q = input(choices[0]) #prints the choices that is in the array
    if q == answer[0]: #if it is equal the the answer in array
      score += 1
      print("Correct")
    else:
      print("Incorrect")

    shift()
    print(qq[1])
    q = input(choices[1])
    if q == answer[1]:
      score += 1
      print("Correct")
    else:
      print("Incorrect")

    shift()
    print(qq[2])
    q = input(choices[2])
    if q == answer[2]:
      score += 1
      print("Correct")
    else:
      print("Incorrect")

    shift()
    print(qq[3])
    q = input(choices[3])
    if q == answer[3]:
      score += 1
      print("Correct")
    else:
      print("Incorrect")

    shift()
    print(qq[4])
    q = input(choices[4])
    if q == answer[4]:
      score += 1
      print("Correct")
    else:
      print("Incorrect")

    shift()
    print(qq[5])
    q = input(choices[5])
    if q == answer[5]:
      score += 1
      print("Correct")
    else:
      print("Incorrect")

    shift()
    print(qq[6])
    q = input(choices[6])
    if q == answer[6]:
      score += 1
      print("Correct")
    else:
      print("Incorrect")

    shift()
    print(qq[7])
    q = input(choices[7])
    if q == answer[7]:
      score += 1
      print("Correct")
    else:
      print("Incorrect")

    shift()
    print(qq[8])
    q = input(choices[8])
    if q == answer[8]:
      score += 1
      print("Correct")
    else:
      print("Incorrect")

    shift()
    print(qq[9])
    q = input(choices[9])
    if q == answer[9]:
      score += 1
      print("Correct")
    else:
      print("Incorrect")

    #Their score
    shift()
    if score == 10:
      print("Good job, you got them all right. Your score was",score,"out of 10")
      score = 0 #set score to 0
    else:
      print("Your score was",score,"out of 10. Try again")
      score = 0 #set score to 0

def instructions():
  print("you will have 10 questions to answer from 4 choices. Type one choice you think is correct. Include the capitals aswell in your final answer.")

#Greetings
print("Multi-choice General Knowledge Quiz")
name = input("What is your name? ")
print("Welcome",(name),)
instructions()
print("You may begin")
