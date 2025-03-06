place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!") 
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    action = input('light a torch or proceed through the dark ?')
    if action == 'light a torch':
        print("Is that a chest? you found a hidden treasure!")
    elif action =='proceed through the dark':
        print("you seem to have stumbled over what seems to be a log")