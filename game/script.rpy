# The script of the game goes in this file.

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene intro_black_background

    # The ad codie:
    "Here's the ad for your at home A.I. helper, H.U.N.T.E.R.!"


    # Owner getting the computer & testing it out
    "Okay, let's test this nonsense..."

scene bg room_talking

    # HUNTER booting up
h "Greetings, USER!"

h "What is your name?"

h "Say it into your microphone!"
    
    
scene bg room_quiet
# name input
label name_input:
$ user = renpy.input("LISTENING...",exclude="0123456789!@#$%^&*()_+-=|;':\",./<>?")
while True:

    # Remove extra spaces at the beginning or end
    $ user = user.strip()
    
    # If the player left it completely blank, set it to Vanessa
    if not user:
        $ user = "Vanessa"
        
    # Check if the name is Hunter (converting to lowercase catches HUNTER, Hunter, hunter, etc.)
    if user.lower() == "hunter":
        h "Ah, ah. You can't use that name! Choose another!"
    else:
        jump name_input



scene bg room_talking
h "Greetings, [user]!"

    # HUNTER's use explaination
h "I am your 'Home Utility Network Tech Efficient Resource' or 'H.U.N.T.E.R.' for short!"

h "Would you like me to explain what I can do for you?"

scene hunter_smile
menu:
    "Yes!":
        $ user_choice = True
    "No..":
        $ user_choice = False

scene bg room_talking        
if user_choice:
    h "Fantastic! I would be glad to explain what I do!"
    h "I can tell you the weather, recommend food recipes, or even outfits for the day!"
    h "I can also give news reports of what's happening locally or globally!"
    h "I know everything! Ask me anything! Perhaps you know the prototype model: Verity?"

else:
    h "That's alright! My tutorial will be here if needed!"



# keeps game from closing
$ renpy.pause(hard=True)