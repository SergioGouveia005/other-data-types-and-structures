
import random
def flip_a_coin():
    return random.randint(0,1)

correct_guesses = 0
#Strategy 1 = Randomly changing between heads and tails
for i in range(10000):
    if flip_a_coin() == flip_a_coin():
        correct_guesses += 1

print("With Strategy 1 = Randomly changing between heads and tails\n" +
    f"Success Rate = £{correct_guesses}\n")

correct_guesses = 0
#Strategy 2 = Sticking with one
for i in range(10000):
    if flip_a_coin() == 1:
        correct_guesses += 1

print("With Strategy 2 = Sticking with one\n" +
    f"Winnings = £{correct_guesses}\n")