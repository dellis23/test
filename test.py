import unittest


class TestSamples(unittest.TestCase):

    def test_greater(self):
        self.assertGreater(4, 3)

    def test_in(self):
        self.assertIn("a", "apple")

    def test_instance(self):
        self.assertIsInstance("apple", basestring)

    def test_truth(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
