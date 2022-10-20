import unittest
import Controller


class TestInput(unittest.TestCase):
    def testDuplicateNumber(self):
        ctrl = Controller.Controller()
        self.assertEqual(ctrl.input_validation(123567880), False)

    def testNumberOutOfRange(self):
        ctrl = Controller.Controller()
        self.assertEqual(ctrl.input_validation(987654321), False)

    def testValidNumber(self):
        ctrl = Controller.Controller()
        self.assertEqual(ctrl.input_validation(102453678), True)


if __name__ == '__main__':
    unittest.main()
