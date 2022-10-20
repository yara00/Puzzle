import State
import time
from collections import deque


class dfs:

    def __init__(self, initialState):
        self.state = initialState
        self.goalState = self.state.getGoalState()
        self.frontier = deque() #stack
        self.explored = set()
        self.parentMap = {}
        self.TempNeighbours = []


    def get_path_and_cost(self,searchState):
        state = searchState
        path = []
        while state != -1:
            path.append(state)
            state = self.parentMap[state]

        path.reverse()
        return path , len(path)-1

    def get_Max_depth(self):
       maxDepth = -10
       print(self.parentMap.keys())
       print(self.parentMap.values())
       leafNodes = set(self.parentMap.keys()).difference(self.parentMap.values())
       print(leafNodes)

       for leaf in leafNodes:
           x, depth = self.get_path_and_cost(leaf)
           maxDepth = max(maxDepth,depth+1)

       return maxDepth


    def algorithm(self):
        start = time.time()
        self.frontier.append(self.state.num)
        self.parentMap.update({self.state.num: -1})

        while self.frontier:
            currentNum = self.frontier.pop()
            currentState = State.State(currentNum)
            self.explored.add(currentNum)
          #  print("Current state number is >>", currentNum)

            if currentState.isGoalState():
                path, cost = self.get_path_and_cost(self.goalState)
                maxDepth = self.get_Max_depth()
                end= time.time()
                print(self.parentMap)
                return {"path": path, "cost": cost, "maxDepth": maxDepth, "expanded": len(self.explored), "time": end-start}

            for neighbour in currentState.find_neighbours():
                if neighbour not in self.frontier:
                    if neighbour not in self.explored:
                        self.TempNeighbours.append(neighbour)

            while self.TempNeighbours:
                temp = self.TempNeighbours.pop()
                self.frontier.append(temp)
                self.parentMap.update({temp: currentNum})

        maxDepth = self.get_Max_depth()
        end = time.time()
        return  {"path": [], "cost": 0, "maxDepth": maxDepth, "expanded": len(self.explored), "time": end-start}



if __name__ == '__main__':
    print("DFS")
    s = State.State(142305678) #182043765        125340678       312045678
    search = dfs(s)
    print( search.algorithm())
  #  search.algorithm()
  #  search.get_Max_depth()