name1=input("What is your first name? ")
name2=input("What is your last name? ")
print("Hi there, " + name1+" "+name2 +", nice to meet you")


print("How old are you?")
age=int(input(""))
print(str(age) + " is a great age!")
if (age >=16):
    print("You are old enough to drive! \n")
if (age ==15):
     print("Still taking the bus, i see.\n")
if (age ==14):
     print("Still taking the bus, i see.\n")
if (age ==13):
     print("Still taking the bus, i see.\n")
if (age ==12):
     print("Still taking the bus, i see.\n")
if (age ==11):
     print("Still taking the bus, i see.\n")
if (age <=10):
    print("Oh so car ride from parents, i see.\n")


grade=int(input("What grade are you in?, if adult type 0: "))
if(grade == 1):
    print("First Grader")
elif(grade == 2):
    print("Second Grader")
elif(grade == 3):
    print("Third Grader")
elif(grade == 4):
    print("Fourth Grader")
elif(grade == 5):
    print("Fifth Grader")
elif(grade == 6):
    print("Sixth Grader")
elif(grade == 7):
    print("Seventh Grader")
elif(grade == 8):
  print("Eight Grader")
elif(grade == 9):
    print("Freshman")
elif(grade == 10):
    print("Sophomore")
elif(grade == 11):
    print("Junior")
elif(grade == 12):
    print("Senior")
if(grade == 0):
  print("You're out of school!")

fav_subject=input("Ok so, " + name1 +", what or what was your favorite subject at school?\n")

if(fav_subject=="math"):
  print("oh math, I love math but you really have to sit down and learn\nthe different units.")
  math_answer=int(input("Let me quiz you on it, whats 9x9:"))
  if(math_answer == 81):
    print("CORRECT!")
  else:
    print("You might need to study more")

if(fav_subject=="Math"):
  print("oh math, I love math but you really have to sit down and learn the different units.")
  math_answer=int(input("Let me quiz you on it, whats 9x9:"))
  if(math_answer == 81):
    print("CORRECT!")
  else:
    print("You might need to study more")  

if(fav_subject=="science"):
  print("science is a very interesting and complex subject.")
  science_answer=input("If you like science so much here is a question,\nWhat is the farthest planet from the solar system? ")
  if(science_answer=="pluto"):
    print("that is not a planet anymore")
  elif(science_answer=="neptune"):
    print("CORRECT!")
  else:
    print("Wrong.... go study more")
  
if(fav_subject=="history"):
  print("history is a fun subject to look back at our past and learn from it. ")
  history_answer=input("If you like history so much here is a question,\n Who was the 16th president? ")
  if(history_answer=="Abraham Lincoln"):
    print("CORRECT!")
  else:
    print("Incorrect maybe go read a book")

if(fav_subject=="english" or fav_subject=="English"): 
  print("english is a fun subject to learn and also where you improve your reading and writing skills. ")
  english_answer=input("If you like english so much here is a question, \nWhat do you do at the beginning of a paragraph?")
  if(english_answer=="indent"):
    print("CORRECT!")
  else:
    print("Incorrect sorry")

if(fav_subject=="langague subject"):
  print("Langague subjects are amazing because you can learn a brand new langague like\nSpanish, French, And other langagues. ")
  langague_subject=input("If you like langagues so much\nwhat is the most popular langague spoken in Spain? ")
  if(langague_subject=="Spanish"):
    print("CORRECT!")
  else:
    print("Incorrect maybe next time you get it right")

fav_sport=input("Hey, " + name1 +", do you have any favorite sports? ")

if(fav_sport=="soccer"):
  print("Soccer is a really fun sport to play but also known as football in other countries.")

if(fav_sport=="football"):
  print("American football is a sport mostly played in the U.S\nbut other countries also play this sport but not in a competitive arena.")

if(fav_sport=="baseball"):
  print("baseball is a really cool sport which is played all around the world!")

if(fav_sport=="basketball"):
  print("Basketball is a hard and a sport that has a lot going on\nespecially with the ways you have to play the sport but overall pretty fun!")

if(fav_sport=="crew" or fav_sport=="rowing"):
  print("This is a very underated sport which is super\nfun to do! ")

if(fav_sport=="golf"):
  print("Oh so a future Tiger Woods I see!")

if(fav_sport=="swim" or fav_sport=="Swim"):
  print("Swim! I love swim and who knows maybe you can become a new Michael Phelps")

if(fav_sport=="wrestling" or fav_sport=="Wrestling"):
  print("Wrestling is a very complex sport and you have \nto be really built so good for you!")

if(fav_sport=="tennis" or fav_sport=="Tennis"):
  print("Tennis is a very engaging athletic sport that's super cool!")

print("So, " + name1 +", how are you today?")
feel=input("")
print("You are " + feel),
if(feel == "Happy"):
    print("That's good to hear!")
elif(feel == "Sad"):
    print("I'm sorry to hear that.")
elif(feel == "Meh" or "meh"):
    print("Hey at least your not in a sad mood!")
else:
    print("Oh okay")
   
print("Tell me more.\n")
print("1 means your day was interesting, 2 means you had a good day, 3 you had a wacky day")
next=input("Type a number ")
import random
r = random.randint(1, 3)
if(r == 1):
    print("Sounds interesting.\n")
elif(r == 2):
    print("That's good to hear.\n")
else:
    print("How unusual.\n")

print("hey im kind of bored now, lets play a game")
game=input("Choose from:\n roll the dice: type 1 \n guess the number: type 2 \n rock paper scissors:type 3 \n game choice:")
if(game=="1"):
  c=0
  while int(input("Press 1 to roll the dice or press 0 to exit\n")):
    c=c+1
    print("you rolled a: ")
    print(random.randint(1,6))
    print("you rolled the dice", c, "times")

if(game=="2"):
  guess_number=random.randint(1,100)
  for i in range (0,11):
    user_guess=int(input("Guess the number (1-100),ten guesses max :"))
    if (user_guess==guess_number):
      print("you did it!")
      print("The right number was" ,guess_number)
    elif(user_guess>guess_number):
      print("Your guess is too high")
    elif(user_guess<guess_number):
      print("Your guess is too low")
    
if(game=="3"):
 import random
 choices = ["Rock", "Paper", "Scissors "]
 computer = random.choice(choices)
 player = False
 cpu_score = 0
 player_score = 0
 while True:
    player = input("Rock, Paper or Scissors?,(0 to end)").capitalize()
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "beats", player)
            cpu_score+=1
        else:
            print("You win!", player, "beats", computer)
            player_score+=1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "loses to", player)
            cpu_score+=1
        else:
            print("You win!", player, "beats", computer)
            player_score+=1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "wins", player)
            cpu_score+=1
        if computer == "Paper":
            print("You Win!", computer, "loses to", player)
            cpu_score+=1
        else:
            print("You win!", player, "Loses to", computer)
            player_score+=1
    elif player=="0":
        print("Final Scores:")
        print("CPU:",cpu_score)
        print("Plaer:",player_score)
        break
print("Well," + name1 +", it has been nice chatting with you.")