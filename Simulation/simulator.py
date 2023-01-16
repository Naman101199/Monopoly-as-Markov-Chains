def monop(finish_order=6,games_order=3):
     
    finish = 10**finish_order
    games = 10**games_order
     
    import random
    from random import shuffle
     
    squares = []
     
    while len(squares) < 40:
        squares.append(0)
     
    # roll values are values from a six by six grid for all dice rolls
    rollvalues = [2,3,4,5,6,7,3,4,5,6,7,8,4,5,6,7,8,9,5,6,7,8,9,10,6,7,8,9,10,11,7,8,9,10,11,12]
     
    games_finished = 0
     
    while games_finished < games:
         
        master_chest = [0,40,40,40,40,10,40,40,40,40,40,40,40,40,40,40]
        chest = [i for i in master_chest]
        shuffle(chest)
         
        master_chance = [0,24,11,'U','R',40,40,'B',10,40,40,5,39,40,40,40]
        chance = [i for i in master_chance]
        shuffle(chance)
         
        position = 0
         
        gos = 0
         
        while gos < finish:
             
            diceroll = int(36*random.random())
             
           
          
                 
            position = (position + rollvalues[diceroll])%40
                 
            if position in [7,22,33]:  # Chance
                chance_card = chance.pop(0)
                if len(chance) == 0:
                    chance = [i for i in master_chance]
                    shuffle(chance)
                if chance_card != 40:

                    if isinstance(chance_card,int):
                        position = chance_card
                    elif chance_card == 'U':
                        while position not in [12,28]:
                            position = (position + 1)%40
                    elif chance_card == 'R':
                        while position not in [5,15,25,35]:
                            position = (position + 1)%40
                    elif chance_card == 'B':
                        position = position - 3

            elif position in [2,17]:  # Community Chest
                chest_card = chest.pop(0)
                if len(chest) == 0:
                    chest = [i for i in master_chest]
                    shuffle(chest)
                if chest_card != 40:
                    position = chest_card

            if position == 30: # Go to jail
                position = 10


            squares.insert(position,(squares.pop(position)+1))
             
            gos += 1
         
        games_finished += 1
     
     
    return squares

a = monop()
print(a)

#a = [28744744, 21323351, 19353892, 22838898, 24300797, 27838685, 23466579, 10303023, 23401934, 23063912, 59094802, 27548789, 26512647, 24048061, 24903594, 27927199, 27917028, 25849127, 29295720, 30761546, 28742070, 28270466, 12207615, 27341178, 32041925, 28955696, 27198280, 26945057, 28279492, 26098951, 0, 26885668, 26279486, 11214438, 25062449, 25664471, 22532229, 21020493, 21026830, 25738878]
r = []
for i in a:
    ri = i/1000000000
    r.append(ri)
    
print(r)

