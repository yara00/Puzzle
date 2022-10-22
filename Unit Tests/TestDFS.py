import unittest
import State
import dfs

class TestDFS(unittest.TestCase):



    def testUnsolvablePuzzle(self):
        state = State.State(812043765)
        result = dfs.dfs(state).algorithm()
        self.assertEqual(result["path"], [], "unsolvable puzzle path should be empty")

        state = State.State(125340678)
        result = dfs.dfs(state).algorithm()
        self.assertEqual(result["cost"], 3, "Cost = 3")


if __name__ == '__main__':
    unittest.main()
