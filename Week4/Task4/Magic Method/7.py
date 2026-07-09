#17.	Override __contains__() so "Rahul" in team returns True if Rahul is in the team.


class Team:
    def __init__(self,name):
        self.name = name 

    def __contains__(self, item):
        return item in self.name
    

t = Team(["iron man","spider man","captain", "black widow","hawkeye"])
print("hawkeye" in t)
print("Dr.strange" in t)