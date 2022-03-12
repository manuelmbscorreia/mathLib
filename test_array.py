import unittest2
import calc

class TestArray(unittest2.TestCase):

    def test_lenght(self):
        result = calc.size_array([1, 3, 2, 5, 4])
        self.assertEquals(result, 5)

    def test_max(self):
        result = calc.max_array([-1, 3, 2, 5, 4])
        self.assertEquals(result, 5)

    def test_min(self):
        result = calc.min_array([-1, 3, 2, 5, 4])
        self.assertEquals(result, -1)

    def test_avg(self):
        result = calc.avg_array([-1, 3, 2, 5, 4])
        self.assertEquals(result, 2.6)

    def test_std(self):
        result = calc.std_array([-1, 3, 2, 5, 4])
        self.assertEquals(result, 2.059)

    def test_asc(self):
        result = calc.asc_array([-1, 3, 2, 5, 4])
        self.assertEquals(result, [-1, 2, 3, 4, 5])

    def test_desc(self):
        result = calc.desc_array([-1, 3, 2, 5, 4])
        self.assertEquals(result, [5, 4, 3, 2, -1])

    def test_reverse(self):
        result = calc.reverse_array([-1, 3, 2, 5, 4])
        self.assertEquals(result, [4, 5, 2, 3, -1])
