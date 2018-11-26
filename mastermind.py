
### MASTERMIND ###

'''
This code can be adapted for personal use as the game 'mastermind', but it is currently testing a bot code which is statistically superior to a human player.
'''

from random import choice

# if you wish to input manually
def user_(words):
    return list(
        raw_input(
        words
        ).lower()
        )
# break the input into a lowercase list

# find hits and bullseyes
def compare_(guess,ans):
    h,b = 0,0
    # check elements and order
    for x in guess:
        if x in ans:
            # hit
            h += 1
            if x == ans[
            guess.index(x)
            ]:
                # hullseye
                b += 1
    return [guess,[h,b]]

# used by the bot strategy
def check_(guess,hist):
	# checks various conditions before making a guess
    for x in hist:
    	# if guess has happened before
        if guess == x[0]:
            return False
        # if conparison gives incorrect results
        if compare_(
        x[0],guess
        )[1] != x[1]:
            return False
    return True

# bot which plays the game
def bot_(items,hist):
	# randomly choose a guess
    guess = [
    choice(items),
    choice(items),
    choice(items),
    choice(items)
    ]
    # check validity of guess
    while check_(
    guess,hist
    ) == False:
    	# make new random guess to check
        guess = [
        choice(items),
        choice(items),
        choice(items),
        choice(items)
        ]
    return guess


################# Game Structure

def game_(items,ans):
	# count of number of guesses
    counter = 1
    # history of guesses
    hist = []
    guess = bot_(items,hist)
    # add guess to history
    hist.append(
    compare_(guess,ans)
    )
    # repeat the process
    # fail if 16 guesses
    while (hist[-1][1] != [
    4,4] and counter < 16):
        counter += 1
        guess = bot_(items,hist)
        hist.append(
        compare_(guess,ans)
        )
    # return how many guess
    return counter


#################### Main

def main():
	# possible items
    items = ['a','b','c','d','e','f']
    # create secret answer
    answer = [
    choice(items),
    choice(items),
    choice(items),
    choice(items)
    ]
    # return #counters
    return game_(items,answer)


############### uses of the main

# how many samples taken
it = int(input(
"Iterations: ")
)
# collection of samples
list_ = [
main() for y in range(it)
]
# print average number of turns taken by the bot
print (
float(sum(list_))/len(list_)
)

