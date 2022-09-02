import curses
from random import randint
from random import choice
import time
import sys
import dc_ascii
import dc_animations

#ascii text generator http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
#ascii image generator https://manytools.org/hacker-tools/convert-images-to-ascii-art/
#the frame work for the menu comes from this github
#https://github.com/nikhilkumarsingh/python-curses-tut/blob/master/02.%20Creating%20Menu%20Display.ipynb

#this will be used by the various menu functions, its global becuase multiple functions use it at once
menu = ["Yes", "No"]


#function to print the title screen
def startGame(stdscr):
    #disables the white text box
    curses.curs_set(0)
    #gets the height and width of the screen
    h, w = stdscr.getmaxyx()
    #sets x and y to be in the middle
    x = w // 2
    y = h // 2
    #function to print the wall border
    dc_ascii.printWall(stdscr)
    #prints the skull art and creeper face
    dc_ascii.printStart(stdscr)
    #makes a color pair, black text on a white background
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    #puts  the users selected option to the top
    current_row = 0
    #asks displays input question
    stdscr.addstr(y - 5, x - 5, "Start game?")
    #refreshes the screen so it will actually display whats above
    stdscr.refresh()
    #function to print the menu options
    printMenu(stdscr, current_row)
    #this loop determines what will happen when the arrow and enter keys are pressed
    while 1:
        #sets key to be whatever key gets pressed
        key = stdscr.getch()
        #if the up  arrow is pressed and the user has not selected the top option
        if key == curses.KEY_UP and current_row > 0:
            #moves the selected option up one
            current_row -= 1
        #if the down arrow is pressed and the bottom option is not selected
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            #moves the selected option down one
            current_row += 1
        #if the enter key is pressed (curses is inconsistent with how it identifies the enter key, so it checks it in two         different ways)
        elif curses.KEY_ENTER or key in [10, 13]:
            #if the top option is selected
            if current_row == 0:
                #function to have the player walk in a room
                player.enterRoom(stdscr)
                #stops the loop
                break
            #if the bottom option is selected
            if current_row == 1:
                #erases the screan
                stdscr.clear()
                #prints a sad face
                stdscr.addstr(y, x, ":(")
                #displays it for two seconds
                stdscr.refresh()
                time.sleep(2)
                #stops the program
                break
        #updates which option the white background gets drawn on, also it passes which option is being selected
        printMenu(stdscr, current_row)


#function to pick and reset an enemy
def makeEnemy():
    global enemy
    enemy = choice(enemies)
    #each enemy has a health range
    if (enemy.name == 'Enderman'):
        enemy.health = randint(18, 22)
    elif (enemy.name == 'Creeper'):
        enemy.health = randint(12, 16)
    elif (enemy.name == 'Witch'):
        enemy.health = randint(14, 18)
    elif (enemy.name == 'Spider'):
        enemy.health = randint(10, 14)
    elif (enemy.name == 'Skeleton'):
        enemy.health = randint(10, 12)
    elif (enemy.name == 'Zombie'):
        enemy.health = randint(10, 12)


# function to print player and enemy health, and players potions
def printUI(stdscr):
    h, w = stdscr.getmaxyx()
    x = w // 2
    y = h // 2
    text1 = "Player health: "
    #this is so that it will print in the true middle
    x = w // 2 - len(text1) // 2
    y = h // 2 - 6
    stdscr.addstr(y, x, text1)

    #decices what color the health will be shown in based on the value
    #if its 20 or above its green
    if player.health > 19:
        #this one is green with a black background
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
        stdscr.addstr(y, x + 15, f"{player.health}", curses.color_pair(3))
    #if its between 10 and 19, it will print as yellow
    elif player.health > 9:
        curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        stdscr.addstr(y, x + 15, f"{player.health}", curses.color_pair(4))
    #if its between 1 and 9, it will print as red
    elif player.health > -1:
        curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)
        stdscr.addstr(y, x + 15, f"{player.health}", curses.color_pair(5))

    #prints the players potions
    y = h // 2 - 5
    text2 = f"Player potions: {player.potion}"
    stdscr.addstr(y, x, text2)
    #prints the enemies health
    y = h // 2 - 4
    text3 = f"Enemy health: {enemy.health}"
    stdscr.addstr(y, x, text3)

    text = f'Current enemy: {enemy.name}'
    x = w // 2 - len(text1) // 2
    y = h // 2 - 3
    stdscr.addstr(y, x, text)
    stdscr.refresh()


#function to print the selected menu option, this gets passed the option the player is selecting
def printMenu(stdscr, selected_row_idx):
    h, w = stdscr.getmaxyx()
    
    for idx, row in enumerate(menu):
        x = w // 2 - len(row) // 2
        y = h // 2 - len(menu) // 2 + idx
        if idx == selected_row_idx:
            #this is turning on the black and white color pair
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            #this turns the color pair off
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()


#the main menu that will be called, decides if the player will attack, potion, or view inventory
def menuSelect(stdscr):
    h, w = stdscr.getmaxyx()
    y = h // 2
    x = w // 2
    #this is a way to clear the options from the secondary weapons screen, to avoid clearing the screen
    stdscr.addstr(y, x - 8, "                    ")
    stdscr.addstr(y - 1, x - 8, "                   ")
    global menu
    #changes the menu to display the proper options
    menu = ['Attack', 'Potion', 'View Character']
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    #resets the selected option to the top
    current_row = 0
    #prints player and enemy information
    printUI(stdscr)
    stdscr.refresh()
    #prints the menu options
    printMenu(stdscr, current_row)

    while 1:
        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key in [10, 13]:
            if current_row == 0:
                #if attack is selected, it will ask if the player wants to use a bow (if the player has one)
                if 'Bow' and "Arrows" in player.inventory:
                    #prints a separate menu
                    menuBow(stdscr)
                    break
                else:
                    #if not, attacks with a sword
                    enemy.attack(stdscr)
                    break
            #if the second option is picked, drinks a potion
            if current_row == 1:
                player.drinkPotion(stdscr)
            #if the last optino is picked, it will print the inventory screen
            if current_row == 2:
                player.printInventory(stdscr)
                break

        printMenu(stdscr, current_row)


#fucntion to choose between sword or bow
def menuBow(stdscr):
    global menu
    menu = ["Use Sword", "Use Bow", "Back"]
    h, w = stdscr.getmaxyx()
    y = h // 2
    x = w // 2
    #this is to clear the 'view character' from the last menu
    stdscr.addstr(y + 1, x - 7, "                  ")
    printUI(stdscr)
    current_row = 0
    printMenu(stdscr, current_row)
    while 1:
        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key in [10, 13]:
            if current_row == 0:
                #if sword is selected, attack with a sword
                enemy.attack(stdscr)
                break

            if current_row == 1:
                enemy.attackBow(stdscr)
                break
            #now that i think about it, im not sure why i added a back option
            if current_row == 2:
                menuSelect(stdscr)
                break

        printMenu(stdscr, current_row)


#makes the parent class for the player and enemy
class Entity:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage


class Player(Entity):
    
    def __init__(self,
                 name,
                 health,
                 damage,
                 potion,
                 weapon=[],
                 head=[],
                 chest=[],
                 legs=[],
                 feet=[],
                 pet=[],
                 #this variable will increase with armor, acts as damage reduction
                 reduction=1,
                 inventory=[],
                 dog=False):
        super().__init__(name, health, damage)
        self.potion = potion
        #place to put the sword
        self.weapon = weapon
        #the next four are all places to put armor pieces
        self.head = head
        self.chest = chest
        self.legs = legs
        self.feet = feet
        self.pet = pet
        self.dog = dog
        #this divides all incoming damage based on armor
        self.reduction = reduction
        #place to put bow, arrows, and ender pearls
        self.inventory = inventory

    #function to have the player walk in a room, find an enemy, and a piece of loot
    def enterRoom(self, stdscr):
        player.died(stdscr)
        curses.curs_set(0)
        global menu
        placeholderRoom.makeRoom()
        #chooses and resets an Enemy
        makeEnemy()
        #sets a variable for the room and enemy
        current_room = placeholderRoom.name
        current_loot = placeholderRoom.loot
        #fucntion to have the player equip found loot
        player.equipLoot(current_loot)
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        #narrates, also keep in mind that the length of this string is the minimum width the program will work with
        text = f"{player.name} has entered {current_room} and encountered a {enemy.name}, and found a {current_loot.name}"
        x = w // 2 - len(text) // 2
        y = h // 2 - 10
        stdscr.addstr(y, x, text)
        if enemy.name == 'Enderman':
            dc_ascii.printEnderman(stdscr)
        elif enemy.name == 'Witch':
            dc_ascii.printWitch(stdscr)
        elif enemy.name == 'Creeper':
            dc_ascii.printCreeper(stdscr)
        elif enemy.name == 'Spider':
            dc_ascii.printSpider(stdscr)
        elif enemy.name == 'Skeleton':
            dc_ascii.printSkeleton(stdscr)
        elif enemy.name == "Zombie":
            dc_ascii.printZombie(stdscr)
        stdscr.refresh()
        menuSelect(stdscr)

    #function to put the loot on the player
    def equipLoot(self, current_loot):
        #if the loot found is a sword, and its a higher tier than the current sword, it will equip it automatically
        if current_loot.part == 'weapon' and current_loot.tier > self.weapon[
                0].tier:
            #removes the respective damage
            if self.weapon[0].tier == 1:
                self.damage -= 2
            elif self.weapon[0].tier == 2:
                self.damage -= 4
            #gets rid of the sword
            self.weapon.remove(self.weapon[0])
            #adds the new sword
            self.weapon.append(current_loot)
            #adds the respective damage
            if self.weapon[0].tier == 1:
                self.damage += 2
            elif self.weapon[0].tier == 2:
                self.damage += 4
            elif self.weapon[0].tier == 3:
                self.damage += 6
        #it does the same process for the rest of the pieces
        elif current_loot.part == 'helmet' and current_loot.tier > self.head[
                0].tier:
            if self.head[0].tier == 1:
                self.reduction -= .03
            elif self.head[0].tier == 2:
                self.reduction -= .05
            self.head.remove(self.head[0])
            self.head.append(current_loot)
            if self.head[0].tier == 1:
                self.reduction += .03
            elif self.head[0].tier == 2:
                self.reduction += .05
            elif self.head[0].tier == 3:
                self.reduction += .07

        elif current_loot.part == 'chestplate' and current_loot.tier > self.chest[
                0].tier:
            if self.chest[0].tier == 1:
                self.reduction -= .1
            elif self.chest[0].tier == 2:
                self.reduction -= .12

            self.chest.remove(self.chest[0])
            self.chest.append(current_loot)
            if self.chest[0].tier == 1:
                self.reduction += .1
            elif self.chest[0].tier == 2:
                self.reduction += .12
            elif self.chest[0].tier == 3:
                self.reduction += .15

        elif current_loot.part == 'pants' and current_loot.tier > self.legs[
                0].tier:
            if self.legs[0].tier == 1:
                self.reduction -= .05
            elif self.legs[0].tier == 2:
                self.reduction -= 0.8

            self.legs.remove(self.legs[0])
            self.legs.append(current_loot)
            if self.legs[0].tier == 1:
                self.reduction += .05
            elif self.legs[0].tier == 2:
                self.reduction += .08
            elif self.legs[0].tier == 3:
                self.reduction += .11

        elif current_loot.part == 'boots' and current_loot.tier > self.feet[
                0].tier:
            if self.feet[0].tier == 1:
                self.reduction -= .02
            elif self.feet[0].tier == 2:
                self.reduction -= .05
            self.feet.remove(self.feet[0])
            self.feet.append(current_loot)
            if self.feet[0].tier == 1:
                self.reduction += .02
            elif self.feet[0].tier == 2:
                self.reduction += .05
            elif self.feet[0].tier == 3:
                self.reduction += .07

        elif current_loot.part == 'potion':
            self.potion += 1

        elif current_loot.part == 'pet':
            if 'Bone' in player.inventory:
                player.pet.remove(self.pet[0])
                player.inventory.remove("Bone")
                player.pet.append(current_loot)
                self.dog = True

    def dogAttack(self, stdscr):
        if self.dog == True:
            damage = randint(2, 5)
            enemy.health -= damage
            h, w = stdscr.getmaxyx()
            text = f"Your dog bit the {enemy.name}, doing {damage} damage"
            y = h // 2
            x = w // 2 - len(text) // 2
            stdscr.addstr(y + 1, x, text)

    #function to print the players inventory (this looks really cool)
    def printInventory(self, stdscr):
        stdscr.clear()
        printUI(stdscr)
        #prints the equiped loot for each slot
        h, w = stdscr.getmaxyx()

        text = f"Pet: {self.pet[0].name}"
        x = w // 2 - len(text) // 2
        y = h // 2 - 7
        stdscr.addstr(y, x, text)

        text = f"Boots: {self.feet[0].name} "
        x = w // 2 - len(text) // 2
        y = h // 2 - 8
        stdscr.addstr(y, x, text)

        text = f"Pants: {self.legs[0].name} "
        x = w // 2 - len(text) // 2
        y = h // 2 - 9
        stdscr.addstr(y, x, text)

        text = f"Chestplate: {self.chest[0].name} "
        x = w // 2 - len(text) // 2
        y = h // 2 - 10
        stdscr.addstr(y, x, text)

        text = f"Helmet: {self.head[0].name} "
        x = w // 2 - len(text) // 2
        y = h // 2 - 11
        stdscr.addstr(y, x, text)

        text = f'Weapon: {self.weapon[0].name}'
        x = w // 2 - len(text) // 2
        y = h // 2 - 12
        stdscr.addstr(y, x, text)

        #prints the players damage
        text = f"Damage: {self.damage}"
        x = w // 2 - len(text) // 2
        y = h // 2 - 13
        stdscr.addstr(y, x, text)

        #prints the item in the inventory. this looks pretty stupid, because instead of saying 'Arrows x2' it says 'Arrows' 'Arrows' and i couldnt figure it out
        stdscr.addstr(y - 2, x - 8, 'Inventory:')
        #in the range of the number of items in the inventory
        for i in range(len(self.inventory)):
            #adds the item
            stdscr.addstr(y - 2, x + 2, f"{player.inventory[i]}")
            #moves to the left by the length of the last item + 1
            x += len(player.inventory[i]) + 1

        #prints the players damage resistance
        text = f"Damage resistance: {self.reduction}"
        x = w // 2 - len(text) // 2
        y = h // 2 - 13
        stdscr.addstr(y, x, text)

        curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_WHITE)
        x = w // 2
        y = h // 2 - 16

        #this is an ascii art of the player that adapts the armor that is on each part
        #if theres nothing, prints a lightly shaded pair of feet
        if self.head[0].tier == 0:
            stdscr.addstr(y - 10, x - 2, "░░░░")
            stdscr.addstr(y - 11, x - 2, "░░░░")
        #for iron, solid white
        elif self.head[0].tier == 1:
            stdscr.addstr(y - 10, x - 2, "████")
            stdscr.addstr(y - 11, x - 2, "████")
        #for diamond, cyan colored
        elif self.head[0].tier == 2:
            stdscr.addstr(y - 10, x - 2, "████", curses.color_pair(6))
            stdscr.addstr(y - 11, x - 2, "████", curses.color_pair(6))
        #for netherite, dark shading. theres no grey, and no way to make custom colors, so this is the best i can do
        elif self.head[0].tier == 3:
            stdscr.addstr(y - 10, x - 2, "▓▓▓▓")
            stdscr.addstr(y - 11, x - 2, "▓▓▓▓")
        #all the others work in the same way
        if self.chest[0].tier == 0:
            stdscr.addstr(y - 6, x - 4, "░░░░░░░░")
            stdscr.addstr(y - 7, x - 4, "░░░░░░░░")
            stdscr.addstr(y - 8, x - 4, "░░░░░░░░")
            stdscr.addstr(y - 9, x - 4, "░░░░░░░░")
        elif self.chest[0].tier == 1:
            stdscr.addstr(y - 6, x - 4, "████████")
            stdscr.addstr(y - 7, x - 4, "████████")
            stdscr.addstr(y - 8, x - 4, "████████")
            stdscr.addstr(y - 9, x - 4, "████████")
        elif self.chest[0].tier == 2:
            stdscr.addstr(y - 6, x - 4, "████████", curses.color_pair(6))
            stdscr.addstr(y - 7, x - 4, "████████", curses.color_pair(6))
            stdscr.addstr(y - 8, x - 4, "████████", curses.color_pair(6))
            stdscr.addstr(y - 9, x - 4, "████████", curses.color_pair(6))
        elif self.chest[0].tier == 3:
            stdscr.addstr(y - 6, x - 4, "▓▓▓▓▓▓▓▓")
            stdscr.addstr(y - 7, x - 4, "▓▓▓▓▓▓▓▓")
            stdscr.addstr(y - 8, x - 4, "▓▓▓▓▓▓▓▓")
            stdscr.addstr(y - 9, x - 4, "▓▓▓▓▓▓▓▓")

        if self.legs[0].tier == 0:
            stdscr.addstr(y - 4, x - 2, "░░░░")
            stdscr.addstr(y - 5, x - 2, "░░░░")
        elif self.legs[0].tier == 1:
            stdscr.addstr(y - 4, x - 2, "████")
            stdscr.addstr(y - 5, x - 2, "████")
        elif self.legs[0].tier == 2:
            stdscr.addstr(y - 4, x - 2, "████", curses.color_pair(6))
            stdscr.addstr(y - 5, x - 2, "████", curses.color_pair(6))
        elif self.legs[0].tier == 3:
            stdscr.addstr(y - 4, x - 2, "▓▓▓▓")
            stdscr.addstr(y - 5, x - 2, "▓▓▓▓")

        if self.feet[0].tier == 0:
            stdscr.addstr(y - 3, x - 2, "░░░░")
        elif self.feet[0].tier == 1:
            stdscr.addstr(y - 3, x - 2, "████")
        elif self.feet[0].tier == 2:
            stdscr.addstr(y - 3, x - 2, "████", curses.color_pair(6))
        elif self.feet[0].tier == 3:
            stdscr.addstr(y - 3, x - 2, "▓▓▓▓")

        global menu
        #changes the menu to only have the back option
        menu = ['Back']
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        current_row = 0

        stdscr.refresh()
        printMenu(stdscr, current_row)
        #makes a one option menu
        while 1:
            key = stdscr.getch()
            if key in [10, 13]:
                if current_row == 0:
                    stdscr.clear()
                    menuSelect(stdscr)
                    break

            printMenu(stdscr, current_row)

    #potion to drink a potion, health is capped at 30
    def drinkPotion(self, stdscr):
        h, w = stdscr.getmaxyx()
        #first checks to see if you dont have a potion
        if self.potion < 1:
            text = "You don't have any potions!"
            x = w // 2 - len(text) // 2
            y = h // 2
            stdscr.addstr(y - 7, x, text)
            stdscr.refresh()
        #if you do, checks to see if your health is at 30
        elif self.health > 29:
            text = "You cannot heal above 30!"
            x = w // 2 - len(text) // 2
            y = h // 2
            stdscr.addstr(y - 7, x, text)
            stdscr.refresh()
        #if your health  is close to 30, it will heal you to get you to thirty
        elif self.health > 21:
            self.potion -= 1

            self.health += randint(8, 12)
            #if your health went over 30
            if self.health > 30:
                #sets a variable to be the differnece between the health and 30
                correction = self.health - 30
                #subtracts the difference from your health to get you down to 30
                self.health -= correction
            printUI(stdscr)
            menuSelect(stdscr)
        #if you have a potion and are not close to thirty, heals you the full amound without any complication
        elif self.potion > 0:
            self.potion -= 1
            self.health += randint(8, 12)
            printUI(stdscr)
            menuSelect(stdscr)

    #function to check and display a death screen if the player died
    def died(self, stdscr):
        #if the player didnt die, move on
        if self.health > 0:
            pass
        #if they did
        elif self.health < 1:
            stdscr.clear()
            #prints the death screen ascii art
            dc_ascii.printDied(stdscr)
            global menu
            #makes a yes or no menu
            menu = ['Yes', 'No']
            curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
            current_row = 0
            h, w = stdscr.getmaxyx()
            #asks if they want to play again
            text = "Play again?"
            x = w // 2 - len(text) // 2
            y = h // 2
            stdscr.addstr(y - 3, x, text)
            stdscr.refresh()
            printMenu(stdscr, current_row)
            while 1:
                key = stdscr.getch()
                if key == curses.KEY_UP and current_row > 0:
                    current_row -= 1
                elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
                    current_row += 1
                elif key in [10, 13]:
                    #if yes is selected
                    if current_row == 0:
                        #resets the player and has them walk in a room
                        player.reset()
                        player.enterRoom(stdscr)
                        break
                    # if no is selected, ends the program
                    if current_row == 1:
                        stdscr.clear()
                        sys.exit(0)

                printMenu(stdscr, current_row)

    #function to reset the players health, potions, inventory, weapon, and armor
    def reset(self):
        player.health = 20
        player.damage = 6
        player.potion = 3
        player.weapon.clear()
        player.head.clear()
        player.chest.clear()
        player.legs.clear()
        player.feet.clear()
        player.inventory.clear()
        player.weapon.append(Loot('fists', 0, 'weapon'))
        player.head.append(Loot('nothing', 0, 'helmet'))
        player.chest.append(Loot('nothing', 0, 'chestplate'))
        player.legs.append(Loot('nothing', 0, 'pants'))
        player.feet.append(Loot('nothing', 0, 'boots'))
        player.pet.append(Loot("none", 1, 'pet'))
        player.dog = False


#makes the enemy class
class Enemy(Entity):
    #it only needs a name, health, and damge
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)

    #function to check if the enemy died, and gives the proper loot to the player
    def died(self, stdscr):
        #if they died
        if self.health < 1:
            h, w = stdscr.getmaxyx()
            #tells the player they killed the enemy
            text = f"{self.name} has been killed by Steve"
            y = h // 2
            x = w // 2 - len(text) // 2
            stdscr.clear()
            stdscr.addstr(y, x, text)
            if self.name == 'Skeleton':
                #gives between 1 and 5 arrows
                arrows = randint(1, 5)
                for i in range(arrows):
                    player.inventory.append('Arrows')
                #if the player has a bow, only gives them arrows
                if player.dog == False and 'Bone' not in player.inventory:
                    stdscr.addstr(y + 2, x, f'Skeleton dropped a bone')
                    player.inventory.append("Bone")
                if 'Bow' in player.inventory:
                    stdscr.addstr(y + 1, x,
                                  f'Skeleton dropped {arrows} arrows')
                else:
                    player.inventory.append('Bow')
                    stdscr.addstr(
                        y + 1, x,
                        f'Skeleton dropped a bow and {arrows} arrows')
                #if they dont have a bow, gives them one
            #if its a witch or a creeper, it will drop a health potion
            elif self.name == 'Witch' or 'Creeper':
                player.potion += 1
                stdscr.addstr(y + 1, x,
                              f'The {self.name} dropped a health potion')
            #if theyre a skeleton, they will drop bow and arrows

            #zombies and creepers dont drop anything
            stdscr.refresh()
            time.sleep(3)
            stdscr.clear()
            #player enters the next room
            player.enterRoom(stdscr)
        #if they didnt die, moves on
        else:
            pass

    #function to have the player and monster attack
    def attack(self, stdscr):
        curses.curs_set(0)
        h, w = stdscr.getmaxyx()
        y = h // 2
        x = w // 2
        #if the enemy is and enderman
        if enemy.name == 'Enderman':
            #subtract from the enderman health the player damage
            self.health -= player.damage
            #plays an animation of the player attacking
            dc_animations.attackEnderman(stdscr)
            stdscr.clear()
            #narrates
            text = f"Steve has done {player.damage} damage to the enderman"
            x = w // 2 - len(text) // 2
            stdscr.addstr(y, x, text)
            player.dogAttack(stdscr)
            x = w // 2
            stdscr.refresh()
            time.sleep(2)
            #checks if the enemy died
            enemy.died(stdscr)
            # does damage to the player divided by the players resistance
            self.damage = int(randint(6, 14) // player.reduction)
            player.health -= self.damage
            #plays the enderman attacking animation
            dc_animations.endermanAttack(stdscr)
            stdscr.clear()
            text = f"The enderman hits Steve, doing {self.damage} damage"
            x = w // 2 - len(text) // 2
            stdscr.addstr(y, x, text)
            x = w // 2
            stdscr.refresh()
            time.sleep(3)
            stdscr.clear()
            #checks if the player died
            player.died(stdscr)
            menuSelect(stdscr)
        #if the enemy is a creeper
        elif enemy.name == "Creeper":
            #attacks the creepr and plays an animation
            self.health -= player.damage
            dc_animations.attackCreeper(stdscr)
            stdscr.clear()
            enemy.died(stdscr)
            text = f"Steve has done {player.damage} damage to the creeper"
            x = w // 2 - len(text) // 2
            stdscr.addstr(y, x, text)
            player.dogAttack(stdscr)
            stdscr.refresh()
            x = w // 2
            time.sleep(2)
            enemy.died(stdscr)
            #the way the creepr attacks is it has a 50/50 chance of exploding and dealing a lot of damage, or doing nothing
            explosion_chance = (randint(1, 2))

            if (explosion_chance == 1):
                explosion = True
            else:
                explosion = False
            #if it did explode
            if explosion == True:
                #plays the animation
                dc_animations.creeperExplode(stdscr)
                stdscr.clear()
                #does damage divided by resistance, the creepr has the highest damage output
                self.damage = int(randint(12, 16) // player.reduction)
                player.health -= self.damage
                text = f"The creeper blew up, doing {self.damage} damage to Steve"
                x = w // 2 - len(text) // 2
                stdscr.addstr(y, x, text)
                stdscr.refresh()
                time.sleep(2)

                x = w // 2
                player.died(stdscr)
                player.enterRoom(stdscr)
            #if it didnt blow up
            else:
                #plays an animation of the player walking away
                dc_animations.creeperEscape(stdscr)
                stdscr.clear()

                text = "The creeper tries to blow up, but Steve steps away just in time"
                x = w // 2 - len(text) // 2
                stdscr.addstr(y, x, text)
                stdscr.refresh()
                time.sleep(3)
                stdscr.clear()
                menuSelect(stdscr)
        #the rest work the same as the enderman
        elif enemy.name == 'Witch':
            stdscr.clear()
            dc_animations.attackWitch(stdscr)
            stdscr.clear()

            self.health -= player.damage
            text = f"Steve has done {player.damage} damage to the witch"
            x = w // 2 - len(text) // 2
            stdscr.addstr(y, x, text)
            player.dogAttack(stdscr)
            stdscr.refresh()
            time.sleep(2)
            stdscr.clear()
            enemy.died(stdscr)
            dc_animations.witchAttack(stdscr)
            stdscr.clear()

            self.damage = int(randint(5, 11) // player.reduction)
            player.health -= self.damage
            text = f"The witch threw a potion at Steve, doing {self.damage} damage"
            x = w // 2 - len(text) // 2
            stdscr.addstr(y, x, text)
            stdscr.refresh()
            time.sleep(2)
            stdscr.clear()
            player.died(stdscr)
            menuSelect(stdscr)

        elif enemy.name == 'Spider':
            dc_animations.attackSpider(stdscr)
            time.sleep(0.5)
            stdscr.clear
            self.health -= player.damage

            enemy.died(stdscr)

            stdscr.clear()

            text = f"Steve did {player.damage} damage to the spider"
            x = w // 2 - len(text) // 2
            stdscr.addstr(y, x, text)
            player.dogAttack(stdscr)
            stdscr.refresh()
            time.sleep(2)
            dc_animations.spiderAttack(stdscr)
            stdscr.clear()

            self.damage = int(randint(4, 7) // player.reduction)
            player.health -= self.damage
            text = f"The spider has bit Steve, doing {self.damage} damage"
            x = w // 2 - len(text) // 2
            stdscr.addstr(y, x, text)
            stdscr.refresh()
            time.sleep(2)
            stdscr.clear()
            player.died(stdscr)
            menuSelect(stdscr)

        elif enemy.name == 'Skeleton':
            dc_animations.attackSkeleton(stdscr)

            self.health -= player.damage

            enemy.died(stdscr)
            stdscr.clear()
            text = f"Steve has done {player.damage} damage to the skeleton"
            x = w // 2 - len(text) // 2
            stdscr.addstr(y, x, text)
            player.dogAttack(stdscr)
            stdscr.refresh()
            time.sleep(2)
            dc_animations.skeletonAttack(stdscr)
            stdscr.clear()

            self.damage = int(randint(4, 7) // player.reduction)
            player.health -= self.damage
            text = f"Skeleton has shot Steve, doing {self.damage} damage"
            x = w // 2 - len(text) // 2
            stdscr.addstr(y, x, text)
            stdscr.refresh()
            time.sleep(2)
            stdscr.clear()
            player.died(stdscr)
            menuSelect(stdscr)

        elif enemy.name == 'Zombie':
            dc_animations.attackZombie(stdscr)
            stdscr.clear()

            self.health -= player.damage

            enemy.died(stdscr)

            text = f"Steve did {player.damage} damage to the zombie"
            x = w // 2 - len(text) // 2
            stdscr.addstr(y, x, text)
            player.dogAttack(stdscr)
            stdscr.refresh()
            time.sleep(2)
            dc_animations.zombieAttack(stdscr)
            stdscr.clear()

            self.damage = int(randint(1, 5) // player.reduction)
            player.health -= self.damage
            text = f"The zombie bit Steve, doing {self.damage} damage"
            x = w // 2 - len(text) // 2
            stdscr.addstr(y, x, text)
            stdscr.refresh()
            time.sleep(2)
            stdscr.clear()
            player.died(stdscr)
            menuSelect(stdscr)

    #function to attack mobs with a bow
    def attackBow(self, stdscr):
        h, w = stdscr.getmaxyx()
        y = h // 2
        x = w // 2
        #the bow does between 4 and 10 damage
        damage = randint(4, 10)
        #each time its used, removes one arrow
        player.inventory.remove('Arrows')
        #the enderman will not be hit by the arrow, but will hit the player
        if self.name == 'Enderman':
            stdscr.clear()
            #animation of the enderman teleporting out of the way
            dc_animations.attackEndermanBow(stdscr)
            stdscr.clear()
            text = "The enderman teleports out of the way of the arrow"
            x = w // 2 - len(text) // 2
            stdscr.addstr(y, x, text)
            stdscr.refresh()
            time.sleep(2)
            stdscr.clear()
            #hits the player
            self.damage = int(randint(6, 14) // player.reduction)
            player.health -= self.damage
            #animation of attacking the player
            dc_animations.endermanAttackBow(stdscr)
            stdscr.clear()
            text = f"The enderman hits Steve, doing {self.damage} damage"
            x = w // 2 - len(text) // 2
            stdscr.addstr(y, x, text)
            x = w // 2
            stdscr.refresh()
            time.sleep(2)
            stdscr.clear()
            player.died(stdscr)
            menuSelect(stdscr)
        #the skeleton will be hit by the arrow, but can also hit the player
        elif self.name == 'Skeleton':
            stdscr.clear()
            dc_animations.attackSkeletonBow(stdscr)
            stdscr.clear()
            self.health -= damage
            text = f"Steve has done {damage} damage to the {self.name}"
            x = w // 2 - len(text) // 2
            stdscr.addstr(y, x, text)
            stdscr.refresh()
            time.sleep(2)
            stdscr.clear()

            enemy.died(stdscr)

            self.damage = int(randint(4, 7) // player.reduction)
            player.health -= self.damage
            dc_animations.skeletonAttackBow(stdscr)
            stdscr.clear()
            text = f"The skeleton has done {self.damage} damage to Steve"
            x = w // 2 - len(text) // 2
            stdscr.addstr(y, x, text)
            stdscr.refresh()
            time.sleep(2)
            stdscr.clear()
            player.died(stdscr)
            menuSelect(stdscr)
        #the rest will be hit and can not hit back
        elif self.name == 'Creeper' or 'Witch' or 'Spider' or 'Zombie':
            stdscr.clear()
            #plays the respective animation
            if self.name == 'Creeper':
                dc_animations.attackCreeperBow(stdscr)
            elif self.name == 'Witch':
                dc_animations.attackWitchBow(stdscr)
            elif self.name == 'Spider':
                dc_animations.attackSpiderBow(stdscr)
            elif self.name == 'Zombie':
                dc_animations.attackZombieBow(stdscr)
            stdscr.clear()
            self.health -= damage
            text = f"Steve did {damage} damage to the {self.name}"
            x = w // 2 - len(text) // 2
            stdscr.addstr(y, x, text)
            stdscr.refresh()
            time.sleep(2)
            stdscr.clear()
            enemy.died(stdscr)
            menuSelect(stdscr)


#makes a class for the room, with a name and loot
class Room:
    def __init__(self, name, loot='placeholder'):
        self.name = name
        self.loot = loot

    #fucntion to choose a name and loot
    def makeRoom(self):
        self.name = choice(rooms).name
        self.loot = choice(loot)


#makes the loot class, with a name, tier, and a part (i wanted to use type, but thats a special word)
class Loot:
    def __init__(self, name, tier, part):
        self.name = name
        self.tier = tier
        self.part = part


#makes the list of enemies, the inital health and damages dont matter because they will be overwritten
enemies = [
    Enemy('Enderman', 10, 10),
    Enemy('Creeper', 10, 10),
    Enemy('Witch', 10, 10),
    Enemy('Skeleton', 10, 10),
    Enemy('Spider', 10, 10),
    Enemy('Zombie', 10, 10)
]

#makes the player
player = Player('Steve', 20, 6, 3)
#makes a temporary enemy and room that will be replaced
placeholderEnemy = Enemy('placeholder', 10, 10)
placeholderRoom = Room('placeholder')

#makes the room list, theres not a lot to choose from tbh
rooms = [Room('Prison'), Room('Storeroom'), Room('Library')]

#makes the loot pool, any one of these can be found at any time
loot = [
    Loot('Iron Sword', 1, 'weapon'),
    Loot('Diamond sword', 2, 'weapon'),
    Loot('Netherite sword', 3, 'weapon'),
    Loot('Iron helmet', 1, 'helmet'),
    Loot('Diamond helmet', 2, 'helmet'),
    Loot('Netherite helmet', 3, 'helmet'),
    Loot('Iron chestplate', 1, 'chestplate'),
    Loot('Diamond chestplate', 2, 'chestplate'),
    Loot('Netherite chestplate', 3, 'chestplate'),
    Loot('Iron pants', 1, 'pants'),
    Loot('Diamond pants', 2, 'pants'),
    Loot('Netherite pants', 3, 'pants'),
    Loot('Iron boots', 1, 'boots'),
    Loot('Diamond boots', 2, 'boots'),
    Loot('Netherite boots', 3, 'boots'),
    Loot('Health potion', 1, 'potion'),
    Loot('Dog', 1, 'pet')
]

#the player starts with 'nothing' equiped
player.weapon.append(Loot('Stone sword', 0, 'weapon'))
player.head.append(Loot('nothing', 0, 'helmet'))
player.chest.append(Loot('nothing', 0, 'chestplate'))
player.legs.append(Loot('nothing', 0, 'pants'))
player.feet.append(Loot('nothing', 0, 'boots'))
player.pet.append(Loot('none', 0, 'pet'))

#starts a curses wrapper and starts the game
curses.wrapper(startGame)