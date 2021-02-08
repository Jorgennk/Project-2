

class player:
    
    def __init__(self, name):
        self.possible_choices = ["Stone", "Scissors", "Paper"]
        self.current_choice = "Undecided"
        self.opponent_choices = []
        self.name = name
        
    def print_current_choice(self):
        print(self.current_choice)
        
        