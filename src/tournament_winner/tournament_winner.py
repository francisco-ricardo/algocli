'''
The tournament is a competition to solve algorithmic problems as fast
as possible. Teams compete in a round robin, where each team faces off
against all other teams. Only two teams compete against each other at
a time, and for each competition, one team is designated the home team,
while the other team is the away team. In each competion there is always
one winner and one loser; there are no ties. A tem receives 3 points if
if wins and 0 points if is loses. The winner of the tournament is the 
team that receives the most amount of points.

'''

def tournamentWinner(competitions, results):
    '''
    Returns the winner of the tournament.

    The competitions array has elements in the form of 
    [home_team, away_team], where each team is a string representing
    the name of the team. The results array contains information
    about the winner of each corresponding competition in the 
    competitions array, where results[i] denotes the winner of
    competitions[i], where a 1 in the results array means that the
    home team in the corresponding competition won and a 0 means that
    the away team won.

    Parameters
    ----------
    competitions: array of competitions
    results: array of the results


    Approach
    ---------

    
    Time: O(n)
    Space: O(k)

    Notes
    -----
    - Following the Camel Case standard for naming functions and variables, 
      despite that the Snake Case is more common in Python coding.

    '''
    HOME_TEAM_WON = 1
    WINNER_POINTS = 3

    bestTeam = ''
    scoresDict = {bestTeam: 0}

    for i, competition in enumerate(competitions):
        result = results[i]
        homeTeam = competition[0]
        awayTeam = competition[1]

        if (result == HOME_TEAM_WON):
            winnerTeam = homeTeam
        else:
            winnerTeam = awayTeam
            
        if (winnerTeam not in scoresDict):
            scoresDict[winnerTeam] = 0
        
        scoresDict[winnerTeam] += WINNER_POINTS

        if (scoresDict[winnerTeam] > scoresDict[bestTeam]):
            bestTeam = winnerTeam

    return bestTeam

# EOF
