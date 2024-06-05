﻿define e = Character("Elsoul", who_color="#ffffff")
define a = Character("Anina", who_color="#008000")
define n = Character("Narrator", who_color="#ff0000")
define o = Character("Oskar", who_color="#7fffd4")
define p = Character("Parents", who_color= "#800080")
define gui.text_size = 28
define config.name = _('Melted')


# The game starts here.
label start:

    scene bg snowy living room:
        size(1920,1080)        
       
    show anna
    a "Elsoul, can we practice your powers a little?"

    #Players can choose whether to answer or not
    #Not answering would lead players to go back to sleep and wake up with anina being dead

    menu:
        "Should elsoul wake up and go with anina?"

        "Wake up":
            jump go_with_anina

        "Continue sleeping":
            jump no_go_anina

    #"fake sleep.": if yes_sleep

    # "Go with Anina": if no_sleep

    #Anina and Elsoul are playing in their rooms at night 
    #They walk towards their living room to play with elsouls sn
    # This ends the game.


label go_with_anina:
    scene bg young elsoul:
        size(1920,1080)
    a "Im scared we will get hurt"

    e "Don't worry, I'll be your supervisor. Let's see what you've got!"

    e "We can make castles and have fun"

    menu:
        "This is a dangerous choice. Stop or continue playing:"

        "continue playing":
            jump go_anina

        "Stop":
            jump go_anina
    return
    #Renpy reads the script top to bottom, if a return isn't placed the options yes and no would both print 

label no_go_anina:
    e "ZZZZZZZZZZZ"

    e "Arugh, Good morning eveybody"

    e "wait, where's anina "

    p "Anina is dead sweetheart"

    e "How?? What happened"

    n "Anina unfortunately died because she froke her own body to death in her sleep"

    return

label go_anina:
    e "Whoa, Anina, your ice powers are amazing! Look at this icy blast!"

    a "Thanks, Elsoul! It's so fun to play with you like this. Let's make a big ice castle!"

    e "Yeah! This is gonna be the best castle ever! But be careful with your ice powers, Anina. Mom said we can't make a mess in the living room."

    a "Don't worry, I'll be super careful. Oops! Uh-oh, did I shoot too fast?"

    e "Anina, look out!"

    a "Oh no, Elsoul! I'm so sorry! Are you okay?"

    e "gasp Anina, I-I can't...I'm falling.."

    a "No, no, no! Elsoul, hold on! I didn't mean to! Mom! Dad! Help!"

    menu:
        "Elsoul got hurt, anina will be blamed:"
        "Run":
            jump ran_away
        "Stay":
            jump run_away 
    return


label ran_away:
    a "I need to leave"
    p "You better not "
    n "Anina runs out of their house "
    a "I have to go away"
    n "Anina is out of her house far in the forest"
    o "Hi who are you"
    a "Im anina "
    "10 years go by"
    #Anina goes off to make a house in the forest
    a "I love living here"
    n "Elsoul shoots Anina"
    a "What are you doing here, i thought you were dead "
    

    return
label run_away:
    a "I'm sorry Elsoul "
    p "Now we have to kill you, your a disgrace to this family"
    a "WHAT I AM YOUR DAUGHTER"
    p "Not anymore"
    n "Parents find a knife and chase anina around their house"