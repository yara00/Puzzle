import State
import time
from collections import deque


class dfs:

    def __init__(self, initialState):
        self.state = initialState
        self.goalState = self.state.getGoalState()
        self.frontier = deque()                         # stack
        self.explored = set()                           # set of all expanded nodes
        self.parentMap = {}
        self.TempNeighbours = []
        self.maxDepth = 0

# function take a state and backtrack in the parentMap with this state to get the path from the intial state to this searchState
# return the path and the cost
    def get_path_and_cost(self, searchState):
        state = searchState
        path = []
        while state != -1:
            path.append(state)
            state = self.parentMap[state]

        path.reverse()
        return path, len(path) - 1

    def algorithm(self):
        start = time.time()

        # start with the intial state in the frontier and in the parent map
        self.frontier.append(self.state.num)
        self.parentMap.update({self.state.num: -1})
        depth = 0

        while self.frontier:
            currentNum = self.frontier.pop()
            currentState = State.State(currentNum)
            self.explored.add(currentNum)
            self.maxDepth = max(depth, self.maxDepth)

            # solvable Case
            if currentState.isGoalState():
                path, cost = self.get_path_and_cost(self.goalState)
                self.maxDepth = max(len(path) - 1, self.maxDepth)
                end = time.time()
                return {"path": path, "cost": cost, "maxDepth": self.maxDepth, "expanded": len(self.explored) - 1,
                        "time": end - start}

            flag = True                     # to satisfy the depth
            for neighbour in currentState.find_neighbours():
                if neighbour not in self.explored :

                        self.TempNeighbours.append(neighbour)
                        flag = False

            if flag:
                depth = depth - 1
            else:
                depth = depth + 1

            while self.TempNeighbours:              # reverse the states to maintain the same strategy
                temp = self.TempNeighbours.pop()
                self.frontier.append(temp)
                self.parentMap.update({temp: currentNum})


        # unsolvable Case
        end = time.time()
        return {"path": [], "cost": 0, "maxDepth": self.maxDepth, "expanded": len(self.explored), "time": end - start}


if __name__ == '__main__':
    print("DFS")
    s = State.State(125340678)  # 182043765        125340678       312045678
    search = dfs(s)
    print(search.algorithm())

