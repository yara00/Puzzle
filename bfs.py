from queue import Queue
import State
import time


class Bfs:
    def __init__(self, initialState):
        self.state = initialState
        self.goalState = self.state.getGoalState()
        self.fringe = Queue()
        self.explored = set()
        self.parentMap = {}
        self.maxDepth = 0

    def getPath(self, state):
        path = []
        while state != -1:
            path.append(state)
            state = self.parentMap[state]
        return path

    def algorithm(self):
        startTime = time.time()
        # append init state to fringe queue
        currentStateNum = self.state.num
        pastStateNum = currentStateNum
        neighbour = 0
        self.fringe.put(currentStateNum)
        self.parentMap.update({self.state.num: -1})  # add root of parent map

        while not self.fringe.empty():
            currentStateNum = self.fringe.get()
            currentState = State.State(currentStateNum)
            self.explored.add(currentStateNum)  # append current state to explored set

            # check goal state
            if currentState.isGoalState():
                # compare goal state depth with past state's to get max depth
                path = self.getPath(currentStateNum)
                pastPath = self.getPath(pastStateNum)
                self.maxDepth = max(len(path), len(pastPath))
                path.reverse()
                endTime = time.time()
                return {"path": path, "cost": len(path) - 1, "maxDepth": self.maxDepth - 1,
                        "expanded": len(self.explored) - 1, "time": endTime - startTime}

            # expand current state node
            for neighbour in currentState.find_neighbours():
                if neighbour not in self.explored:
                    # append neighbour to fringe queue
                    self.fringe.put(neighbour)
                    self.parentMap.update({neighbour: currentStateNum})
            pastStateNum = neighbour  # keep track of last state
        # unsolvable case
        return {"path": [], "cost": 0, "maxDepth": 0, "expanded": 0, "time": 0}


if __name__ == '__main__':
    s = State.State(12345678)  # 125340678
    bfs = Bfs(s)
    print(bfs.algorithm())
