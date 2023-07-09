"""
You are given an integer array matches where matches[i] = [winner_i, loser_i] indicates that the player winner_i defeated player loser_i in a match.

Return a list answer of size 2 where:

    - answer[0] is a list of all players that have not lost any matches.
    - answer[1] is a list of all players that have lost exactly one match.

The values in the two lists should be returned in increasing order.

Note:
You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.


Example 1:
Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]

Example 2:
Input: matches = [[2,3],[1,3],[5,4],[6,4]]
Output: [[1,2,5,6],[]]


Constraints:
1 <= matches.length <= 105
matches[i].length == 2
1 <= winneri, loseri <= 105
winneri != loseri
All matches[i] are unique.
"""

from collections import defaultdict

def findWinners(matches: list[list[int]]) -> list[int]:

    no_loss = []
    one_loss = []
    players = set()
    losses = defaultdict(int)

    for winner, loser in matches:
        players.add(winner)
        players.add(loser)

        losses[loser] += 1

    for player in players:
        loss_count = losses[player]

        if loss_count == 0:
            no_loss.append(player)
            
        elif loss_count == 1:
            one_loss.append(player)

    return [sorted(no_loss), sorted(one_loss)]