print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

chosen_direction = input('You\'re at a cross road. '
                         'Where do you want to go?\n '
                         'Type "left" or "right"\n').lower()

if chosen_direction == "left":
    chosen_action = input('You\'ve come to a lake. '
                          'There is a island in the middle of the lake.\n '
                          'Type "wait" to wait for a boot. '
                          'or Type "swim" to swim across\n').lower()
    if chosen_action =="wait":
        chosen_door = input("You arrive at the island unharmed. "
                            "There is house with 3 doors. One red, "
                            "one yellow and one blue. "
                            "Which colour do you choose?\n").lower()
        if chosen_door == "yellow":
            print("You Win!")
        elif chosen_door == "red":
            print("Burned by fire.\n Game Over.")
        elif chosen_door == "blue":
            print("Eaten by beasts.\n Game Over.")
        else:
            print("Chosen door doesn't exist.\n Game Over.")
    else:
        print("Attacked by trout.\n Game Over.")
else:
    print("Fall into a whole.\n Game Over.")


