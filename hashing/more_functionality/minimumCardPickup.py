"""
You are given an integer array cards where cards[i] represents the value of the ith card.
A pair of cards are matching if the cards have the same value.

Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards.
If it is impossible to have matching cards, return -1.


Example 1:
Input: cards = [3,4,2,3,4,7]
Output: 4

Example 2:
Input: cards = [1,0,5,3]
Output: -1


Constraints:
1 <= cards.length <= 105
0 <= cards[i] <= 106
"""

import math

def minimumCardPickupHashMap(cards: list[int]) -> int:
    
    output = math.inf
    hash_map = {}
    
    for i, c in enumerate(cards):
        if c in hash_map:
            output = min(output, i - hash_map[c] + 1)
            
        hash_map[c] = i
        
    return output if output < math.inf else -1