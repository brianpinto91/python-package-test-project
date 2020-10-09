import unittest
from statsdistribbrian._base import Base

class TestBase(unittest.TestCase):

    def test_initialization_no_data(self):
        base = Base()
        self.assertIsNone(base.data, msg="Expected empty object data when no data is passed")

    def test_invalid_data(self):
        base = Base({'a':1,'b':2}) #test passing a dictionary instead of a list
        self.assertIsNone(base.data, msg="Expected empty object data when wrong data is passed")

    def test_init_file_data_empty(self):
        base = Base("data_empty.txt")
        self.assertIsNone(base.data, msg="Expected empty object data when no data in file")

    def test_init_file_data_non_empty(self):
        base = Base("data.txt")
        data = [29.0, 5.0, 16.0, -114.0, 169.0, 74.0, -3.0, 6.0, -198.0, 29.0]
        self.assertCountEqual(base.data, data, "Data was not correctly read from the file")

    def test_init_list_data_non_empty(self):
        data = [29.0, 5.0, 16.0, -114.0, 169.0, 74.0, -3.0, 6.0, -198.0, 29.0]
        base = Base(data)
        self.assertCountEqual(base.data, data, "Data was not correctly read from the list")

    def test_add_data_method_1(self):
        #test add_data when the instance was intially created with data
        data = [29.0, 5.0, 16.0, -114.0, 169.0, 74.0, -3.0, 6.0, -198.0, 29.0]
        base = Base(data)
        base.add_data(data)
        self.assertCountEqual(base.data, data, "Data was not correctly read from the list")

    def test_add_data_method_2(self):
        #test add_data when the instance was intially created without data
        data = [29.0, 5.0, 16.0, -114.0, 169.0, 74.0, -3.0, 6.0, -198.0, 29.0]
        base = Base()
        base.add_data(data)
        self.assertCountEqual(base.data, data, "Data was not correctly read from the list")

if __name__ == "__main__":
    unittest.main()
