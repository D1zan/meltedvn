define e = Character("Elsoul", who_color="#ffffff")
define a = Character("Anina", who_color="#008000")
define n = Character("Narrator", who_color="#ff0000")
define o = Character("Oskar", who_color="#7fffd4")
define p = Character("Parents", who_color= "#800080")
define l = Character("Police", who_color= "#080437")
define gui.text_size = 28
define config.name = ('Melted')
#Game starts here 
label start:

# scene bg snowy living room:
#size(1920,1080)        
       
    show anna
    a "Elsoul, can we practice my powers a little?"

    #Players can choose whether to answer or not
    #Not answering would lead players to go back to sleep and wake up with anina being dead

    menu:
        "Should elsoul wake up and go with anina?"

        "Wake up":
            jump go_with_anina

        "Continue sleeping":
            jump no_go_anina


label go_with_anina:
    #scene bg young elsoul:
#   size(1920,1080)
    a "Im scared we will get hurt"

    e "Don't worry, I'll supervise. Let's see what you've got!"

    e "We can make castles and have fun"

    menu:
        "Both are dangerous choices:"

        "continue playing with castles":
            jump go_anina

        "Make snow angels":
            jump go_anina
    return
    #Renpy reads the script top to bottom, if a return isn't placed the options yes and no would both print 

label no_go_anina:
    e "ZZZZZZZZZZZ"

    p "Elsoul wake up, where is your sister?"

    e "im not sure, I've been sleeping."

    
return

label go_anina:
    e "Whoa, Anina, your ice powers are amazing! Look at this icy blast!"

    a "Thanks, Elsoul! It's so fun to play with you like this!"

    e "Yeah! This is gonna be the best night ever! But be careful with your ice powers, Anina. Mom said we can't make a mess in the living room."

    a "Don't worry, I'll be super careful. Oops! Uh-oh, did I shoot too fast?"

    e "Anina!"

    a "Oh no, Elsoul! I'm so sorry! Are you okay?"

    e "gasp Anina, I-I can't..breathe...."

    a "No, no, no! Elsoul, hold on! I didn't mean to! Mom! Dad! Help!"

    menu:
        "Elsoul got hurt, anina will be blamed:"
        "Run away":
            jump ran_away
        "Stay":
            jump run_away 
    return


label ran_away:
    a "I need to leave."

    p "You better not!!"

    n "Anina runs out of their house. "

    a "I have to go. "

    n "Anina is out of her house far in the forest."

    o "Hi who are you?"

    a "Im anina. "

    "10 years go by"
    #Anina goes off to make a house in the forest
    a "I love living here."

    n "Elsoul shoots Anina."

    a "What are you doing here, i thought you were dead. "
    

    return
label run_away:
    a "I'm sorry Elsoul. "

    p "Now we have to kill you, your a disgrace to this family."

    a "WHAT? I AM YOUR DAUGHTER."

    p "Not anymore."

    n "Parents find a knife and chase anina around their house."

    menu: 
        "Anina now has to hide"
        "Hide in her room":
            jump hide_bed
        "Hide under the stairs":
            jump hide_stairs
    return

label hide_bed:
    n "Anina is now under her bed."

    a "I did not know I had all of this stuff under here."

    p "Anina, where are youu...."

    a "Woah, I can't believe I have this knife from elsoul under my bed. I can use it."

    n "Anina's parents are in the kitchen, nowhere near her rooom."

    a "Maybe I have a chance to survive if I build a fort behind my door."

    n "Anina piles furniture behind her bedroom door."

label hide_stairs:
    n "Anina is now under the stairs."

    p "Anina where are youuu...."

    "Her parents are walking on the stairs, on top of Anina."

    a "Hopefully they won't find me here."

    p "We will find you and kill you."

    "Anina's parents fall through the steps."

    p "Ha found you."

    "Her parents found her."

    a "No please don't kill me, I love you."

    p "Too bad."

    "Anina is killed."
