# The script of the game goes in this file.

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene intro_black_background

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    # The ad codie:
    "Here's the ad for your at home A.I. helper, H.U.N.T.E.R.!"


    # Owner getting the computer & testing it out
    "Okay, let's test this nonsense..."

    # HUNTER booting up
    h "Greetings, USER!"

    h "What is your name?"

    h "Say it into your microphone!"
    
    # name input
    $ user = renpy.input("LISTENING...")
    if not user:
        $ user = "Vanessa"

    h "Greetings, [user]!"

    # HUNTER's use explaination
    h "I am your 'Home Utility Network Tech Efficient Resource' or 'H.U.N.T.E.R.' for short!"
    h "Would you like me to explain what I can do for you?"
    

# keeps game from closing
$ renpy.pause(hard=True)

