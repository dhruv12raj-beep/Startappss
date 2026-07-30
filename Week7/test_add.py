import unittest

from demo import *

# class TestAdd(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(add(2,4),6)

#     def test_sub(self):
#         self.assertEqual(sub(7,3),4)

#     def test_string(self):
#         self.assertRegex("demo@gmail.com",r".+gmail\.com" )


# if __name__ == "__main__":
#     unittest.main()

def test_add():
    assert add(2,4)== 6


def test_sub():
    assert sub(6,2)==3


#parameterized tests: test multipple inputs
import pytest

@pytest.mark.parametrize("a,b,result",[

    (2,4,6),
    (2,4,6),
    (2,4,6),
    (2,4,6),
    (2,4,6),
    (2,4,6)
])

def test_add(a,b,result):
    assert add(a,b) ==result

# uses of pytest
'''pytest for entire test , pytest filename, pytest --lf , ptest x : stops after first failure
fixture: fixture provides reusable setup code before tests executes     '''