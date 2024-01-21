import datetime

class CricketPlayer:
    def __init__(self, fname, lname, team, birth_year):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = birth_year
        self.team = team
        self.scores = []


def get_age(self):
    now = datetime.datetime.now()
    return now.year - self.birth_year

def add_score(self, score):
    self.scores.append(score)

def get_average_score(self):
    return sum(self.scores)/len(self.scores)


virat = CricketPlayer('virat', 'kohli', 'india', 1988)
virat.add_score(80)
virat.add_score(100)
virat.add_score(0)


david = CricketPlayer('david', 'warner', 'australia', 1985)
david.add_score(37)
david.add_score(23)
david.add_score(85)

print(david.get_average_score())

5 < 8



