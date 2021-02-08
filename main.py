import visualizer
import player
import random_player
import sequential_player
import most_common_player
import historian
import judge





continue_menu = True

while continue_menu:
    
    print("___________________    ___________________")
    print("===.--------.      \__/      .--------.===")
    print("    \___     \_____/  \_____/     ___/")
    print("        \__________\__/__________/")
    print("            Jørgen Menu 9000 \n \n")
    choice = input("0 for exit, 1 for ...: ")
    
    #Exit menu
    if choice == "0":
        print("0 detected, exiting menu...")
        continue_menu = False

        
    #Choice 1
    elif choice == "1":
        a = player.player("Jonas")
        print(a.name)
        b = random_player.random_player("Jørgen")
        b.select_action()
        b.print_current_choice()
        
    
    #Choice 2
    elif choice == "2":
        r = random_player.random_player("ronas")
        s = sequential_player.sequential_player("sonas")
        judy = judge.judge()
        
        for i in range(100):
            r.select_action()
            s.select_action()
            wiener = judy.decide_winner(r, s)
            judy.record_winner(wiener)
        
        times_square = visualizer.visualizer()
        times_square.winner_graph(judy)
        
    elif choice == "3":
        continue_tournament = True
        
        while continue_tournament:
            print("0 for exit")
            print("1 for random V sequential")
            print("2 for sequential V historian")
            print("3 for most common V historian")
            print("4 for sequential V histoian")
            t_choice = input("Your choice: ")
            
            if t_choice == "0":
                continue_tournament = False
            
            elif t_choice == "1":
                    r = random_player.random_player("ronas")
                    s = sequential_player.sequential_player("sonas")
                    judy = judge.judge()
                    for i in range(100):
                        r.select_action()
                        s.select_action()
                        wiener = judy.decide_winner(r, s)
                        judy.record_winner(wiener)
                        
                    times_square = visualizer.visualizer()
                    times_square.winner_graph(judy)

            elif t_choice == "2":
                s = sequential_player.sequential_player("sonas")
                h = historian.historian("honas")
                judy = judge.judge()
                
                for i in range(100):
                    s.select_action()
                    h.select_action()
                    wiener = judy.decide_winner(s, h)
                    judy.record_winner(wiener)
                        
                times_square = visualizer.visualizer()
                times_square.winner_graph(judy)
        
            elif t_choice == "3":
                c = most_common_player.most_common_player("conas")
                h = historian.historian("honas")
                judy = judge.judge()
                
                for i in range(100):
                    c.select_action()
                    h.select_action(c)
                    wiener = judy.decide_winner(c, h)
                    judy.record_winner(wiener)
                    
                times_square = visualizer.visualizer()
                times_square.winner_graph(judy)
                
            elif t_choice == "4":
                s = sequential_player.sequential_player("sonas")
                h = historian.historian("honas")
                judy = judge.judge()
                
                for i in range(100):
                    s.select_action()
                    h.select_action(s)
                    wiener = judy.decide_winner(s, h)
                    judy.record_winner(wiener)
                    
                times_square = visualizer.visualizer()
                times_square.winner_graph(judy)
                
                
            else:
                print("What? ._.")
    #Dump all inputs not recognized here
    else:
        print("Input not recognized")