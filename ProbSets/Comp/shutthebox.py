import sys
import random
import box

if len(sys.argv) == 2:
    name = str(sys.argv[1])
else:
    name = str(input("Player name: "))
print('')
digits = list(range(1,10))
dice = random.randint(2,12)
while box.isvalid(dice, digits) == True and sum(digits)!= 0:
    print('Numbers left: ' + str(digits))
    print('Roll: ' + str(dice))
    player_input = input("Numbers to eliminate: ")
    choices = box.parse_input(player_input, digits)
    while sum(choices) != dice and box.isvalid(dice, digits)==True:
        print("Invalid input")
        player_input = input("Numbers to eliminate: ")
        choices = box.parse_input(player_input, digits)
    else:
        digits = [d for d in digits if d not in choices]
    points = str(sum(digits))
    if sum(digits) < 7:
        dice = random.randint(1,6)
    else:
        dice = random.randint(2,12)
    print('')
if points == "0":
    print('Score for player ' + name + ": " + points + " points.")
    print("Congratulations! You shut the box")
else:
    print('Numbers left: ' + str(digits))
    print("Roll: " + str(dice))
    print("Game over!")
    print('Score for player ' + name + ": " + points + " points.")
