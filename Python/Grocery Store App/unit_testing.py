import unittest
from class_file import StoreInfo, ShoppingList


class TestStoreInfo(unittest.TestCase):

    def setUp(self):
        print("SETUP")

    def tearDown(self):
        print("TEARDOWN")

    def test_one(self):
        location = True
        address = True
        self.assertEqual(location, True)
        self.assertEqual(address, True)


class TestShoppingList(unittest.TestCase):

    def test_two(self):
        name = True
        price = True
        self.assertEqual(name, True)
        self.assertEqual(price, True)


if __name__ == "__main__":
    unittest.main()


#
