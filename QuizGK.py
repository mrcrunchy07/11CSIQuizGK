import time #for time.sleep (delays)
import os #for terminal clearance
from random import randint

#Defining variables/lists
well_dones = [
  "Correct, well done.",
  "Correct, good job.",
  "Correct, keep it going.",
  "Correct, you're a genius",
  "Correct einstein.",
  "Correct, you're quite the smarty pants aren't ja"
]

wrongs = [
  "Incorrect, but good try.",
  "Incorrect but it alright.",
  "Incorrect... lol",
  "Incorrect"
]

ANSWER = [ #Stores all the correct ANSWERs for the question
  "Fe",
  "2010",
  "Edmund Hillary",
  "Blue Whale",
  "Luigi",
  "Vermicelli",
  "Jupiter",
  "Ambush",
  "11",
  "Mongolia",
]

QQ = [ #Stores the question in order
  "Q1 What is the symbol for Iron? ",
  "Q2 When was the tv show Adventure time created? ",
  "Q3 Who was the first person to climb the top of Mt Everest?  ",
  "Q4 What is the largest mammal? ",
  "Q5 Who is Super Mario's brother? ",
  "Q6 What type of pasta has the name meaning 'little worms'? ",
  "Q7 What is the 5th planet away from the sun? ",
  "Q8 What is a group of tigers called? ",
  "Q9 How many herbs & spices for KFC recipe? ",
  "Q10 What country listed has no sea boarder? ",
]

#The multi CHOICES (4 CHOICES)
CHOICES = ["CHOICES: In  Au  Ir  Fe ",
           "CHOICES: 2014  2010  1991  2018 ",
           "CHOICES: Edmund Hillary  Juerg Marmet  Ernest Rutherford  John Cena ",
           "CHOICES: Elephant  Blue Whale  Gorilla  Giraffe ","CHOICES: Louis  Luigi  Luisa  None ",
           "CHOICES: Vermicelli  Vermiblu  Crostini  Vermilunghi ",
           "CHOICES: Earth  Mars  Jupiter  Venus ",
           "CHOICES: Stripede  Pride  Coalition  Ambush ",
           "CHOICES: 2  6  20  11 ",
           "CHOICES: Poland  Rome  Iran  Mongolia ",
          ]

#Defining functions

def well_done_man():
  global well_dones2
  well_dones2 = well_dones[randint(0,5)] #Generates randomly
  print(well_dones2)
  time.sleep(.3)

def incorrect():
  global wrongs
  incorrects = wrongs[randint(0,3)]
  print(incorrects)
  time.sleep(.3)

def shift(): # Makes a new line
  print("") 

def clear(): # Clears the terminal
  os.system("cls" if os.name == "clr" else "clear")

def instructions(): #The instructions
  print("This quiz topic is General Knowledge (a broad range of facts).\nYou will have 10 questions to answer from 4 choices.\nType one choice you think is correct.\nInclude the capitals aswell in your final ANSWER otherwise it will register as incorrect.")

def greeting(): #greeting
  global name
  name = input("What is your name? ") #Ask their name

def questions(): 
  #set score to 0
  shift()
  print("-----------------------------------------------------------------")
  score = 0
  while score <10: #If they have less than score than will have to keep retrying until the score is 10
    #Q1
    shift()
    print(QQ[0]) # ""
    print(CHOICES[0])
    q = input("ANSWER: ") #input
    if q == ANSWER[0]: #If input is equal to the answer 
      score += 1 # Score goes up by one
      well_done_man() # Words of approval
    else: #If input is not equal to answer
      incorrect() #incorrect so score doesn't change
      if q.strip() == "": #If answer is blank then shows real answer
        print("You didn't answer anything. The real answer is", ANSWER[0])
      else: # If answer incorrect then shows real answer
        print("You answered...",q,". The real answer is", ANSWER[0])

    #Q2
    shift()
    print(QQ[1]) # ""
    print(CHOICES[1])
    q = input("ANSWER: ")
    if q == ANSWER[1]:
      score += 1
      well_done_man()
    else:
      incorrect()
      if q.strip() == "":
        print("You didn't answer anything. The real answer is", ANSWER[1])
      else:
        print("You answered...",q,". The real answer is", ANSWER[1])

    #Q3
    shift()
    print(QQ[2])
    print(CHOICES[2])
    q = input("ANSWER: ")
    if q == ANSWER[2]:
      score += 1
      well_done_man()
    else:
      incorrect()
      if q.strip() == "":
        print("You didn't answer anything. The real answer is", ANSWER[2])
      else:
        print("You answered...",q,". The real answer is", ANSWER[2])

    #Q4
    shift()
    print(QQ[3])
    print(CHOICES[3])
    q = input("ANSWER: ")
    if q == ANSWER[3]:
      score += 1
      well_done_man()
    else:
      incorrect()
      if q.strip() == "":
        print("You didn't answer anything. The real answer is", ANSWER[3])
      else:
        print("You answered...",q,". The real answer is", ANSWER[3])

    #Q5
    shift()
    print(QQ[4])
    print(CHOICES[4])
    q = input("ANSWER: ")
    if q == ANSWER[4]:
      score += 1
      well_done_man()
    else:
      incorrect()
      if q.strip() == "":
        print("You didn't answer anything. The real answer is", ANSWER[4])
      else:
        print("You answered...",q,". The real answer is", ANSWER[4])

    #Q6
    shift()
    print(QQ[5])
    print(CHOICES[5])
    q = input("ANSWER: ")
    if q == ANSWER[5]:
      score += 1
      well_done_man()
    else:
      incorrect()
      if q.strip() == "":
        print("You didn't answer anything. The real answer is", ANSWER[5])
      else:
        print("You answered...",q,". The real answer is", ANSWER[5])

    #Q7
    shift()
    print(QQ[6])
    print(CHOICES[6])
    q = input("ANSWER: ")
    if q == ANSWER[6]:
      score += 1
      well_done_man()
    else:
      incorrect()
      if q.strip() == "":
        print("You didn't answer anything. The real answer is", ANSWER[6])
      else:
        print("You answered...",q,". The real answer is", ANSWER[6])

    #Q8
    shift()
    print(QQ[7])
    print(CHOICES[7])
    q = input("ANSWER: ")
    if q == ANSWER[7]:
      score += 1
      well_done_man()
    else:
      incorrect()
      if q.strip() == "":
        print("You didn't answer anything. The real answer is", ANSWER[7])
      else:
        print("You answered...",q,". The real answer is", ANSWER[7])

    #Q9
    shift()
    print(QQ[8])
    print(CHOICES[8])
    q = input("ANSWER: ")
    if q == ANSWER[8]:
      score += 1
      well_done_man()
    else:
      incorrect()
      if q.strip() == "":
        print("You didn't answer anything. The real answer is", ANSWER[8])
      else:
        print("You answered...",q,". The real answer is", ANSWER[8])

    #Q10
    shift()
    print(QQ[9])
    print(CHOICES[9])
    q = input("ANSWER: ")
    if q == ANSWER[9]:
      score += 1
      well_done_man()
    else:
      incorrect()
      if q.strip() == "":
        print("You didn't answer anything. The real answer is", ANSWER[9])
      else:
        print("You answered...",q,". The real answer is", ANSWER[9])

    #End and their score
    shift()
    print("-----------------------------------------------------------------")
    shift()
    percent = int(score/10*100) # Percentage form
    if score == 10:
      print("Good job, you got them all right. Your score was",score,"out of 10.",percent,"%.")
      score = 10
      while score == 10:
        try:
          retry = int(input("\nWould you like to play again? 1-yes 2-no ")) # They can choose to redo or not
          if retry == 1:
            score = 0
            clear()
          elif retry == 2:
            time.sleep(0.3)
            print("Ok, thanks for playing.")
            break
        except TypeError: #if they enter typeerror
          print("Plz make sure it is 1 or 2")
        except ValueError:
          print("Plz make sure it is 1 or 2")
        except NameError:
          print("Plz make sure it is 1 or 2")
    else:
      print("Good try",(name),". Your score was",score,"out of 10.",percent,"%.")
      score = 0 # They are forced to redo
      time.sleep(3)
      print("Try again")
      time.sleep(2)
      clear()
#Title
print("Multi-choice General Knowledge Quiz") 

#Greetings
while True:
  greeting() #The greeting for their name
  if name.strip() != "":
    break
  print("Please enter your name. \n")
clear()
time.sleep(0.5)
print("Welcome",(name),) #Greets them
time.sleep(1)
instructions() # explains instructions
time.sleep(5) # Pauses time for 5 seconds just so they have time to read the instructions
print("Good luck. You may begin.") # Ready for quiz
time.sleep(1.5)

#Questions
questions() #questions executed
