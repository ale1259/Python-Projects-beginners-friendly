print("Welcome to General Knowledge Quiz")

playing = input("Do you want to play? (Y)es or (N)o ")

if playing != "Y":
    print("Well maybe next time")
    quit()

print("Great!!! Let's start")
score = 0

answer = input("What is the capital of France? ")

if answer == "Paris":
   print("Amazing that is the correct answer!!!")
   score += 1
else:
    print("Oohh, that is not correct")


answer = input("Which planet is knoiwn as the 'Red Planet'? ")

if answer == "Mars":
   print("Wow that is CORRECT!!!")
   score += 1

else:
    print("Oohh, that is not correct")


answer = input("Who painted the Mona Lisa? ")

if answer == "Leonardo Da Vinci" or "Da Vinci" or "da Vinci":
   print("Unbelievable!! You knew that one")
   score += 1
else:
    print("Ups, wrong answer, try later")
         


answer = input("Who wrote the play 'Romeo and Juliet'? ")

if answer == "William Shakespeare":
   print("You really know a lot!!!")
   score += 1
else:
    print("Nope!, that is not correct")

answer = input("What is the greatest mammal on earth? ")

if answer == "whale" or "blue whale" or "whales":
   print("Exactly!!! A lot of people confuse this one with the elephant, great job!!!")
   score += 1
else:
    print("MMM, I don't think so")    

print("You got " + str(score) + " questions correct!!")
print("You got " + str((score/ 5) * 100) + "%.")

                    
