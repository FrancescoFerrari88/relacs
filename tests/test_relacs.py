import unittest
from relacs import relacs as rl

class testCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(rl.add_nums(10,5),15.0)
        self.assertEqual(rl.add_nums(-1,1),0.0)
        self.assertEqual(rl.add_nums(-1,-1),-2.0)

    def test_divide(self):
        self.assertEqual(rl.divide_nums(10,5),2)
        self.assertEqual(rl.divide_nums(-1,1),-1)
        self.assertEqual(rl.divide_nums(-1,-1),1)
        self.assertEqual(rl.divide_nums(5,2),2.5)

# test for errors to be correctly raised
        self.assertRaises(ValueError, rl.divide_nums, 5, 0)
        with self.assertRaises(ValueError):
            rl.divide_nums(5, 0)

class testEmployee(unittest.TestCase):

    def setUp(self):
        self.emp1 = rl.Employees("Francesco","Ferrari",1000)
        self.emp2 = rl.Employees("ANGELICA","gRAY",1000)

    def tearDown(self):
        pass

    def test_email(self):
        self.assertEqual(self.emp1.email, "ferrari@ie-freiburg.mpg.de")
        self.assertEqual(self.emp2.email, "gray@ie-freiburg.mpg.de")


if __name__ == "__main__":
    unittest.main()
