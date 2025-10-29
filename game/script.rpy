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

    # Initialize battle stats
    $ player_max_hp = 100
    if gear == "slime":
        $ player_max_hp = 80  # Vulnerable
    elif gear == "repaired":
        $ player_max_hp = 120  # Sturdy
    $ player_hp = player_max_hp
    $ enemy_hp = 150
    $ battle_log = []
    $ player_defending = False

    # Battle loop
    while player_hp > 0 and enemy_hp > 0:
        show screen battle_screen
        $ action = ui.interact()

        if action == "attack":
            $ damage = renpy.random.randint(20, 40)
            if gear == "well_made":
                $ damage += 10
            $ enemy_hp -= damage
            $ battle_log.append("You attack for [damage] damage!")
        elif action == "defend":
            $ player_defending = True
            $ battle_log.append("You defend, reducing damage next turn.")
        elif action == "potion":
            $ damage = 30
            if gear == "slime":
                $ damage -= 10  # Slippery
            $ enemy_hp -= damage
            $ battle_log.append("You throw a potion for [damage] damage!")
        elif action == "flee":
            $ battle_log.append("You flee the battle!")
            jump flee_ending

        # Enemy turn
        if enemy_hp > 0:
            $ enemy_damage = renpy.random.randint(15, 30)
            if player_defending:
                $ enemy_damage //= 2
                $ player_defending = False
            if gear == "repaired":
                $ enemy_damage -= 5
            $ player_hp -= enemy_damage
            $ battle_log.append("The Eldritch Horror attacks for [enemy_damage] damage!")

    hide screen battle_screen

    if player_hp <= 0:
        jump defeat_ending
    else:
        jump victory_ending



label decline_quest:

    adventurer "Sorry, I'm not interested."

    townsfolk "Suit yourself. Safe travels."

    "You leave town without adventure."

    return

label victory_ending:

    "You have defeated the Eldritch Horror!"

    if gear == "slime":
        "Despite your armor dissolving, you stand victorious."
    elif gear == "repaired":
        "Your sturdy armor held, and the town cheers your bravery."
    else:
        "Your well-made armor shines, and you are hailed as a legend."

    "You return to town as a hero."

    return

label defeat_ending:

    "The Eldritch Horror overwhelms you. You fall in the sewers."

    "But wait, a townsfolk finds you and drags you back. You live to fight another day."

    "You return to town defeated but alive."

    return

label flee_ending:

    "You flee from the battle, leaving the sewers behind."

    "The town is disappointed, but you survive."

    return

screen battle_screen:
    # Background
    add Solid("#000000")  # Black background for JRPG feel

    # Top: HP Bars
    frame:
        xalign 0.5
        yalign 0.05
        background Solid("#333333")
        padding (20, 10)
        hbox:
            spacing 50
            vbox:
                text "[player_name]" color "#FFFFFF" size 24
                bar value player_hp range player_max_hp xmaximum 300 ysize 20
                text "HP: [player_hp]/[player_max_hp]" color "#FFFFFF" size 18
            vbox:
                text "Eldritch Horror" color "#FF0000" size 24
                bar value enemy_hp range 150 xmaximum 300 ysize 20
                text "HP: [enemy_hp]/150" color "#FFFFFF" size 18

    # Center: Battle Title
    text "Battle!" xalign 0.5 yalign 0.3 size 48 color "#FFFF00"

    # Bottom: Command Buttons
    frame:
        xalign 0.5
        yalign 0.9
        background Solid("#444444")
        padding (20, 10)
        hbox:
            spacing 20
            textbutton "Attack" action Return("attack") text_size 24
            textbutton "Defend" action Return("defend") text_size 24
            textbutton "Potion" action Return("potion") text_size 24
            textbutton "Flee" action Return("flee") text_size 24

    # Message Window: Bottom overlay
    frame:
        xalign 0.5
        yalign 0.7
        background Solid("#222222")
        padding (20, 10)
        xmaximum 800
        ymaximum 150
        viewport:
            scrollbars "vertical"
            mousewheel True
            vbox:
                for log_entry in battle_log[-5:]:
                    text log_entry color "#FFFFFF" size 20