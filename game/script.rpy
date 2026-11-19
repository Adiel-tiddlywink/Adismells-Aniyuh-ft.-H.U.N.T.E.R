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
$ user = renpy.input("LISTENING...",exclude="0123456789!@#$%^&*()_+-=|;':\",./<>?")
    # If the player left it completely blank, set it to Vanessa
if not user:
    $ user = "Vanessa"

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

h "So, do you have any questions?"

label questioning:

menu:
    "What's the weather like in 'town'?":
        h ""
        
    "What should our meal plans be for today?":
        h ""

    "What's happening in 'town'?":
        h ""

    "Verity?":
        window hide
        show verityewwwww:
            xpos 0.0
            ypos 0.0
            xysize(1920,1080)
            alpha 0.0
            linear 0.5 alpha 1.0

h "Oops... wrong file."
hide verityewwwww

# keeps game from closing
$ renpy.pause(hard=True)