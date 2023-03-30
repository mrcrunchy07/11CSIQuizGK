def shift():
  print(" ")


def questions():
  #set score to 0
  score = 0
  while score <10:
    shift()
    print(qq[0])
    q = input(choices[0])
    if q == answer[0]:
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
      score = 10
      try:
        retry = int(input("Would you like to try again? 1-yes 2-no "))
        if retry == 1:
          score = 0
        elif retry == 2:
          print("ok")
      except TypeError:
        print("Plz make sure it is y/n")
      except ValueError:
        print("Plz make sure it is y/n")
      except NameError:
        print("Plz make sure it is y/n")
    else:
      print("Your score was",score,"out of 10. Try again")
      score = 0
