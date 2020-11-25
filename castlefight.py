import time
import random

#one player user and one computer user
class User:
    def __init__(self, name, faction, health):
        self.name = name
        self.faction = faction
        self.health = health
    def getName(self):
        return self.name
    def getHealth(self):
        return self.health

#four factions available for either player to choose
#factions are purely cosmetic
class Faction:
    def __init__(self, name, rock, paper, scissor):
        self.name = name
        self.rock = rock
        self.paper = paper
        self.scissor = scissor
    def getName(self):
        return self.name

#every faction has a rock, paper, and scissor unit (aka their role)
class Unit:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    def getName(self):
        return self.name
    def getRole(self):
        return self.role

#initialize a human faction
def init_human():
    rock = Unit("Knight", 'r')
    paper = Unit("Pikeman", 'p')
    scissor = Unit("Footman", 's')
    return Faction("Human", rock, paper, scissor)

#initialize an orc faction
def init_orc():
    rock = Unit("Brawler", 'r')
    paper = Unit("Boomer", 'p')
    scissor = Unit("Grunt", 's')
    return Faction("Orc", rock, paper, scissor)

#initialize an elven faction
def init_elven():
    rock = Unit("Guardian", 'r')
    paper = Unit("Assassin", 'p')
    scissor = Unit("Ranger", 's')
    return Faction("Elven", rock, paper, scissor)

#initialize an undead faction
def init_undead():
    rock = Unit("Abomination", 'r')
    paper = Unit("Ghoul", 'p')
    scissor = Unit("Zombie", 's')
    return Faction("Undead", rock, paper, scissor)

#print the combat board 
def print_board(player, computer, player_side, computer_side):
    print("\nPLAYER UNITS: ------------- COMPUTER UNITS: ")
    print("\n#1:" + player_side[0].getName() + " ------------- " + computer_side[0].getName())
    print("\n#2:" + player_side[1].getName() + " ------------- " + computer_side[1].getName())
    print("\n#3:" + player_side[2].getName() + " ------------- " + computer_side[2].getName())
    print("\n#4:" + player_side[3].getName() + " ------------- " + computer_side[3].getName())

#combat between two units is a game of rock, paper, scissors based on each unit's role
def combat(player_unit, computer_unit):
    p = player_unit.getRole()
    c = computer_unit.getRole()
    pName = player_unit.getName()
    cName = computer_unit.getName()
    if p == 'r':
        if c == 'r':
            print("\nYour " + pName + " and the enemy " + cName + " kill each other!")
            return 0
        elif c == 'p':
            print("\nYour " + pName + " is killed by the enemy " + cName + "!")
            return -1
        elif c == 's':
            print("\nYour " + pName + " kills the enemy " + cName + "!")
            return 1
    elif p == 'p':
        if c == 'r':
            print("\nYour " + pName + " kills the enemy " + cName + "!")
            return 1
        elif c == 'p':
            print("\nThe " + pName + " and the " + cName + " kill each other!")
            return 0
        elif c == 's':
            print("\nYour " + pName + " is killed by the enemy " + cName + "!")
            return -1
    elif p == 's':
        if c == 'r':
            print("\nYour " + pName + " is killed by the enemy " + cName + "!")
            return -1
        elif c == 'p':
            print("\nYour " + pName + " kills the enemy " + cName + "!")
            return 1
        elif c == 's':
            print("\nThe " + pName + " and the " + cName + " kill each other!")
            return 0

def main():
    choice = 0
    game_running = True

    #player must enter a valid number from 1 - 4 to select their faction
    while((choice != 1) and (choice != 2) and (choice != 3) and (choice != 4)):
        print("FACTIONS\n")
        print("1. Human\n")
        print("2. Orc\n")
        print("3. Elven\n")
        print("4. Undead\n")
        choice = int(input("Pick a faction, enter a number (1 - 4): ")) 
    if choice == 1:
        pFaction = init_human()
    elif choice == 2:
        pFaction = init_orc()
    elif choice == 3:
        pFaction = init_elven()
    else:
        pFaction = init_undead()
        
    #player is initialized here
    player = User("Player", pFaction, 10)
    print(player.getName() + " chose " + player.faction.getName() + "!")

    #computer randomly chooses a faction
    randChoice = random.randint(1, 4)
    if randChoice == 1:
        cFaction = init_human()
    elif randChoice == 2:
        cFaction = init_orc()
    elif randChoice == 3:
        cFaction = init_elven()
    else:
        cFaction = init_undead()

    #computer is initialized here
    computer = User("Computer", cFaction, 10)
    print(computer.getName() + " chose " + computer.faction.getName() + "!")
    time.sleep(1)

    #both sides start with an empty board
    player_side = [None, None, None, None]
    computer_side = [None, None, None, None]

    #game is running as long as neither side has less than 1 health
    while(game_running):

        #player chooses four units for the round
        choices_made = 0
        while(choices_made != 4):
            unit_choice = 0
            print("PLAYER HEALTH: " + str(player.getHealth()) + " ------------- " + "COMPUTER HEALTH: " + str(computer.getHealth()))
            while((unit_choice != 1) and (unit_choice != 2) and (unit_choice != 3)):
                print("\n\nAVAILABLE UNITS (enter 1, 2, or 3)\n")
                print("1. " + player.faction.rock.getName())
                print("2. " + player.faction.paper.getName())
                print("3. " + player.faction.scissor.getName())
                unit_choice = int(input("Pick unit #" + str(choices_made+1) + ": "))
            if unit_choice == 1:
                player_side[choices_made] = Unit(player.faction.rock.getName(), player.faction.rock.getRole())
            elif unit_choice == 2:
                player_side[choices_made] = Unit(player.faction.paper.getName(), player.faction.paper.getRole())
            else:
                player_side[choices_made] = Unit(player.faction.scissor.getName(), player.faction.scissor.getRole())
            choices_made = choices_made + 1

        #computer randomly chooses four units for the round
        for x in range(4):
            rand_unit = random.randint(1, 3)
            if rand_unit == 1:
                computer_side[x] = Unit(computer.faction.rock.getName(), computer.faction.rock.getRole())
            elif rand_unit == 2:
                computer_side[x] = Unit(computer.faction.paper.getName(), computer.faction.paper.getRole())
            else:
                computer_side[x] = Unit(computer.faction.scissor.getName(), computer.faction.scissor.getRole())
            
        print_board(player, computer, player_side, computer_side)
        
        print("\nFIGHT!")
        time.sleep(1)

        #combat is handled here
        #starts at 0, adds 1 if the player wins a fight, and takes away 1 if the player loses a fight
        #at the end of the round, a positive score is removed from the computer
        #a negative score is removed from the player
        #and a zero score means nobody loses health
        combat_result = 0
        for x in range(4):
            combat_result = combat_result + combat(player_side[x], computer_side[x])
            time.sleep(2)
        if combat_result > 0:
            print("\n" + player.getName() + " wins the round and deals " + str(combat_result) + " damage!")
            computer.health = computer.health - combat_result
        elif combat_result < 0:
            print("\n" + player.getName() + " loses the round and takes " + str(combat_result * -1) + " damage!")
            player.health = player.health + combat_result
        elif combat_result == 0:
            print("\nTie round! Nobody takes any damage!")
        time.sleep(2)

        #check for gameover
        #there cannot be a tie so no need to check for that
        if (player.getHealth() < 1):
            winner = computer
            game_running = False
        elif (computer.getHealth() < 1):
            winner = player
            game_running = False
        

    print("\n" + winner.getName() + " wins!")
        
        
        
        
    
