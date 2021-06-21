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

