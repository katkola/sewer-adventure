# Declare characters used by this game.
define adventurer = Character("[player_name]")
define townsfolk = Character("Townsfolk")
define monster = Character("Eldritch Horror")

# The game starts here.
label start:

    $ player_name = renpy.input("What is your name, adventurer?")

    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name = "Adventurer"

    "You are [player_name], a new adventurer arriving in the town of Eldridge."

    "The town seems quiet, but rumors of monsters in the sewers have been spreading."

    "As you enter the town square, a townsfolk approaches you."

    townsfolk "Hey there, stranger! You look like someone who can handle trouble."

    townsfolk "The sewers are infested with a terrible monster. Can you help us?"

    menu:
        "Accept the quest":
            jump accept_quest
        "Decline and leave town":
            jump decline_quest

label accept_quest:

    adventurer "I'll take care of it."

    townsfolk "Great! But you might want to get some proper gear first. The sewers are dangerous."

    "You head into the town square to find equipment."

    "You see several options: a flashy slime store, the smith's workshop, or a dark alley."

    menu:
        "Visit the flashy slime store":
            jump slime_store
        "Go to the smith's workshop":
            jump smith_workshop
        "Explore the dark alley":
            jump dark_alley

label slime_store:

    "You enter the flashy slime store. The walls are covered in glowing slime displays."

    "A charming salesperson with slick hair greets you."

    define salesperson = Character("Slime Salesperson")

    salesperson "Welcome! Our slime armor is the latest in fashion and protection!"

    "You buy the slime armor. It's lightweight and slippery, great for stealth but dissolves in acid."

    $ gear = "slime"

    jump to_sewers

label smith_workshop:

    "You enter the smith's workshop. The air is hot from the forge."

    "A charming smith with a muscular build and kind eyes welcomes you."

    define smith = Character("Armorsmith")

    smith "Ah, an adventurer! Let me show you my finest work."

    "You purchase well-made armor. It's balanced, protective, and reliable."

    $ gear = "well_made"

    jump to_sewers

label dark_alley:

    "You venture down the dark alley. It's littered with trash, but you spot useful scraps."

    "A charming scavenger with a mischievous grin approaches."

    define scavenger = Character("Scavenger")

    scavenger "Looking for gear? I can help you patch something up from this junk."

    "You repair makeshift armor from the trash. It's sturdy for direct combat but noisy."

    $ gear = "repaired"

    jump to_sewers

label to_sewers:

    "Inside the sewers, it's dark and damp. You hear a growl in the distance."

    "You come across an ancient inscription on the wall: 'To proceed, answer me this: I am not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?'"

    menu:
        "Fire":
            "Correct! The inscription glows, and a hidden door opens."
            jump monster_encounter
        "Plant":
            "Wrong. The wall rumbles, but you can try again."
            jump to_sewers
        "Wind":
            "Wrong. The wall rumbles, but you can try again."
            jump to_sewers

label monster_encounter:

    "Beyond the door, you spot the monster ahead. It's an eldritch horror, a twisted abomination formed from the discarded waste of cheap slime armor carelessly thrown away, pulsing with unnatural, corrosive energy."

    if gear == "slime":
        "Your slime armor glistens in the dim light, making you feel agile but vulnerable to acid."
    elif gear == "repaired":
        "Your patched armor creaks as you move, sturdy but potentially noisy."
    else:
        "Your well-made armor feels comfortable and protective."

    menu:
        "Charge in with your sword":
            jump charge_attack
        "Sneak up quietly":
            jump sneak_attack
        "Use a potion":
            jump potion_attack

label charge_attack:

    "You charge at the monster!"

    monster "A guttural, echoing screech fills the air!"

    if gear == "slime":
        "Your slime armor dissolves quickly under the monster's acid, and you take heavy damage but manage to defeat it."
        "You return to town wounded but victorious."
    elif gear == "repaired":
        "Your sturdy repaired armor absorbs the blows, and you defeat the monster with ease."
        "You return to town as a hero, your armor battered but intact."
    else:
        "Your well-made armor protects you perfectly, and you defeat the monster efficiently."
        "You return to town looking pristine and heroic."

    return

label sneak_attack:

    "You sneak up and strike from behind."

    if gear == "slime":
        "Your slippery slime armor lets you move silently and strike precisely."
        "You defeat the monster without it noticing."
        "You return to town stealthily, avoiding any attention."
    elif gear == "repaired":
        "Your creaky armor makes a noise, alerting the monster slightly, but you still defeat it."
        "You return to town with some scratches."
    else:
        "Your well-made armor allows smooth movement, and you defeat the monster cleanly."
        "You return to town admired for your skill."

    return

label potion_attack:

    "You throw a potion at the monster."

    if gear == "slime":
        "The slime armor's slick surface makes you slip during the throw, but the potion still hits."
        "The monster is confused, and you defeat it, though you injure yourself slipping."
        "You return to town limping but successful."
    elif gear == "repaired":
        "Your repaired armor is steady, and the potion explodes perfectly."
        "You defeat the monster cleverly."
        "The town praises your ingenuity."
    else:
        "Your well-made armor provides perfect balance for the throw."
        "The potion works flawlessly, and you defeat the monster effortlessly."
        "You return as the town's greatest hero."

    return

label decline_quest:

    adventurer "Sorry, I'm not interested."

    townsfolk "Suit yourself. Safe travels."

    "You leave town without adventure."

    return