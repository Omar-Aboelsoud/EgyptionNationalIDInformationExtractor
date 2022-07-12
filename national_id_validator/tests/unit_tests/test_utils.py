from django.test import TestCase
from ...utils import (
    nid_get_month,
    nid_get_day,
    nid_get_governate_code,
    nid_get_birth_century
)


class TestUtils(TestCase):
    def tearDown(self):
        pass

    def setUp(self):
        pass

    def test_nid_get_month(self):
        """
        Test extracting month from nid get index [3:5]
        """
        # Given
        nid_number = '29203022300145'
        # When
        month = nid_get_month(nid_number)
        # Then
        self.assertEqual(month, 3)

    def test_nid_get_day(self):
        """
        Test extracting day from nid get index [5:7]
        """
        # Given
        nid_number = '29203022300145'
        # When
        day = nid_get_day(nid_number)
        # Then
        self.assertEqual(day, 2)

    def test_get_governate_code(self):
        """
        Test extracting governate code from nid get index [7:9] from nid
        """
        # Given
        nid_number = '29203022300145'
        # When
        get_governate_code = nid_get_governate_code(nid_number)
        # Then
        self.assertEqual(get_governate_code, '02')

    def test_get_governate_code(self):
        """
        Test extracting birth century from nid get index [0] from nid + 17
        """
        # Given
        nid_number = '29203022300145'
        # When
        get_governate_code = nid_get_birth_century(nid_number)
        # Then
        self.assertEqual(get_governate_code, 19)
