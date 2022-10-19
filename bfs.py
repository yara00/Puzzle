from queue import Queue
import State
import time


class Bfs:
    result = {}

    def __init__(self, initialState):
        self.state = initialState
        self.goalState = self.state.getGoalState()
        self.fringe = Queue()
        self.explored = set()
        self.parentMap = {}

    def algorithm(self):
        startTime = time.time()
        # append init state to fringe queue
        self.fringe.put(self.state.num)
        self.parentMap.update({self.state.num: -1})

        while not self.fringe.empty():
            currentStateNum = self.fringe.get()
            currentState = State.State(currentStateNum)
            # append current state to explored set
            self.explored.add(currentStateNum)
            # check goal state
            if currentState.isGoalState():
                break

            # expand current state node
            for neighbour in currentState.find_neighbours():
                if neighbour not in self.explored and neighbour not in self.fringe.queue:
                    # append neighbour to fringe queue
                    self.fringe.put(neighbour)
                    self.parentMap.update({neighbour: currentStateNum})

        # unsolvable case
        if self.goalState not in self.parentMap.keys():
            return False
        else:
            state = self.goalState
            path = []
            while state != -1:
                path.append(state)
                state = self.parentMap[state]

            path.reverse()
            endTime = time.time()
            result = dict({"Path": path, "Cost": len(path) - 1, "Expanded": len(self.explored) - 1,
                           "Depth": 0, "Time": endTime - startTime})
            return result


if __name__ == '__main__':
    s = State.State(125348670)
    bfs = Bfs(s)
    # startTime = time.time_ns()
    print(bfs.algorithm())
    #  endTime = time.time_ns()
    # print(endTime - startTime)
