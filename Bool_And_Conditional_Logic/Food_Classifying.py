# randomly set the food  variable to either 'apple','grape', 'bacon', 'steak', 'worm', or 'dirt'.
# Don't worry about how it works for now, we'll learn more shortly.
#
# When you run the prewritten code, food will be randomly assigned.  You task is to write code that will
# classify what food is.
#
# If food is set to either 'apple' or 'grape', your code should print 'fruit'.
# If food is set to either 'bacon' or 'steak', your code should print 'meat'
# If food is set to either 'dirt' or 'worm' your code should print 'yuck'

# NO TOUCHING ============================================
from random import choice
food = choice(['apple','grape', 'bacon', 'steak', 'worm', 'dirt'])
# NO TOUCHING =============================================


# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
if food == 'apple' or food == 'grape':
    print("fruit")
elif food == 'steak' or food == 'bacon':
    print("meat")
else:
    print("yuck")