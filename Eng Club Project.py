#this is from when it didn't work, but may be freely modified. check gambling.py for full version

class Player:
	def __init__(self, name, health, damage):
  	self.name = name
    self.health = health
    self.damage = damage
    self.isattacking = false
  def Attack(dmg, enemyname):
  	enemyname.health -= dmg
  	self.isattacking = false
playername = Input("Your name: ")
currentplayer = new Player(playername, 100, 10)

enemieslist = ["Monster1", "Monster2", "Monster3"]
monsters = []


class Enemy:
	def __init__(self, name, health, damage):
  	self.name = name
    self.health = health
    self.damage = damage
  def TakeDamage(dmg):
  	self.damage -= dmg
i = 0
h = 100
for i in enemieslist:
  Monster1 = new Enemy(i, h, 10 + h * 0.1)
  h + =10
  monsters.append(Monster1)
  
stage = 0
def runGame():
  
  stage +=1
