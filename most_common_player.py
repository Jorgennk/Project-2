from player import player
import random
"""
Please pylint....

"""


class most_common_player(player):
    
    
    def __init__(self, name):
        super().__init__(name)
    
    
    def select_action(self):
        count = [0, 0, 0]
        
        
        if not self.opponent_choices:
            self.current_choice = random.choice(self.possible_choices)
        else:

            for choice in self.opponent_choices:
                if choice == "Rock":
                    count[0] += 1
                
                elif choice == "Scissors":
                    count[1] += 1

                elif choice == "Paper":
                    count[2] += 1
                    
            most_chosen = max(count)
            index_of_most_chosen = count.index(most_chosen)
            
            if index_of_most_chosen == 0:
                self.current_choice = "Paper"
                
            elif index_of_most_chosen == 1:
                self.current_choice = "Rock"
                
            elif index_of_most_chosen == 2:
                self.current_choice = "Scissors"