#

class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        target = '123450'
        start = ''.join(str(i) for tiles in board for i in tiles)
        
        moves = [[1,3],[0,2,4],[1,5],[0,4],[1,3,5],[2,4]]
        
        current_level, next_level = [start], []
        result = 0
        visited = set()
        
        while current_level:
            for state in current_level:
                if state == target:
                    return result
                i = state.index('0')
                for move in moves[i]:
                    new_state = list(state)
                    new_state[i], new_state[move] = new_state[move], new_state[i]
                    new_state = ''.join(new_state)
                    if new_state not in visited:
                        next_level.append(new_state)
                        visited.add(new_state)
            result += 1
            current_level, next_level = next_level, []
        return -1
