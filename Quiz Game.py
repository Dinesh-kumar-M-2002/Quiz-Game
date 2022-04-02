print("Welcome to my computer Quiz")
playing=input("Do you want to play? ").lower()
score=0
if playing != "yes":
    quit()
else:
    print("Okay Lets Play :)")
answer=input("1.Which planet has the most moons? ").lower()
if answer=="saturn":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
answer=input("2.What country has won the most World Cups? ").lower()
if answer=="brazil":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
answer=input("3.How many bones do we have in an ear? ").lower()
if answer=="3":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
answer=input("4.Name the longest river in the world? ").lower()
if answer=="nile":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
answer=input("5.How many keys does a classic piano have? ").lower()
if answer=="88":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
print("---------------------------------------")
print("You got "+str(score)+"/5"+" correct!!")
print("You got "+str((score / 5) * 100)+"%.")
print("---------------------------------------")
