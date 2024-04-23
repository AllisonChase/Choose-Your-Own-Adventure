#Choose your own adventure

# You're a traveler who just arrived in a small village.  Tell us about yourself.
#What is your name, race and class?
#races are: Human, elf, dwarf, orc, goblin, gnome"
#Classes are: Druid, Sorcerer, Bard, Cleric, Rouge, Artificer, Fighter
#Welcome to your new adventure.  Do you want to go in the pub, or store
# if the answer is store, it's closed
# if the answer is pub. move on.
#speak to the bartender.  Bartender says hi how are you
# you have the following choices to answer:  "hello, good sir.  "what the hell are you looking at? "Give me a beer barkeep before i stab you!, "say nothing and scowl.
# any choice other than the first one results in "That's rude try again if you want service."
#what drink would you like
#you don't have any money and the bartender asks you to leave.
#do you, leave, steal a drink from the shelf, steal a drink from behind the bar?
#if you chose on of the short races, and you steal from the shelf, you get caught, if you're tall you get away with it
#if you chose one of the tall races and you still from behind the bar, you get caught, if you're short you get away with it.

#if you chose to leave, you go outside and see a persong gettting attacked
#if you chose to steal, you are inside and hear a person getting attacked, and then went outside to investigate, and see the person getting attacked.


#start next loop


def main():
    print("Welcome to the Adventure!")
    
    # Valid races and classes
    valid_races = ["human", "elf", "dwarf", "orc", "goblin", "gnome"]
    valid_classes = ["druid", "sorcerer", "bard", "cleric", "rogue", "artificer", "fighter"]
    
    while True:
        name = input("What is your name? ")
        
        race = input("What is your race? (Human, Elf, Dwarf, Orc, Goblin, Gnome) ").lower()
        if race not in valid_races:
            print("That race doesn't exist in this world. Please choose again.")
            continue  # Restart the loop
        
        player_class = input("What is your class? (Druid, Sorcerer, Bard, Cleric, Rogue, Artificer, Fighter) ").lower()
        if player_class not in valid_classes:
            print("That class doesn't exist in this world. Please choose again.")
            continue  # Restart the loop
        
        print("\nWelcome to your new adventure, " + name + " the " + race.capitalize() + " " + player_class + "!")
        break  # Exit the loop once valid input is provided
    
    while True:
        print("\nYou find yourself in a small village. Do you want to go to the pub or the store?")
        location_choice = input("Enter 'pub' or 'store': ").lower()
        
        if location_choice == "store":
            print("\nThe store is closed. You decide to move on.")
        elif location_choice == "pub":
            print("\nYou enter the pub and see the bartender behind the counter.")
            bartender_greeting = input("The bartender says, 'Hi, how are you?' How do you respond?\n"
                                       "1. 'Hello, good sir.'\n"
                                       "2. 'What the hell are you looking at?'\n"
                                       "3. 'Give me a beer barkeep before I stab you!'\n"
                                       "4. Say nothing and scowl.\n"
                                       "Enter your choice (1, 2, 3, or 4): ")
            
            if bartender_greeting == "1":
                print("\nThe bartender nods and asks, 'What drink would you like?'")
                drink_choice = input("You don't have any money. Do you:\n"
                                     "1. Leave the pub\n"
                                     "2. Attempt to steal a drink from the shelf\n"
                                     "3. Attempt to steal a drink from behind the bar\n"
                                     "Enter your choice (1, 2, or 3): ")
                
                if drink_choice == "1":
                    print("\nYou decide to leave the pub. As you step outside, you see a person getting attacked!")
                elif drink_choice == "2":
                    if race in ["human", "elf", "orc"]:
                        print("\nYou successfully steal a drink from the shelf and enjoy it.")
                        print("\nAs you sip your stolen drink, you hear a commotion outside.")
                        print("You rush outside and see someone getting attacked!")
                    else:
                        print("\nYou attempt to steal a drink from the shelf, but you get caught!")
                elif drink_choice == "3":
                    if race in ["dwarf", "goblin", "gnome"]:
                        print("\nYou successfully steal a drink from behind the bar and enjoy it.")
                        print("\nAs you enjoy your stolen drink, you hear a commotion outside.")
                        print("You rush outside and see someone getting attacked!")
                    else:
                        print("\nYou attempt to steal a drink from behind the bar, but you get caught!")
                else:
                    print("\nThat's rude! The bartender asks you to leave.")
            else:
                print("\nThat's rude! The bartender says, 'That's rude. Try again if you want service.'")
        else:
            print("\nInvalid choice. You wander around and eventually leave the village.")
            break  # End the loop and exit the game
    
    print("\nGame Over. Thanks for playing!")

# Call the main function to start the game
main()
         