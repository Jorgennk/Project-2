import random
from player import player



class random_player(player):
    
    
    def __init__(self, name):
        super().__init__(name)
    
    def select_action(self):
        self.current_choice = random.choice(self.possible_choices)
        
    
        
        

        
        
