import unittest
import vim_output as sut


@unittest.skip("Don't forget to test!")
class VimOutputTests(unittest.TestCase):

    def test_example_fail(self):
        result = sut.vim_output_example()
        self.assertEqual("Happy Hacking", result)
