import matplotlib.pyplot as plt
import time
import judge

#x = list(range(0,10))
#y = list(range(-10,0))
#
#plt.plot(x,y)
#plt.show()
#
#time.sleep(5)

class visualizer:
    
    def __init__(self):
        pass
    
    
    def winner_graph(self, judge):
        p1 = judge.participants[0]
        p2 = judge.participants[1]
        
        p1c= 0
        p2c = 0
        x_axis = list(range(0, len(judge.winner_history)))
        y_axis = []
        
        if not judge.winner_history:
            print("Empty winner history")
            return None
        else:
            
            for winner in judge.winner_history:
                if winner == p1:
                    p1c += 1
                elif winner == p2:
                    p2c += 1
                    
        num_of_wins = max(p1c, p2c)
        
        if num_of_wins == p1c:
            series_winner = p1
        else:
            series_winner = p2
            
        #Build the graph
        
        if not judge.winner_history:
            print("Empty winner history")
            return None
        else:
            
            iterator = 0
            wins = 0
            for winner in judge.winner_history:
                if winner == series_winner:
                    wins += 1
                iterator += 1
                y_axis.append(wins/iterator)
                
        plt.xlabel("Number of mathes with a winner")
        plt.ylabel("Win graph of the winner: " + series_winner)
        plt.plot(x_axis, y_axis, "k-")
        plt.show()