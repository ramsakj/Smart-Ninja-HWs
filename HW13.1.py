class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds

class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards

print("Enter some football players data!")

f_name = input("Enter first name: ")
l_name = input("Enter last name: ")
height = input("Enter height: ")
weight = input("Enter weight: ")
goals = input("Enter the number of goals: ")
y_cards = input("Enter the number of yellow cards: ")
r_cards = input("Enter the number of red cards: ")

new_player = FootballPlayer(first_name=f_name, last_name=l_name, height_cm=float(height), weight_kg=float(weight),
                            goals=goals, yellow_cards=y_cards, red_cards=r_cards)

with open("players.json", "w") as players_file:
    players_file.write(str(new_player.__dict__))

print("player: {0}".format(new_player.__dict__))

