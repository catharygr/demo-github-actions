import unittest
from suma import sumar

class TestSumar(unittest.TestCase):

  def test_sumar(self):
    self.assertEqual(sumar(3, 2), 5)
    self.assertEqual(sumar(-1, 1), 0)
    self.assertEqual(sumar(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()