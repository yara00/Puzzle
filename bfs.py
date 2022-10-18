from queue import Queue
import State


class Bfs:

    def __init__(self, initialState):
        self.state = initialState
        self.goalState = str(123456789).zfill(10)
        self.fringe = Queue()
        self.explored = set()

    #  self.neighbour = None

    # append the init state to fringe list
    def algorithm(self):
        self.fringe.put(self.state)
        while not self.fringe.empty():
            self.state = self.fringe.get()
            self.explored.add(self.state)
            print("expolored ")
            print(self.state)
            if self.goalState is self.state:
                return self.state
            for neighbour in self.state.find_neighbours():
                if neighbour not in self.fringe and self.explored:
                    self.fringe.put(neighbour)

        return False


if __name__ == '__main__':
    state = State.State()
    print("ana fe bfs now")
