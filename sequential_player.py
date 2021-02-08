from player import player


class sequential_player(player):
    
    
    def __init__(self, name):
        super().__init__(name)


    def select_action(self):
            
        if self.current_choice == "Undecided":
            self.current_choice = "Rock"
                
        elif self.current_choice == "Rock":
            self.current_choice = "Scissors"

        elif self.current_choice == "Scissors":
            self.current_choice = "Paper"
            
        elif self.current_choice == "Paper":
            self.current_choice = "Rock"
    