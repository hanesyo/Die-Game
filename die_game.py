import random
die_faces = (1, 2, 3, 4, 5, 6) # Expressions & Variables 1.1 & 1.2

class Player:
     def create_player(self, name):
        """Creates a new player with a name and start their score at 0"""
        self.name = name
        self.score = 0
        return self
def die_tuple():
    rolls = []  
    for _ in range(3):  
        this_roll = random.choice(die_faces)  
        rolls.append(this_roll)  
    return rolls

def tupled_out(rolls):
    """Checks if all 3 die are the same"""
    return all(roll == rolls[0] for roll in rolls)

def die_reroll(rolls, fixed_die):
        """Reroll any dice that are not duplicates."""
        for i in range(len(rolls)):
            if rolls[i] not in fixed_die:
                rolls[i] = random.choice(die_faces)  
        return rolls

def tuple_game():
    players = []
    player_num = int(input("Enter the number of players: "))
    # create players
    for i in range (player_num):
         player_name = input(f"Enter player name {i +1}: ")
         players.append(Player().create_player(player_name))
    while True:
         for player in players:
            print(f"{player.name}'s turn")
            input("Press Enter to roll the die:")

            rolls = die_tuple()
            print("You rolled: ", rolls)
            # Check if the player has tupled out
            if tupled_out(rolls):
                print("You TUPLED OUT, better luck next time.")
                print(f"GAME OVER for {player.name} ")
                break
            else:
                fixed_die = set(die for die in rolls if rolls.count(die)> 1)
                # Check for duplicates
                if fixed_die:
                    print(" Duplicate found: ", fixed_die)
                    rolls = die_reroll(rolls, fixed_die)
                    user_choice = input("Another roll?(y or n):" )
                    if rolls[0] in fixed_die:
                        print("You rolled the same number as the duplicates. You TUPLED OUT!")
                        print(f"GAME OVER for {player.name} ")
                        break
                    if user_choice == "y":
                        rolls = die_reroll(rolls, fixed_die)
                score = sum(rolls)
                player.score += score
                print("Your score for this turn is: ", score)
                print("Total score:", player.score)
                
            if tupled_out(rolls):
                print(f" {player.name}'s turn is over")

tuple_game()