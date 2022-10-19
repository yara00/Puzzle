import unittest
import State
import astar

class TestAStar(unittest.TestCase):
    def testSimpleCasePathLength(self):
        search = astar.AStarSearch()
        result = search.findPathAndDetails(102345678)
        self.assertEqual(len(result["path"])-1,1,"Should be one path") # -1 is added because path with 6 states have 5 steps

    def testSimpleCaseLastNodeInPath(self):
        search = astar.AStarSearch()
        result = search.findPathAndDetails(102345678)
        self.assertEqual(result["path"][-1],State.State(0).getGoalState(),"Last node should be goal state")

    def testInfiniteCasePathLength(self):
        search = astar.AStarSearch()
        result = search.findPathAndDetails(812043765)
        self.assertEqual(len(result["path"]),0,"Path list should be empty")

    def testStartingWithGoalCase(self):
        search = astar.AStarSearch()
        result = search.findPathAndDetails(12345678)
        self.assertEqual(len(result["path"]), 1, "Path list should contain only goal node")



if __name__ == '__main__':
    unittest.main()