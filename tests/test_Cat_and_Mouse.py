import unittest
from Cat_and_Mouse.Cat_and_Mouse import Cat_and_Mouse

class TestCatAndMouse(unittest.TestCase):
    
    def test_cat_b(self):
        self.assertEqual(Cat_and_Mouse(1, 2, 3), "Cat B")

    def test_mouse_c(self):
        self.assertEqual(Cat_and_Mouse(1, 3, 2), "Mouse C")

    def test_cat_b_again(self):
        self.assertEqual(Cat_and_Mouse(1, 5, 4), "Cat B")

if __name__ == '__main__':
    unittest.main()
