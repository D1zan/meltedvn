define e = Character("Elsoul")
define a = Character("Anina")
define n = Character("Narrator")
define o = Character("Oskar")
define p = Character("parents")
define gui.text_size = 28

# The game starts here.
label start:

    scene bg snowy forest:
        size(1920,1080)        
       
    show anna
    e "Anina, where are you?"
    #Players can choose whether to answer or not
    #Not answering would lead players to go back to sleep and wake up with anna being dead

    menu:
        "Should elsoul go with anina?"

        "Yes":
            jump go_with_anina

        "No":
            jump no_go_anina

    #"fake sleep.": if yes_sleep

    # "Go with Anina": if no_sleep

    #Anina and Elsoul are playing in their rooms at night 
    #They walk towards their living room to play with elsouls sn
    # This ends the game.


label go_with_anina:

    e "im right behind you silly"
    a " Ok let me make snow piles so we can jump on it "
    e "I'll jump while you make them"
    n "Elsoul is going quite fast, someone might get hurt"

    menu:
        "Anina is struggling to catch up to Elsoul. Stop or continue playing"

        "continue playing":
            jump go_anina

        "Stop":
            jump no_anina
    return
    #Renpy reads the script top to bottom, if a return isn't placed the options yes and no would both print 

label no_go_anina:

    e "ZZZZZZZZZZZ"
    "The Next Day "
    e "Arugh, Good morning eveybody"
    e "wait, where's anina "
    p "Anina is dead sweetheart"

    return

label go_anina:
    n "anina hits elsoul with an icicle"
    a "Oh no what did I do"
