# - Game Program Script Training, including nested if/else statements

print ("-------Game On!----------")
player = input ("Hello. What is your name?\n: ")

game = input ("It's nice to meet you " + player + ". Do you like games? y/n: ")

if game == ("y"):
    print ("Let's play a game.")
    
else:
    print ("...What a shame. I had such a great idea for a game " + player + ". ")
    exit()

print ("Okay. I'll go first")
players_guess = input ("Guess what number I'm thinking of between 1 and 9 \n")

if players_guess == ("5"):
    print ("You got it! I know... this is a horrible game.")
    print ("How about a nice game of chess?")
else:
    print ("Nope!")
    print ("You are awful at this. Have you considered golf?\nWe should try soemthing else.")
    

player_game = input ("I actually can't play chess yet Do you know any games? \nTell me: ")
print ("I don't know how to play " + player_game + ". \nMaybe we should just sit here and drink booze? ")

player_drink = input ("Wait... do you drink? \n y/n:")
if player_drink == ("n"):
    print ("A thousand appologies, no offense intended. We can try something else. ")
    
else:
    player_drink_type = input("What kind of adult beverage do you enjoy most? \nTell me: ")
    print ("Oh wait... are you even old enough to drink " + player_drink_type + "? ")
    player_age = input ("How old are you?\n age: ")

    if player_age >= "21":
        print ("Okay " + player + "! I'll see if I can find some " + player_drink_type)
    
    else:
        print ("Bugger off " + player + "!" +"\nYou are only " + player_age + " \nAre you trying to get me in trouble?")
        print ("No " + player_drink_type + " for you!")       

print ("Question. Do you have any favorite books? ")
player_book = input ("Tell me your favorite: ")
print ("I've never read, " + " '" + player_book + "' ")
print ("Well, this has been fun " + player + "! I'll be going now. \nYou look like you have all this in order.")
print ("Remember, purple ice-cream has no bones!\n --------Game Over--------")

endgame = input("\n \n \n Press q to quit ")
if endgame == ("q"):
    print ("Bye " + player + "! ")
    exit ()
else:
    print ( player + "!!!!!! I really need to use the bathroom! I'm out! ")
    exit ()


















