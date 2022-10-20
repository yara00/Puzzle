import unittest
import State
import bfs


class TestBFS(unittest.TestCase):
    def testUnsolvablePuzzle(self):
        state = State.State(812043765)
        result = bfs.Bfs(state).algorithm()
        self.assertEqual(result["path"], [], "unsolvable puzzle path should be empty")

    def testInitialGoalState(self):
        state = State.State(12345678)
        result = bfs.Bfs(state).algorithm()
        self.assertEqual(result["path"][-1], state.getGoalState(), "path should contain goal state only")

    def testMaxDepth(self):
        state = State.State(125340678)
        result = bfs.Bfs(state).algorithm()
        self.assertEqual(result["maxDepth"], result["cost"] + 1, "max depth should be greater than search depth by 1")


if __name__ == '__main__':
    unittest.main()
