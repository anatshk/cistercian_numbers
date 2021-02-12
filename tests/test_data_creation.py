import unittest
import numpy as np

from read_cistercian_with_cnn.data_creation import CistercianImageGenerator


class TestCistercianImageGenerator(unittest.TestCase):
    def test_sanity(self):
        cig = CistercianImageGenerator(batch_size=7, min_value=5, max_value=9, min_height=7, max_height=10,
                                       min_width=5, max_width=10, network_input_size=28)

        self.assertEqual(cig.batch_size, 7)
        self.assertEqual(cig.list_of_values, [5, 6, 7, 8, 9])
        self.assertEqual(cig.list_of_heights, [7, 8, 9, 10])
        self.assertEqual(cig.list_of_widths, [5, 6, 7, 8, 9, 10])
        self.assertEqual(cig.network_input_size, 28)
        self.assertEqual(len(cig), 18)

    def test_init_specific_ranges(self):
        list_of_values = [100, 5087, 3425, 12, 54, 765]
        list_of_heights = [7, 45, 13, 8, 20, 12, 5]
        list_of_widths = [5, 13, 14, 16, 23, 50]
        cig = CistercianImageGenerator(batch_size=7, list_of_values=list_of_values, list_of_heights=list_of_heights,
                                       list_of_widths=list_of_widths, network_input_size=28)

        self.assertEqual(cig.batch_size, 7)
        self.assertEqual(cig.list_of_values, sorted(list_of_values))
        self.assertEqual(cig.list_of_heights, sorted(list_of_heights))
        self.assertEqual(cig.list_of_widths, sorted(list_of_widths))
        self.assertEqual(cig.network_input_size, 28)
        self.assertEqual(len(cig), len(list_of_values) * len(list_of_heights) * len(list_of_widths) // 7)

    def test_create_all_permutations(self):
        cig = CistercianImageGenerator(batch_size=7, min_value=5, max_value=6, min_height=9, max_height=10,
                                       min_width=8, max_width=10)

        expected_y = np.array([5, 5, 5, 6, 6, 6, 5, 5, 5, 6, 6, 6])

        expected_x_dims = [
            (9, 8),
            (9, 9),
            (9, 10),
            (9, 8),
            (9, 9),
            (9, 10),
            (10, 8),
            (10, 9),
            (10, 10),
            (10, 8),
            (10, 9),
            (10, 10),
        ]

        np.testing.assert_array_equal(expected_y, cig.y)
        self.assertEqual(expected_x_dims, cig.x_dims)

    def test_create_x_arrays_for_training(self):
        cig = CistercianImageGenerator(batch_size=2, network_input_size=16, list_of_heights=[7, 17, 30],
                                       list_of_widths=[5, 15, 50])
        batch_x = cig._create_x_arrays_for_training(numbers=np.array([1, 2004, 389, 54]),
                                                    dimension_tuples=[(7, 5), (17, 15), (30, 50), (7, 5)])

        self.assertEqual(batch_x.shape, (16, 16, 4))
        # the images returned here were visually examined to show that they make sense
