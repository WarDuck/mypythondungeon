import sys, random


class Skeleton:
    name = "Skeleton"
    description = "You come across a skeleton! it is decrepit, bearly holding togehter. Still, it is armed with a rusty sword and shield. Better be careful!"
    health = 20
    defense = 15
    attack = 5
    damage = 5

class WalkingCorpse:
    name = "Walking Corpse"
    description = "A walking corpse shambles towards you! it moves slowly but the foul magic powering it gives it unnatural strenght."
    health = 40
    defense = 10
    attack = 0
    damage = 5

class Troll:
    name = "Troll"
    description = "You hear a thunderous roar followed by heavy footsteps. Out from the dark corridor ahead you suddenly see a Dungeon Troll stompping towards you, wielding a club almost as large as you are. With a loud grunt it attacks you!"
    health = 80
    defense = 18
    attack = 10
    damage = 5

class Minotaur:
    name = "Minotaur"
    description = "Suddenly the floor starts to shake. The pounding gets heavier and heavier and the shaking gets so violent dust and pebbles start to fall from the ceiling. You start to hear the breathing of something that must be enormuous, much larger then the Dungeon Troll you encountered earlier. Panic grips you as you start to see something making it's way towards you from the corridor ahead. You grab hold of your weapon and ready yourself. The beast comes in to view. Before you stands to largest, most vicious looking beast you've ever seen: The MINOTAUR! Towering at the length of two men, it has the body of a giant and the head of a bull with glowing red eyes. It wields a double bladed axe so huge, the shaft could easily be used as a batterning ram. It gives the loudest roar ever heard by man and marches towards you!"
    health = 100
    defense = 23
    attack = 15
    damage = 5


class Knife:
    name = "Knife"
    type = "weapon"
    description = "The knife is the only weapon allowed to the lower classes. It is not much but you can make do."
    attack = 5
    damage = 5

class ShortSword:
    name = "Short Sword"
    type = "weapon"
    description = "The short sword is the standard weapon asigned to the army conscripts and city militia."
    attack = 10
    damage = 7

class Axe:
    name = "Axe"
    type = "weapon"
    description = "The axe not considered a weapon at all but a tool, but in the hands of the right person it can do a lot of damage"
    attack = 8
    damage = 10

class Warhammer:
    name = "Warhammer"
    type = "weapon"
    description = "The warhammer is a devastating weapon, in many cases capable of destroying a foe in a single blow"
    attack = 4
    damage = 20

class LongSword:
    name = "Long Sword"
    type = "weapon"
    description = "The long sword is the tool of a master swordsman. It's finesse let's it strike home where other weapons would miss. Luckily your know something of it's use"
    attack = 17
    damage = 8


class Shirt:
    name = "Shirt"
    type = "armor"
    description = "A commoners shirt. with this as your armor, your best bet is to rely on evasion"
    defense = 10

class LeatherArmor:
    name = "Leather Armor"
    type = "armor"
    description = "Lether armor is what is worn by the conscripted masses of Karrahun's armies"
    defense = 13

class ScaleMail:
    name = "Scale Mail"
    type = "armor"
    description = "Scale mail is the high end. It is reserved for army officers and the noble's personal guards."
    defense = 16

class FullPlate:
    name = "Full Plate"
    type = "armor"
    description = "Full plate is the arnor of a noble. How strange to find such a thing here. Maybe the torments of the labyrinth are not reserved only for the poor?"
    defense = 20

class Key:
    name = "Key"
    type = "key"


class Player:
    health = 100
    stamina = 100
    weapon = Knife()
    armor = Shirt()
    pocket = 0

player = Player()


def combat(enemy_string):
    global health
    global grid_enemies

    player.stamina = 100
    
    if enemy_string == "walking corpse":
        enemy = WalkingCorpse()
    elif enemy_string == "skeleton":
        enemy = Skeleton()
    elif enemy_string == "troll":
        enemy = Troll()
    elif enemy_string == "minotaur":
        enemy = Minotaur()
        
    print ( enemy.description )
    
    while enemy.health > 0 and player.health > 0:
        #print ("*dev* Enemy attack:", enemy.attack)
        #print ("*dev* Enemy defense:", enemy.defense)
        print ("Your attack bonus:", player.weapon.attack)
        print ("Your damage bonus:", player.weapon.damage)
        print ("Your defense:", player.armor.defense)
        print ("Your stamina:", player.stamina)
        print ("Your health: ", player.health)
        print ("Enemy health: ", enemy.health)
        print ("Your move!")
        print ("A to attack")
        print ("B to power attack (costs 40 stamina)")
        print ("C to feint (costs 30 stamina)")
        print ("X to exit")
        
        while True:
            action = input()
            if action in ["A","B","C","X"]:
                break
            else:
                print ("invalid action!")
                
        if action == "A":
            attack_roll = random.randint(1,20) + player.weapon.attack
            print("Your attack is:", attack_roll)
            if attack_roll >= enemy.defense:
                damage_roll = random.randint(1,5)+player.weapon.damage
                print("You hit and do", damage_roll, "amount of damage")
                enemy.health -= damage_roll
            else:
                print("The",enemy.name,"blocked your attack.")
        elif action == "B":
            if player.stamina >= 40:
                attack_roll = random.randint(1,20) + player.weapon.attack
                player.stamina -= 40
                print("Your attack is:", attack_roll)
                if attack_roll >= enemy.defense:
                    damage_roll = (random.randint(1,5)+player.weapon.damage) * 2
                    print("You hit and do", damage_roll, "amount of damage")
                    enemy.health -= damage_roll
                    
                else:
                    print("Enemy blocked your attack.")
            else:
                print ("Not enough stamina")
        elif action == "C":
            if player.stamina >= 30:
                attack_roll = random.randint(1,20) + player.weapon.attack
                player.stamina -= 30
                print("Your attack is:", attack_roll)
                if attack_roll >= enemy.defense:
                    print("Your hit and lower the enemy's defense by 5")
                    enemy.defense -= 5
                else:
                    print("Enemy did not fall for your feint.")
            else:
                print("Not enough stamina")
        elif action == "X":
            sys.exit(0)
                
            
        enemy_attack_roll = random.randint(1,20) + enemy.attack
        if enemy_attack_roll >= player.armor.defense:
            enemy_damage_roll = random.randint(1,5)+enemy.damage
            print ("Enemy strikes you and deals", enemy_damage_roll, "damage")
            player.health -= enemy_damage_roll
        else:
            print("You blocked the enemy attack.")
        
    if player.health <= 0:
        print ("DARK SOULS HAS GOT NOTHING ON ME!")
        
    if enemy.health <= 0:
        print ("you slaughtered!")
        grid_enemies[y_position][x_position]=""

grid_items = [
["","","","","Key","","","","","Warhammer"],
["","","","","","","","","Scale Mail",""],
["","","","","","","","","",""],
["","","","","","","","","",""],
["","","","","","","","","",""],
["","","","","","","","","","Short Sword"],
["","","","","","","","","",""],
["","","","","","","","","",""],
["Full Plate","","","","","","","","",""],
["Long Sword","","","","","","","","Leather Armor",""]
]

grid_enemies = [
["","","","troll","","","","","skeleton",""],
["","","","","","walking corpse","","","","walking corpse"],
["","","","","","","","","","" ],
["","","skeleton","","","","","","","" ],
["","","","","skeleton","","walking corpse","","",""  ],
["","","","walking corpse","","","","","","" ],
["skeleton","","","","","skeleton","","","","walking corpse" ],
["skeleton","walking corpse","","","","","","","","" ],
["","","","skeleton","","","","","","" ],
["","","","skeleton","","","","","","skeleton" ]
]

grid_options = [
[["C","X","F"],    ["B","C","X"],    ["B","D","X"],        ["B","D","X"],        ["D","X"],        ["B","C","X"],    ["C","D","X"],["B","C","X"],    ["C","D","X"],    ["C","X"]        ],
[["A","C","X"],["A","B","X"],    ["B","D","X"],        ["C","D","X"],        ["C","X"],        ["A","C","X"],    ["A","B","X"],["A","C","D","X"],["A","X"],        ["A","C","X"]    ],
[["A","C","X"],["B","X"],        ["C","D","X"],        ["A","C","X"],        ["A","C","X"],    ["A","C","X"],    ["B","C","X"],["A","B","D","X"],["C","D","X"],    ["A","C","X"]    ],
[["A","C","X"],["C","X"],        ["A","C","X"],        ["A","C","X"],        ["A","C","X"],    ["A","C","X"],    ["A","C","X"],["B","C","X"],    ["A","D","X"],    ["A","C","X"]    ],
[["A","B","X"],["A","C","D","X"],["A","C","X"],        ["A","C","X"],        ["A","B","C","X"],["A","D","X"],    ["A","C","X"],["A","C","X"],    ["B","C","X"],    ["A","D","X"]    ],
[["C","X"],    ["A","B","X"],    ["A","B","C","D","X"],["A","B","C","D","X"],["A","C","D","X"],["B","C","X"],    ["A","D","X"],["A","C","X"],    ["A","C","X"],    ["C","X"]        ],
[["A","B","X"],["B","D","X"],    ["A","D","X"],        ["A","C","X"],        ["A","C","X"],    ["A","B","C","X"],["B","D","X"],["A","C","D","X"],["A","B","C","X"],["A","D","X"]    ],
[["B","C","X"],["B","D","X"],    ["B","D","X"],        ["A","D","X"],        ["A","C","X"],    ["A","C","X"],    ["B","C","X"],["A","C","D","X"],["A","B","X"],    ["C","D","X"]    ],
[["A","X"],    ["B","C","X"],    ["B","D","X"],        ["B","D","X"],        ["A","B","D","X"],["A","D","X"],    ["A","C","X"],["A","B","C","X"],["B","D","X"],    ["A","C","D","X"]],
[["B","X"],    ["A","D","X"],    ["E","B","X"],        ["B","D","X"],        ["B","D","X"],    ["B","D","X"],    ["A","D","X"],["A","X"],        ["B","X"],        ["A","D","X"]    ]
]

grid_story = [
[# row 1
    "You stand at a door",
    "There's a corridor to the east and south",
    "You stand in a east-west corridor",
    "You stand in a east-west corridor",
    "The corridor ends in a stone wall",
    "There's a corridor to the east and south",
    "There's a corridor to the south and west",
    "There's a corridor to the east and south",
    "There's a corridor to the south and west",
    "The corridor ends in a stone wall"
],
[# row 2
    "You stand in a north-south corridor",
    "There's a corridor to the north and east",
    "You stand in a east-west corridor",
    "There's a corridor to the south and west",
    "The corridor ends in a stone wall",
    "You stand in a north-south corridor",
    "There's a corridor to the north and east",
    "You stand in a north-south corridor with a corridor to the west",
    "The corridor ends in a stone wall",
    "You stand in a north-south corridor"
],
[# row 3
    "You stand in a north-south corridor",
    "The corridor ends in a stone wall",
    "There's a corridor to the south and west",
    "You stand in a north-south corridor",
    "You stand in a north-south corridor",
    "You stand in a north-south corridor",
    "There's a corridor to the east and south",
    "You stand in a east-west corridor with a corridor to the north",
    "There's a corridor to the south and west",
    "You stand in a north-south corridor"
],
[# row 4
    "You stand in a north-south corridor",
    "The corridor ends in a stone wall",
    "You stand in a north-south corridor",
    "You stand in a north-south corridor",
    "You stand in a north-south corridor",
    "You stand in a north-south corridor",
    "You stand in a north-south corridor",
    "There's a corridor to the east and south",
    "There's a corridor to the north and west",
    "You stand in a north-south corridor"
],
[# row 5
    "There's a corridor to the north and east",
    "You stand in a north-south corridor with a corridor to the west",
    "You stand in a north-south corridor",
    "You stand in a north-south corridor",
    "You stand in a north-south corridor with a corridor to the east",
    "There's a corridor to the north and west",
    "You stand in a north-south corridor",
    "You stand in a north-south corridor",
    "There's a corridor to the east and south",
    "There's a corridor to the north and west"
],
[# row 6
    "The corridor ends in a stone wall",
    "There's a corridor to the north and east",
    "You stand at a crossroads",
    "You stand at a crossroads",
    "You stand in a north-south corridor with a corridor to the west",
    "There's a corridor to the east and south",
    "There's a corridor to the north and west",
    "You stand in a north-south corridor",
    "You stand in a north-south corridor",
    "The corridor ends in a stone wall"
],
[# row 7
    "There's a corridor to the north and east",
    "You stand in an east-west corridor",
    "There's a corridor to the north and west",
    "You stand in a north-south corridor",
    "You stand in a north-south corridor",
    "You stand in a north-south corridor with a corridor to the east",
    "You stand in a east-west corridor",
    "You stand in a north-south corridor with a corridor to the west",
    "You stand in a north-south corridor with a corridor to the east",
    "There's a corridor to the north and west"
],
[# row 8
    "There's a corridor to the east and south",
    "You stand in an east-west corridor",
    "You stand in an east-west corridor",
    "There's a corridor to the north and west",
    "You stand in a north-south corridor",
    "You stand in a north-south corridor",
    "There's a corridor to the east and south",
    "You stand in a north-south corridor with a corridor to the west",
    "There's a corridor to the north and east",
    "There's a corridor to the south and west"
],
[# row 9
    "The corridor ends in a stone wall",
    "There's a corridor to the east and south",
    "You stand in an east-west corridor",
    "You stand in an east-west corridor",
    "You stand in an east-west corridor with a corridor to the north",
    "There's a corridor to the north and west",
    "You stand in a north-south corridor",
    "You stand in a north-south corridor with a corridor to the east",
    "You stand in an east-west corridor",
    "You stand in a north-south corridor with a corridor to the west"
],
[# row 10
    "The corridor ends in a stone wall",
    "There's a corridor to the north and west",
    "You found a health fountain.",
    "You stand in an east-west corridor",
    "You stand in an east-west corridor",
    "You stand in an east-west corridor",
    "There's a corridor to the north and west",
    "You stand at the the door you entered the labyrinth. The corridor heads north",
    "The corridor ends in a stone wall",
    "There's a corridor to the north and west"
]
]

x_position = 7
y_position = 9

print("\n\nWelcome to The Labyrinth.\n\
From time to time the nobles of the great city \n\
Karrahun get bored. They then often turn to the \n\
poor for sport. One such sport is to throw some \n\
poor soul into The Labyrinth and watch as he \n\
struggles to survive and get out.\n\
Today that unlucky soul is you. You have been \n\
captured and thrown into The Labyrinth with only\n\
the shirt on your back and knife in your hand. \n\
But you are not like your unfortunate predessesors.\n\
You have lived a harder life than most and you know\n\
how to fight to survive. You have no intentions to\n\
die here today.\n\
But beware: the undead remains of those who have\n\
perished in this labyrinth still haunt it, and \n\
legend has it that a mighty Minotaur roams\n\
somewhere in this labyrinth!\n");

def game():
    global x_position
    global y_position
    while True:
        if grid_items[y_position][x_position] != "":
            item_string = grid_items[y_position][x_position]

            if item_string == "Knife":
                item = Knife()
            elif item_string == "Short Sword":
                item = ShortSword()
            elif item_string == "Long Sword":
                item = LongSword()
            elif item_string == "Axe":
                item = Axe()
            elif item_string == "Warhammer":
                item = Warhammer()
            elif item_string == "Shirt":
                item = Shirt()
            elif item_string == "Leather Armor":
                item = LeatherArmor()
            elif item_string == "Scale Mail":
                item = SaleMail()
            elif item_string == "Full Plate":
                item = FullPlate()
            elif item_string == "Key":
                item = Key()

            print("You find a ", item.name)
            print(item.description)
            print("A to pick it up")
            print("B to leave it")

            while True:
                action = input()
                if action in ["A","B"]:
                    break
                else:
                    print ("invalid action!")

            if action == "A":
                if item.type == "weapon":
                    grid_items[y_position][x_position] = player.weapon.name
                    player.weapon = item
                elif item.type == "armor":
                    grid_items[y_position][x_position] = player.armor.name
                    player.armor = item
                elif item.type == "key":
                    player.pocket = item
                    grid_items[y_position][x_position] = ""
                    grid_enemies[1][0] = "minotaur"

        print (grid_story[y_position][x_position])
        print ("Your health: ", player.health)
        print("What do you want to do?")
        for option in grid_options[y_position][x_position]:
            if option == "A":
                print("A to head north")
            elif option == "B":
                print("B to head east")
            elif option == "C":
                print("C to head south")
            elif option == "D":
                print("D to head west")
            elif option == "E":
                print("E to drink from fountain")
            elif option =="F":
                print("F to open door")
            elif option == "X":
                print("X to exit") 


        while True:
            action = input()
            if action in grid_options[y_position][x_position]:
                break
            else:
                print ("invalid action!")

        if action == "A":
            y_position -= 1
        elif action == "B":
            x_position += 1
        elif action == "C":
            y_position += 1
        elif action == "D":
            x_position -= 1
        elif action == "E":
            player.health = 100
        elif action == "F":
            if player.pocket != 0:
                print("You have done it! You re the first to ever escape the \
                labyrinth! Now you have a word or two for the people who put\
                in there in the first place. But wait. What is this? You are\
                surrounded by guards and they do not look happy. They surround\
                you and overwhelm you before you have a chance to do anything.\
                Seems survivng the labyrinth was not part of the plan. Now they\
                drag you of for a quiet execution, but you have survived the\
                labyrinth and you are not about to die now...")
                return
            else:
                print("The door is locked!")
        elif action == "X":
            return

        # print ("*dev* You are at:", x_position,",", y_position)

        if grid_enemies[y_position][x_position]:
            combat(grid_enemies[y_position][x_position])
        
        if player.health <= 0:
            print ("game over!")
            return


game()