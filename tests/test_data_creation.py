import unittest

from read_cistercian_with_cnn.data_creation import CistercianImageGenerator


class TestCistercianImageGenerator(unittest.TestCase):
    def test_sanity(self):
        cig = CistercianImageGenerator(batch_size=7, min_value=5, max_value=9, min_height=7, max_height=10,
                                       min_width=5, max_width=10)

        self.assertEqual(cig.batch_size, 7)
        self.assertEqual(cig.min_value, 5)
        self.assertEqual(cig.max_value, 9)
        self.assertEqual(cig.min_height, 7)
        self.assertEqual(cig.max_height, 10)
        self.assertEqual(cig.min_width, 5)
        self.assertEqual(cig.max_width, 10)
        self.assertEqual(cig.total_length, 5 * 4 * 6)
        self.assertEqual(len(cig), 18)


