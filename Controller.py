import State
import bfs
import dfs
import astar


class Controller:
    def solve(self, method, initialState):
        state = State.State(initialState)

        if method == "bfs":
            result = bfs.Bfs(state).algorithm()
        elif method == "dfs":
            result = dfs.dfs(state).algorithm()
        elif method == "astar":
            result = astar.AStarSearch().findPathAndDetails(initialState)

        return result


if __name__ == '__main__':
    ctrl = Controller()
    print(ctrl.solve("bfs", 125348670))
    print("ana t7t el control now")
