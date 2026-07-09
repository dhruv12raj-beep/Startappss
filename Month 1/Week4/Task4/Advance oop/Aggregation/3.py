# Create a Team class and a Player class. Add multiple players to a team and display all player names.


class Team:
    def __init__(self,name):
        self.name = name 
        self.players = []


class Player:
    def __init__(self,name):
        self.name = name 


t1 = Team("India")
p1 = Player("Dhruv")
p2 = Player("Aizen")


t1.players.append(p1)
t1.players.append(p2)


for p in t1.players:
    print(f"Team: {t1.name} -> Players: {p.name}")