define e = Character("Elsoul", who_color="#ffffff")
define a = Character("Anina", who_color="#008000")
define n = Character("Narrator", who_color="#ff0000")
define o = Character("Oskar", who_color="#7fffd4")
define p = Character("Parents", who_color= "#800080")
define gui.text_size = 28

# The game starts here.
label start:

    scene bg snowy forest:
        size(1920,1080)        
       
    show anna
    a "Elsoul, can we practice your powers a little?"

    #Players can choose whether to answer or not
    #Not answering would lead players to go back to sleep and wake up with anina being dead

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
    a "Im scared we will get hurt"

    e "Don't worry, I'll be your supervisor. Let's see what you've got!"

    e "I'll jump while you make snow mountains"

    n "Elsoul is jumping quite fast, someone might get hurt"



    menu:
        "Anina is struggling to catch up to Elsoul. Stop or continue playing"

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

    P "WHAT DID YOU DO!!!"

   
   
   
    menu:
        "Anina's parents will ground her for the rest of her life"

        "Run away":
            jump ran_away

        "Stay":
            jump run_away 
    return


label ran_away:
    a "IM out of here"

label run_away:
    a "im never leaving "