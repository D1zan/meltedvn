define e = Character("Elsoul", who_color="#ffffff")
define a = Character("Anina", who_color="#008000")
define n = Character("Narrator", who_color="#ff0000")
define o = Character("Oskar", who_color="#7fffd4")
define p = Character("parents", who_color= "#800080")
define gui.text_size = 28

# The game starts here.
label start:

    scene bg snowy forest:
        size(1920,1080)        
       
    show anna
    a "Elsoul, where are you?"
    #Players can choose whether to answer or not
    #Not answering would lead players to go back to sleep and wake up with anna being dead

    menu:
        "Should elsoul wake up and go with anina?"

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
    scene bg young elsoul:
        size(1920,1080)
    e "im right behind you silly"
    a "Oo you scared me, please play with me in the living room "
    e "I'll jump while you make snow mountains"
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
