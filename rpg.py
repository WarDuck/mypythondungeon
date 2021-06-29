import sys, random

health = 100
weapon = "knife"

def combat(enemy):
    global health
    global grid_enemies

    stamina = 100
    if weapon == "knife":
        attack = 5
    defense = 10
    
    if enemy == "walking corpse":
        enemy_health = 40
        enemy_defense = 10
        enemy_attack = 0
    elif enemy == "skeleton":
        enemy_health = 20
        enemy_defense = 15
        enemy_attack = 5
    elif enemy == "troll":
        enemy_health = 80
        enemy_defense = 20
        enemy_attack = 10
    elif enemy == "minotaur":
        enemy_health = 100
        enemy_defense = 25
        enemy_attack = 15
        
    print ("In combat with", enemy, "!")
    
    while enemy_health > 0 and health > 0:
        print ("*dev* Enemy attack:", enemy_attack)
        print ("*dev* Enemy defense:", enemy_defense)
        print ("Your stamina:", stamina)
        print ("Your health: ", health)
        print ("Enemy health: ", enemy_health)
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
            attack_roll = random.randint(1,20) + attack
            print("Your attack is:", attack_roll)
            if attack_roll >= enemy_defense:
                damage = random.randint(5,10)
                print("You hit and do", damage, "amount of damage")
                enemy_health -= damage
            else:
                print("The",enemy,"blocked your attack.")
        elif action == "B":
            if stamina >= 40:
                attack_roll = random.randint(1,20) + attack
                stamina -= 40
                print("Your attack is:", attack_roll)
                if attack_roll >= enemy_defense:
                    damage = random.randint(5,10) * 2
                    print("You hit and do", damage, "amount of damage")
                    enemy_health -= damage
                    
                else:
                    print("Enemy blocked your attack.")
            else:
                print ("Not enough stamina")
        elif action == "C":
            if stamina >= 30:
                attack_roll = random.randint(1,20) + attack
                stamina -= 30
                print("Your attack is:", attack_roll)
                if attack_roll >= enemy_defense:
                    print("You hit and lower the enemy's defense by 5")
                    enemy_defense -= 5
                else:
                    print("Enemy did not fall for your feint.")
            else:
                print("Not enough stamina")
        elif action == "X":
            sys.exit(0)
                
            
        enemy_attack_roll = random.randint(1,20) + enemy_attack
        if enemy_attack_roll >= defense:
            enemy_damage = random.randint(5,10)
            print ("Enemy strikes you and deals", enemy_damage, "damage")
            health -= enemy_damage
        else:
            print("You blocked the enemy attack.")
        
    if health <= 0:
        print ("yo deaaad!")
        
    if enemy_health <= 0:
        print ("you slaughtered!")
        grid_enemies[y_position][x_position]=""

grid_items = [
["","","","","","","","","",""],
["","","","","","","","","",""],
["","","","","","","","","",""],
["","","","","","","","","",""],
["","","","","","","","","",""],
["","","","","","","","","",""],
["","","","","","","","","",""],
["","","","","","","","","",""],
["","","","","","","","","",""],
["","","","","","","","","",""]
]

grid_enemies = [
["","","","troll","","","","","","walking corpse"],
["minotaur","","","","","walking corpse","","","skeleton",""],
["","","","","","","","","","" ],
["","","skeleton","","","","","","","" ],
["","","","","skeleton","","walking corpse","","",""  ],
["","","","walking corpse","","","","","","walking corpse" ],
["skeleton","","","","","skeleton","","","","" ],
["","walking corpse","","","","","","","","" ],
["skeleton","","","skeleton","","","","","","" ],
["","","","skeleton","","","","","skeleton","" ]
]


x_position = 7
y_position = 9
grid_options = [
[["C","X"],    ["B","C","X"],    ["B","D","X"],        ["B","D","X"],        ["D","X"],        ["B","C","X"],    ["C","D","X"],["B","C","X"],    ["C","D","X"],    ["C","X"]        ],
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

print ("welcome to patriks rpg version 0.2!")

while True:
    print ("Your health: ", health)
    print("What do you want to do?")
    for option in grid_options[y_position][x_position]:
        if option == "A":
            print("A to go north")
        elif option == "B":
            print("B to go east")
        elif option == "C":
            print("C to go south")
        elif option == "D":
            print("D to go west")
        elif option == "E":
            print("E to drink from fountain")
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
        health = 100
    elif action == "X":
        sys.exit(0)

    print ("*dev* You are at:", x_position,",", y_position)

    if grid_enemies[y_position][x_position]:
        combat(grid_enemies[y_position][x_position])
        
    if health <= 0:
        print ("game over!")
        sys.exit(0)
