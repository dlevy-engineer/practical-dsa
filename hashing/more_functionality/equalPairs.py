"""
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).


Example 1:
Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1

Example 2:
Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3


Constraints:
n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 105
"""

def equalPairs(grid: list[list[int]]) -> int:

    # our strategy for solving this problem will rely on hash maps, but lists are mutable, and therefore are not hashable
    # so we define a simple function for converting lists to tuples
    def convert_to_key(arr):
        return tuple(arr)
    
    # we're going to need two hashmaps, one for row frequencies and one for column frequencies
    row_dic = {}
    col_dic = {}

    # instantiate an output variable
    output = 0

    # instantiate the column count and a grid for storing column values
    n_col = len(grid[0])
    cols = [[] for _ in range(n_col)]

    # now we do the work of constructing our hash maps
    for row in grid:
        # convert the row to a key and increment its corresponding value
        row_key = convert_to_key(row)
        row_dic[row_key] = row_dic.get(row_key, 0) + 1

        for col in range(n_col):
            cols[col].append(row[col])

    for col in cols:
        col_key = convert_to_key(col)
        col_dic[col_key] = col_dic.get(col_key, 0) + 1

    print(f'Rows: {row_dic}')
    print(f'Columns {col_dic}')
    for key in row_dic:
        output += row_dic[key] * col_dic.get(key, 0)

    return output