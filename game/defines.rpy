define m = Character("Madeline")
define h = Character("H.U.N.T.E.R.", color = "#0ef04e", image="HUNTER_TALKING")
define images = ("intro_black_background.jpg")
define images = ("HUNTER.jpg")
define image = ("HUNTER_NEUTRAL.jpg")
define image = ("HUNTER_SMILE.jpg")
define image = ("HUNTER_ROOM.jpg")
define image = ("HUNTER_OPENMOUTH_A.jpg")
define image = ("HUNTER_OPENMOUTH_B.jpg")
define images = ("verityewwwww.png")

define image = "bg room_quiet" == "HUNTER_SMILE.jpg"

image bg room_talking:
    "HUNTER_OPENMOUTH_A.jpg"
    0.18 # Seconds mouth stays open
    "HUNTER_SMILE.jpg"
    0.18 # Seconds mouth stays closed
    "HUNTER_OPENMOUTH_B.jpg"
    0.18
    "HUNTER_SMILE.jpg"
    0.18
    "HUNTER_OPENMOUTH_B.jpg"
    0.18
    "HUNTER_OPENMOUTH_A.jpg"
    0.18
    "HUNTER_NEUTRAL.jpg"
    0.18
    repeat

image bg room_quiet:
    "HUNTER_SMILE.jpg"
    0.18 # Seconds mouth stays closed
    repeat