#RPG - Non HD Remake
#by Ruari Phipps

import random, os, time

locations = {"North Town":["Salty Sea Tavern","Houses","Ethans Shop","Path"],"Salty Sea Tavern":["Buy Ale: 5 gold","Talk to owner","Exit"]}

#Classes
class Character (object):
    def __init__(self,name,className,health,maxHealth,armour,attack,speed,gold,inventory,storySection):
        self.name = name
        self.health = health
        self.maxHealth = maxHealth
        self.className = className
        self.armour = armour
        self.attack = attack
        self.speed = speed
        self.gold = gold
        self.storySection = storySection
    def heal(self,amount):
        if self.health == self.maxHealth:
            print ("Your already at max health")
        else:
            self.health += amount
            if self.health > self.maxHealth:
                self.health = self.maxHealth
            print ("You have been healed")
    def removeGold(self,amount):
        if self.gold - amount < 0:
            print ("You dont have enough money for that")
        else:
            self.gold -= amount
    
            
            
        
        


#Functions
def cls():
    os.system("cls")

def promptEnter():
    input("\n(Press enter to continue)")

def showMap():
    print ("    MAP OF RUARI   ") 
    print ("     _____      KEY:")
    print (" ___|  T D|_    T=Town")
    print ("|          _|   D=Dock")
    print ("|_C   F   |_    C=Cave")
    print ("  |     _   |   F=Forest")
    print ("  |___T| |__|       ")
    promptEnter()
    cls()
    return

def startmenu():
    print ("Ruari Games Presents")
    time.sleep(1)
    print ("PokeScrolls: Call of Battlecraft")
    time.sleep(2)
    print ("Enter number of choice:\n1.New Game\n2.Continue Game\n3.Exit")
    while True:
        userchoice = input ()
        if userchoice == "1":
            newgame()
        elif userchoice == "2":
            continuegame()
        elif userchoice == "3":
            exit()
        else:
            print ("Please enter valid input")

def newgame():
    cls()
    name = input("Enter your name: ")
    cls()
    print ("Select your class:\n1.Warrior(High health and armour)\n2.Wizard(High attack and High Speed)")
    while True:
        classchoice = input ("Enter number of your choice: ")
        if classchoice == "1":
            hp = 30
            maxhp = 30
            className = "warrior"
            armour = 10
            attack = 5
            speed = 5
            break 
        elif classchoice == "2":
            hp = 25
            maxhp = 25
            className = "wizard"
            armour = 5
            attack = 10
            speed = 10
            break
        else:
            print ("Please enter valid input")
    player = Character(name,className,hp,maxhp,armour,attack,speed,10,[],"none")
    beginStory(player)

def beginStory(player):
    cls()
    print("In a world not to different from ours,\na new adventure was about to begin.\n"+player.name,"the",player.className,"was on board a boat heading off unware about their future adventure.")
    promptEnter()
    cls()
    print("As the sun begins to rise",player.name,"comes up onto the deck\n"+player.name,"look onto the distance and spot an island.\nThe island of Ruari!")
    promptEnter()
    cls()
    print("A few hours later",player.name,"steps onto the land and is greated my and old man")
    print("OLD MAN: Hello traveler and welcome to Ruari island\nJust so you know some mysterios things have been hapening on the island recently so take care\nAnyway have a map to guide you\nI would recomend going to North town first, the tavern is top quality")
    time.sleep(5)
    print ("\nYOU HAVE OBTAINED A MAP!")
    print ("Type map to use it, try it now")
    while True:
        if input().lower() == "map":
            showMap()
            break
        else:
            print ("Try again")
    location = "North Town"
    player.storySection = "Salty Sea Tavern"
    mainSection(player,location)
    
def mainSection(player,location):
    print ("You have entered",location)
    options = locations[location]
    for x in range (0,len(options)):
        print (str(x+1)+"."+options[x])
    while True:
        selection = input("Enter number of choice: ")
        if int(selection) >= 0 or selection <= len(options)-1:
            location, player = selectFunction(player,options[int(selection)-1],location )
            break
        else:
            print("Enter Valid Choice")
    
def selectFunction(player,Selected,location):
    if Selected == "Salty Sea Tavern":
        location = "Salty Sea Tavern"
    if Selected == "Buy Ale: 5 gold":
        if player.removeGold(5) != False:
            player.heal(5)
    if Selected == "Talk to owner" and location == "Salty Sea Tavern":
        if player.storySection == "Salty Sea Tavern":
            print ("JOSH: You must be a torist, welcome to the island\nI'm Josh the owner of this tavern is their anything i can do for you?")
            print ("(You ask about the mystrious things going on)")
            print ("JOSH: Oh, well no one really knows whats happening.\nThere has been rumours of curses, magic and dragons but its all rubbish.\nNothings happened for decades it just stories to make it seem exiciting.")
            print ("But there is something going on in the houses of this town, dont know what\nbut you look like you can deal with it.\nTell you what if you sort out whats going on, i'll give you 30 gold if thats alright,\nGo to the shop and tell my brother I sent you.")
            player.storySection = "EthansShop"
        else:
            print ("JOSH:"+random.choice["How you doing mate","Nothing better than one of my ales","Heard of a guy named Jay? Apparently he's creating powerful creatures. Thats just wrong","My brothers called ethan and he own the shop in this town","I wanted to be a stand up comeidian but this is alrigh"])
    if Selected == "Exit" and location == "Salty Sea Tavern":
        location = "North Town"
        
        
#Maincode


startmenu()
