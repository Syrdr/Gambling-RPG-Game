import random

class Enemy:
    def __init__(self, health, name, damage):
        self.health = health
        self.name = name
        self.damage = damage
        
    def TakeDamage(self, dmg):
        self.health -= dmg
        
class Player:
    def __init__(self, health, damage, name):
        self.health = health
        self.damage = damage
        self.name = name
        
    def TakeDamage(self, dmg):
        self.health -= dmg


playerwon = False
monsters = ["Monster Octopus", "Evil Troll", "Eater", "Chomper"]
playername = input("Your name: ")
i = 0
isBattleDone = False
playerinstance = Player(100, 10, playername)

while i < 4:
    playerhealth = 100 + i * 4  # Update player health based on battle round
    playerinstance.damage = 10 + i  # Update player damage based on battle round
    currentmonster = Enemy(i * 10 + 100, monsters[i], 10 + i)
    print(f"\n{playername} is currently fighting monster {monsters[i]}")
    isBattleDone = False

    while not isBattleDone:
        # Use a random multiplier for each attack
        player_multiplier = random.random()
        monster_multiplier = random.random()
        
        # Player attacks monster
        playerdmg = playerinstance.damage * player_multiplier
        currentmonster.TakeDamage(playerdmg)
        print(f"{playername} dealt {playerdmg:.2f} damage")
        
        if currentmonster.health <= 0:
            print(f"{monsters[i]} has been slain!")
            playerwon = True
            isBattleDone = True
            break  # Exit the battle loop when the monster is defeated
        
        # Monster attacks player
        monsterdmg = currentmonster.damage * monster_multiplier
        playerinstance.TakeDamage(monsterdmg)
        print(f"{monsters[i]} dealt {monsterdmg:.2f} damage")
        
        if playerinstance.health <= 0:
            print(f"{playername} has been slain!")
            playerwon = False
            isBattleDone = True
            break  # Exit the battle loop when the player is defeated
        
    if playerinstance.health <= 0:  # If player died, break the main loop
        break  # End the game if the player is dead

    # Ask if the player wants to keep going only after a battle is over
    if isBattleDone:
        currentreward = i * 2 + 2
        keepgoing = input(f"Do you want to keep going? You can add $2 to your existing ${currentreward} reward! Losing will drop your prize money to zero (y to continue, anything else to stop):\n ")
        if keepgoing.lower() != "y":
            print(f"You chose to stop! Ending this battle. Total prize is {currentreward}")
            break  # Exit the main loop if the player decides to stop the game

    i += 1  # Move to the next monster

# Final reward based on the number of battles won
if playerwon:
    print(f"\nYou win ${currentreward}!")
else:
    print(f"\nYou won {i} battles but still lost your last one! You win nothing!")
