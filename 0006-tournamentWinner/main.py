competitions = [
  ["AlgoMasters", "FrontPage Freebirds"],
  ["Runtime Terror", "Static Startup"],
  ["WeC#", "Hypertext Assassins"],
  ["AlgoMasters", "WeC#"],
  ["Static Startup", "Hypertext Assassins"],
  ["Runtime Terror", "FrontPage Freebirds"],
  ["AlgoMasters", "Runtime Terror"],
  ["Hypertext Assassins", "FrontPage Freebirds"],
  ["Static Startup", "WeC#"],
  ["AlgoMasters", "Static Startup"],
  ["FrontPage Freebirds", "WeC#"],
  ["Hypertext Assassins", "Runtime Terror"],
  ["AlgoMasters", "Hypertext Assassins"],
  ["WeC#", "Runtime Terror"],
  ["FrontPage Freebirds", "Static Startup"]
]
results = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]




def tournamentWinner(competitions, results):
    if len(competitions) != len(results):
        return ''
    winner = {}
    for win in range(len(results)):
        if results[win] == 0:
            # list[1]  yutgan
            win_value=competitions[win][1]
            if win_value not in winner:
                winner[win_value] = 1
            else:
                winner[win_value] +=1
        else:
            # list[1]  yutgan
            win_value=competitions[win][0]
            if win_value not in winner:
                winner[win_value] = 1
            else:
                winner[win_value] +=1
    return max(winner, key=winner.get)


print(tournamentWinner(competitions,results))


# optimalroq 


def tournamentWinner(competitions, results):
    winner = {}
    for win in range(len(results)):
        if results[win] == 0:
            win_value=competitions[win][1]
        else:
            win_value=competitions[win][0]


        winner[win_value] = winner.get(win_value, 0) + 1 
    return max(winner, key=winner.get)


print(tournamentWinner(competitions,results))



def tournamentWinner(competitions, results):
    points = {}
    for (home, away), res in zip(competitions, results):
        winner = away if res == 0 else home
        points[winner] = points.get(winner, 0) + 1
    return max(points, key=points.get)