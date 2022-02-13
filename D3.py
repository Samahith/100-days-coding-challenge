# 100 days coding challenge
# Day 3
#  conditional statements, logical operators ,code blocks & scopes
# final project (game)
print( """
        ..--+++--..
     .-'     |     `-.
   +'        |        `+
  '          |          `
 '           |           `
:            |            :
:          +'|`+          :
.        +'  |  `+        ;
 +     +'    |    `+     +
  `. +'      |      `+ .'
    `._      |      _.'
       `--.._|_..--' mh
 """)

# game content
greetings = """
Welcome to treassure island.
your misson is to find the treassure.
 """
print(greetings)
crossroad = input("your at a crossroad. where do yout want ot go , left or right ? \n >>> ").lower()
print(crossroad)
if crossroad == "left":
    print("you have read near the sea bed")
    choise_2 = input("to cross the sea and reach the ocean type boat to wait for a boat or type swim to swim accross \n >>> ").lower()
    if choise_2 == "boat":
        print("you have arrived on the island unharmed")
        choise_3 = input("There is a house in the island with three doors choose a correct door which leads to the treassure").lower()
        if choise_3 == "red":
            print("Game over")
        elif choise_3 == "green":
            print("Game over")
        elif choise_3 == "black":
            print("Congratulations you have found the treassure")
        else :
            print("game over")
    else :
        print("game over")
else:
    print("game over")
