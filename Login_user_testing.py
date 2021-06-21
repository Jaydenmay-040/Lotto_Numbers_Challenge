import unittest
from Login_user import lotto
import random
import rsaidnumber
from dateutil import relativedelta
from datetime import datetime


class Testing Lotto(unittest.TestCase):
    def test_compare(self):
        instance = lotto()
# instantiation
        a = [1, 2, 2]
        b = [1, 2, 3]
        self.assertEqual(2, instance.compare(a,b))
    
    def test_random(self):
        rand_num = random.randint(1, 49)
        self.assertTrue(0 < rand_num < 50, "Random value not in range 1-49")

    def test_rsa_id(self):
        id_pass = rsaidnumber.parse("0211015147088")
        self.assertTrue(id_pass, "ID should return true")

    def test_age(self):
        id_number = rsaidnumber.parse("0211015147088")
        age = relativedelta.relativedelta(datetime.today(), id_number.date_of_birth).years
        self.assertTrue(age >= 18, "Should return true")


if __name__ == '__Login_user__':
    unittest.Login_user()
