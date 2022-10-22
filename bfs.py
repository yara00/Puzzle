from queue import Queue
import State
import time


class Bfs:
    def __init__(self, initialState):
        self.state = initialState
        self.goalState = self.state.getGoalState()
        self.fringe = Queue()
        self.fringeDict = {}
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
        self.fringeDict[currentStateNum] = 1
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
                if neighbour not in self.explored and neighbour not in self.fringeDict.keys():
                    # append neighbour to fringe queue
                    self.fringe.put(neighbour)
                    self.fringeDict[neighbour] = 1
                    self.parentMap.update({neighbour: currentStateNum})

            pastStateNum = neighbour  # keep track of last state

        # unsolvable case
        path = self.getPath(currentStateNum)
        self.maxDepth = len(path) - 1
        return {"path": [], "cost": 0, "maxDepth": self.maxDepth,
                "expanded": len(self.explored), "time": time.time() - startTime}


if __name__ == '__main__':
    s = State.State(812043765)  # 125340678 182043765 #812043765
    bfs = Bfs(s)
    print(bfs.algorithm())
