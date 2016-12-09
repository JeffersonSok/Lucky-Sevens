###
#Lucky Sevens
###

# Start with $10, every game costs $1 to play
# Roll two dice
# If the result is seven win $5 (+$4 overall after the $1 cost)
# The game continously plays until you run out of money.
# At the end, it tells you how many rounds were played.
money = 10  
round_number = 0
print 'Money is', money, "ten dollars"
import random
min = 1
max = 6

roll_again = "yes" 

while money >0:
    round_number += 1
    print "You have played for %d rounds" % (round_number)
    print "Rolling the dice..."
    print "The values are...."
    print random.randint(1, 6)
    print random.randint(1, 6)
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    money -=1
    if die1 + die2 == 7:
       money +=5
       print 'You have', money, 'dollars'
    else:
        print 'You have', money, 'dollars'
