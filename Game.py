import random

# Item Class
class Item:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect  # Can be a heal amount, attack buff, etc.

# Enemy Class
class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    
    def attack(self, player):
        player.take_damage(self.attack_power)
    
    def take_damage(self, damage):
        self.health -= damage
        return self.health <= 0

# Player Class
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 10
        self.inventory = []
        self.experience = 0
        self.level = 1
    
    def attack(self, enemy):
        enemy.take_damage(self.attack_power)
    
    def take_damage(self, damage):
        self.health -= damage
        return self.health <= 0
    
    def use_item(self, item):
        if item.effect > 0:
            self.health += item.effect
        self.inventory.remove(item)
    
    def level_up(self):
        self.level += 1
        self.attack_power += 5
        self.health += 20
        print(f"You leveled up to level {self.level}!")

# Game Logic
def game():
    player = Player(name=input("Enter your player name: "))
    
    rooms = ["empty", "enemy", "item"]
    
    while player.health > 0:
        print("\nChoose a direction to move: north, south, east, west")
        direction = input("Enter direction: ").strip().lower()
        
        event = random.choice(rooms)
        
        if event == "enemy":
            enemy = Enemy("Goblin", 30, 5)
            print(f"An enemy {enemy.name} appears!")
            
            while enemy.health > 0 and player.health > 0:
                print("\n1) Attack  2) Use Item")
                action = input("Choose an action: ").strip()
                
                if action == "1":
                    player.attack(enemy)
                    print(f"You attacked the {enemy.name}. Enemy health: {enemy.health}")
                    
                    if enemy.health <= 0:
                        print("You defeated the enemy!")
                        player.experience += 20
                        if player.experience >= 50:
                            player.level_up()
                        break
                    
                    enemy.attack(player)
                    print(f"The {enemy.name} attacked you. Your health: {player.health}")
                    
                elif action == "2" and player.inventory:
                    print("Choose an item to use:")
                    for i, item in enumerate(player.inventory):
                        print(f"{i+1}) {item.name}")
                    item_choice = int(input("Enter item number: ")) - 1
                    player.use_item(player.inventory[item_choice])
                else:
                    print("Invalid action or no items left!")
        
        elif event == "item":
            item = Item("Health Potion", effect=random.randint(10, 30))
            print(f"You found a {item.name}!")
            player.inventory.append(item)
        
        else:
            print("The room is empty.")

    print("Game Over! Thanks for playing.")

# Run the game
if __name__ == "__main__":
    game()
