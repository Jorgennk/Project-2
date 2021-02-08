import player


class judge:
    
    def __init__(self):
        self.winner_history = []
        self.winner_choices = []
        self.participants = []
        
        
    #
    def decide_winner(self, player1, player2):
        
        self.participants.append(player1.name)
        self.participants.append(player2.name)
        
        player1.opponent_choices.append(player2.current_choice)
        player2.opponent_choices.append(player1.current_choice)
        
        if player1.current_choice == player2.current_choice:
            self.winner = None
            return None
            
        if player1.current_choice == "Rock":
            if player2.current_choice == "Paper":
                return player2
            elif player2.current_choice == "Scissors":
                return player1
            
        if player1.current_choice == "Scissors":
            if player2.current_choice == "Rock":
                return player2
            elif player2.current_choice == "Paper":
                return player1
            
            
        if player1.current_choice == "Paper":
            if player2.current_choice == "Scissors":
                return player2
            elif player2.current_choice == "Rock":
                return player1
            
            
    def record_winner(self, player):
        
        if not player == None:
            self.winner_history.append(player.name)
            self.winner_choices.append(player.current_choice)
        
        
    def reset(self):
        self.winner_history = []
        self.winner_choices = []
        
            