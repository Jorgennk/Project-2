from player import player
import random

class historian(player):
        
    def __init__(self, name):
        super().__init__(name)
    
    
    def is_sequential(self):
        
        
        confidence = 0
        iterator = 0
        
        if not self.opponent_choices:
            return 0
        else:

            for choice in self.opponent_choices:
                if iterator%3 == 0:
                    if choice == "Rock":
                        confidence += 1
                    else:
                        confidence -= 1

                elif iterator%3 == 1:
                    if choice == "Scissors":
                        confidence += 1
                    else:
                        confidence -= 1
                        
                elif iterator%3 == 2:
                    if choice == "Paper":
                        confidence += 1
                    else:
                        confidence -= 1
                        
                iterator += 1
                
                return confidence / iterator
            
                
    
    
    
    def is_most_common(self):
        
        
        
        count = [0, 0, 0]
        iterator = 0
        confidence = 0
        tmp_list = []
        
        if not self.opponent_choices:
            self.current_choice = random.choice(self.possible_choices)
        else:
            for choice in self.opponent_choices:
                
                #Prediction part
                
                confidence_on_player = max(count)
                index_of_confidence_on_player = count.index(confidence_on_player)

                if index_of_confidence_on_player == 0:
                    common_wants = "Paper"

                elif index_of_confidence_on_player == 1:
                    common_wants = "Rock"

                elif index_of_confidence_on_player == 2:
                    common_wants = "Scissors"
                    
#----------------- Separation line ----------------------
                if common_wants == choice:
                    confidence += 1
                else:
                    confidence -= 1
                
                
#--------- Update the info on current choice -------------
                if choice == "Rock":
                    count[0] += 1
                
                elif choice == "Scissors":
                    count[1] += 1

                elif choice == "Paper":
                    count[2] += 1

#Update the iterator keeping count of how many times run
                iterator += 1    
 
        if not iterator == 0:
            return confidence / iterator
        else:
            return 0
        
    def beat_sequential(self, opponent):
        if not opponent.opponent_choices:
            self.current_choice = random.choice(self.possible_choices)
            
        
        else:
            last = self.opponent_choices[-1]
            
            if last == "Rock":
                self.current_choice = "Rock"
                
            elif last == "Scissors":
                self.current_choice = "Scissors"
                
            elif last == "Paper":
                self.current_choice = "Paper"
        
        
        
    def beat_common(self, opponent):
        
        count = [0, 0, 0]
        
        if not opponent.opponent_choices:
            pass
        else:
            

            for choice in opponent.opponent_choices:
                if choice == "Rock":
                    count[0] += 1
                
                elif choice == "Scissors":
                    count[1] += 1

                elif choice == "Paper":
                    count[2] += 1
                    
            confidence_on_player = max(count)
            index_of_confidence_on_player = count.index(confidence_on_player)
            
            if index_of_confidence_on_player == 0:
                common_wants = "Paper"
                
            elif index_of_confidence_on_player == 1:
                common_wants = "Rock"
                
            elif index_of_confidence_on_player == 2:
                common_wants = "Scissors"
                
        #Now beat it >:D
        
        if common_wants == "Paper":
            self.current_choice = "Scissors"
            
        elif common_wants == "Rock":
                self.current_choice = "Paper"
                
        elif common_wants == "Scissors":
            self.current_choice = "Rock"
            
            
    def beat_random(self):
        """
        Can't really find a strategy to beat randomness can you?
        If you cant beat it, join it
        """
        self.current_choice = random.choice(self.possible_choices)
        
        
    def select_action(self, opponent):
        
        confidence_levels = [0, 0, 0]
        confidence_levels[0] += self.is_sequential()
        confidence_levels[1] += self.is_most_common()
        print(confidence_levels)
  
        confidence_on_player = max(confidence_levels)
        index = confidence_levels.index(confidence_on_player)
        print(index)
        
        if index == 0:
            self.beat_sequential(opponent)
        elif index == 1:
            self.beat_common(opponent)
        else:
            self.beat_random()