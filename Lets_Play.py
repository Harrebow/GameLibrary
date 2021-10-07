import random
    
gameList = [
            "diceroll", 
            "coinflip",
            "rockpaperscissors"
            ]

gameList_hidden = [
            "rpsls", 
            "rps",
            "dice",
            "coin",
            "flip",
            "roll"
            ]

class gameerr(Exception):
    pass
class dicerollerr(gameerr):
    pass
class coinfliperr(gameerr):
    pass
class rockpaperscissorserr(gameerr):
    pass


def cleanup(word):
    word = word.lower()
    nope = [" ","!","#","$","%","&","'","*","+","-",".","^","_","`","|","~",":","(",")","]","[","{","}","\\","/",'"',"£"]
    clean = ""
    for char in word:
        if char in nope:
            continue
        else:
            clean += char
    return clean

def diceroll():
    rolls = input("\nPlease type how many times you would like to roll the dice: ")
    dice = input("\nHow many sides would you like your dice to have? The default is 6 sides: ")
    print("\n")

    if dice == "":
        dice = "6"
    if not dice.isdigit() and rolls.isdigit():
        raise dicerollerr()

    for i in range(int(rolls)):
        roll = random.randint(1, int(dice))
        if roll != 1:
            print("You rolled a:", roll)
        else:
            print("You rolled a 1. Critical fail!\nThe goblin steals all your gold and your lucky sword!")
    return

def coinflip():
    rounds = input("\nPlease type how many times you would like to flip the coin: ")
    face = input("\nPlease choose Heads or Tails: ")
    print("\n")
    face = cleanup(face)
    if not rounds.isdigit() and face != "heads" or not rounds.isdigit() and face != "tails":
        raise coinfliperr

    pScore, cScore = 0, 0
    faces = {0:"heads", 1:"tails"}

    for x in range(int(rounds)):
        flip = random.randint(0,1)
        if face == faces[flip]:
            pScore += 1
        else:
            cScore += 1
        print("Round " + str(x+1) + ":", faces[flip].title())
    
    score(pScore,cScore)

def rockpaperscissors():
    rounds = input("Please type how many times you would like to play: ")
    print("\n")

    pScore, cScore = 0, 0
    hands = ["rock", "paper", "scissors"]
    phand = "rock"

    for x in range(int(rounds)):
        hand = input("\nPlease choose Rock or 'r', Paper or 'p', Scissors or 's': ")
        hand = cleanup(hand)
        if hand == "r":
            hand = "rock"
        elif hand == "p":
            hand = "paper"
        elif hand == "s":
            hand = "scissors"
        elif hand == "":
            hand = phand
        elif hand not in hands:
            raise rockpaperscissorserr()
        
        phand = hand

        chand = hands[random.randint(0,2)]
        if hand == chand:
            print("Round " + str(x+1) + ": " + "Draw!")
        elif chand == hands[0] and hand != hands[1]:
            print("Round " + str(x+1) + ":", chand, "beats", hand, "sorry. Try again.")
            cScore += 1
        elif chand == hands[1] and hand != hands[2]:
            print("Round " + str(x+1) + ":", chand, "beats", hand, "sorry. Try again.")
            cScore += 1
        elif chand == hands[2] and hand != hands[0]:
            print("Round " + str(x+1) + ":", chand, "beats", hand, "sorry. Try again.")
            cScore += 1
        else:
            print("Round " + str(x+1) + ":", hand, "beats", chand, "Congratulations! You Win.")
            pScore += 1

    score(pScore,cScore)

def rpsls():
    rounds = input("Please type how many times you would like to play: ")
    print("\n")

    pScore, cScore = 0, 0
    hands = ["rock", "paper", "scissors", "lizard", "spock"]
    phand = "rock"

    for x in range(int(rounds)):
        hand = input("\nPlease choose Rock or 'r', Paper or 'p', Scissors or 's', Lizard or 'l', Spock or 'v': ")
        hand = cleanup(hand)
        verb = ["cuts","covers","crushes","poisons","smashes","decapitates","eats","disproves","vaporizes"]
        if hand == "r":
            hand = "rock"
        elif hand == "p":
            hand = "paper"
        elif hand == "s":
            hand = "scissors"
        elif hand == "l":
            hand = "lizard"
        elif hand == "v":
            hand = "spock"
        elif hand == "":
            hand = phand
        elif hand not in hands:
            raise rockpaperscissorserr()
        
        phand = hand

        chand = hands[random.randint(0,4)]
        if hand == chand:
            print("Round " + str(x+1) + ":", chand, "vs", hand, "Draw!")
        elif chand == hands[0] and hand == hands[2] or chand == hands[0] and hand == hands[3]:
            print("Round " + str(x+1) + ":", chand, verb[2], hand, "sorry. Try again.")
            cScore += 1
        elif chand == hands[1] and hand == hands[0] or chand == hands[1] and hand == hands[4]:
            if hand == hands[0]:
                print("Round " + str(x+1) + ":", chand, verb[1], hand, "sorry. Try again.")
            else:
                print("Round " + str(x+1) + ":", chand, verb[7], hand, "sorry. Try again.")
            cScore += 1
        elif chand == hands[2] and hand == hands[1] or chand == hands[2] and hand == hands[3]:
            if hand == hands[1]:
                print("Round " + str(x+1) + ":", chand, verb[0], hand, "sorry. Try again.")
            else:
                print("Round " + str(x+1) + ":", chand, verb[5], hand, "sorry. Try again.")
            cScore += 1
        elif chand == hands[3] and hand == hands[1] or chand == hands[3] and hand == hands[4]:
            if hand == hands[1]:
                print("Round " + str(x+1) + ":", chand, verb[6], hand, "sorry. Try again.")
            else:
                print("Round " + str(x+1) + ":", chand, verb[3], hand, "sorry. Try again.")
            cScore += 1
        elif chand == hands[4] and hand == hands[0] or chand == hands[4] and hand == hands[2]:
            if hand == hands[0]:
                print("Round " + str(x+1) + ":", chand, verb[8], hand, "sorry. Try again.")
            else:
                print("Round " + str(x+1) + ":", chand, verb[4], hand, "sorry. Try again.")
            cScore += 1
        else:
            print("Round " + str(x+1) + ":", hand, "beats", chand, "Congratulations! You Win.")
            pScore += 1

    score(pScore,cScore)

def score(pScore,cScore):
    if pScore > cScore:
        w = """
            ------------------------
            Winner! Congratulations!
            ------------------------
            """
    elif pScore == cScore:
        w = """
            ----------------
            Draw! Well done.
            ----------------
            """
    else:
        w = """
            ----------------------
            Better luck next time.
            ----------------------
            """
    print("\nPlayer scored:", pScore,"\nComputer scored", cScore, "\n"+w)

def rematchplz():
    global rematch
    rematchChoice = input("""
    -------------------------------
     Would you like to play again?
     'y' for Yes, any key for No:
    -------------------------------
    """)
    if rematchChoice.lower() != "y":
        rematch = False

def game():
    print("""
    --------------------------------------------------------------------------------------------
    let\'s play a game! Please type in the name of the game you wish to play from the list below:
    --------------------------------------------------------------------------------------------
    """)

    for games in gameList:
        print("""
        -------------------
        """,
        games, 
        """
        -------------------
        """, end="")

    gameChoice = cleanup(input("\n"))
    print("****************          ", gameChoice)

    try:
        if gameChoice in gameList or gameChoice in gameList_hidden:
            if gameChoice == "diceroll" or gameChoice == "dice" or gameChoice == "roll":
                diceroll()
            elif gameChoice == "coinflip" or gameChoice == "coin" or gameChoice == "flip":
                coinflip()
            elif gameChoice == "rpsls":
                rpsls()
            elif gameChoice == "rockpaperscissors" or "rps":
                rockpaperscissors()
        else:
            raise gameerr
        
        rematchplz()

    except dicerollerr:
        print("""
        --------------------------------------------------
        That was not a valid number, try 12 or 20 perhaps.
        --------------------------------------------------
        """)
    except coinfliperr:
        print("""
        ------------------------------------------------------------------------------------------------------------------------------
        This coin only has heads or tails, please choose one and go back to making whatever bad decision it was you were flipping for.
        ------------------------------------------------------------------------------------------------------------------------------
        """)
    except rockpaperscissorserr:
        print("""
        -------------------------------------------------------------------------------------
        Your choices were Rock, Paper or Scissors... unless you're playing RPSLS with Sheldon
        -------------------------------------------------------------------------------------
        """)
    except gameerr:
        print("""
        ---------------------------------------------------------------------
        Your choice was not in the list of available games. Please Try again!
        ---------------------------------------------------------------------
        """)
    except Exception as e:
        print(e)

rematch = True
while rematch == True:
    game()