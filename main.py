

# Player class. Created when user completes character creation.
class Player:
    def __init__(self, name, stats):
        self.name = name
        self.health = 100
        self.items = []
        self.stats = stats



# Broad encounter class. Properties TBD.
class Encounter:
    def __init__(self):
        pass



# Combat Encounter class. Must include stats (bulk,swift,ego)
class CombatEncounter(Encounter):
    def __init__(self, stats):
        # super.__init__()
        self.stats = stats






# Character Creation

name = input("what is your name?")
creation_points = 20

print(f"you have {str(creation_points)} points left")

bulk = int(input("how bulky are you?"))
creation_points -= bulk

print(f"you have {str(creation_points)} points left")
swift = int(input("how nimble are you?"))
creation_points -= swift

print(f"you have {str(creation_points)} points left")
ego = int(input("how popular are you?"))
creation_points -= ego

print(f"Bulk:{str(bulk)} Swift:{str(swift)} Ego:{str(ego)}")
print(creation_points)

player = Player(name=name, stats=(bulk,swift,ego))





        
