# This is a fundamentals project. I was on the Bandit Challenge over
# at Overthewire.org and have gotten almost half way through it and was noticing
# that I was using a little bit of muscle memory. I thought to myself, "in
# order to really get the most out of this, I should start randomizing the
# levels I have already beaten and play it through like that to make reinforce
# those core linux commands". So, I thought, what a great challenge/ homework project.
# I'm just starting my classes in Python, I should be able to make a random number
# generator that can be set by the user based on the levels they want to play randomly.Sorry! No passwords here...
# This is where that rabbit hole, a 2 liter bottle of Coke and some perfectly legal
# cannibis took me. So, now when I want to run the Bandit Challenge, I open up this little beauty
# enter the scope of levels I want to challenge myself with and the program makes the decissions for me.
# Enjoy!

#-------The Bandit Challenge Random Level Generator-------------------------------

#import random

print ("Welcome to The Bandit Challenge Random Level Generator - By: Badger_Chaotica")
print("-------------------------------------------------------------------------------")

lowest_level = input("What is the lowest level you would like to randomly play?\n0=34: ")
highest_level = input("Okay, now what's the highest level you would like to randomly play?\n0-34: ")
print ("Randomizing...")

import random
random_level = random.randint((int(lowest_level)),(int(highest_level)))
print ("-------------")
print("Play Level " + (str(random_level)))
print ("-------------")

import time
time.sleep(10)
exit ()

# At this time I can only assume I will be able to loop these commands and start from scratch after
# completing each levels. I just keep my passwords on a notepad open as I play. As I learn more Python,
# I will be able to tweak this some more. Still a work in progress. Cheers! --Badger_Chaotica--


















