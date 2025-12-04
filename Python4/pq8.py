class Player:
    player_count = 0
    def __init__(self, name, level):
        self.name = name
        self.level = level
        Player.player_count+=1

p = Player("Vineetha", "Beginner")
print(f"{p.player_count ,p.name, p.level}")

p1 = Player("Varshitha", "Pro")
print(f"{p1.player_count ,p1.name, p1.level}")