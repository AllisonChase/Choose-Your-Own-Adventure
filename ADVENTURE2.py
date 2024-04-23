import os
import pandas as pd

#money count
#travel walks and finds 500 gold on the road
#goes to pub spends 100 gold
#plays cards and wins 164 gold
#gets cocky and looses 469 gole
#shows the gold count after this interaction

moneycount=[]

print()
print("Hello traveler!  You walk towards a villiage and look down!  What luck, a bad of 500 gold!")
print()
moneycount.append(int(500))

choice1=input("Would you like to go to the pub, or run away with the cash? Pub or run? ")

if choice1.lower()== "pub":
    print("Hooray time to get our drink on.  You spend 100 gold on a round of drinks")
    moneycount.append(int(-100))
else:
    print("if you're going to be borning then game over.")


choice2=input("Some goblins have a gambling cards table going on! Will you join?   y/n? ")

if choice2.lower()=="y":
    print("You sit down for some cards.   It's your lucky day, you win 164 gold!")
    moneycount.append(int(164))
else:
    print("seriously, what a buzzkill. go home")


choice3=input("You're on a hot streak, keep playing?  y/n? ")

if choice3.lower()=="y":
    print("oooooo.  Should have quit while you were hot.  You lose 469 Gold.")
    moneycount.append(int(-469))

print("here's how much you have left:")
print(sum(moneycount))

travelcompanions={"Fred":"Rouge", "Susan":"Orc","FlippidyDoo":"Gnome"}

travelcompanions["Gordon"] ="Elf"
travelcompanionsDF=pd.DataFrame(travelcompanions.items(),columns=["Name","Race"])
travelcompanionsDF.index += 1
# print(travelcompanionsDF)

print(travelcompanionsDF)