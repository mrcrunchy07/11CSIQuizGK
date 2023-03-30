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


def instructions():
  print("you will have 10 questions to answer from 4 choices. Type one choice you think is correct. Include the capitals aswell in your final answer.")

#Greetings
print("Multi-choice General Knowledge Quiz")
name = input("What is your name? ")
print("Welcome",(name),)
instructions()
print("You may begin")
