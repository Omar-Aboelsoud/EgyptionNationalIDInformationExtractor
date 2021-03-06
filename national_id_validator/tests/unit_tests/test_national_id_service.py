from django.test import TestCase
from national_id_validator.services import NIDService
from national_id_validator.utils import nid_validation
from django.core.exceptions import ValidationError


class TestNIDValidator(TestCase):
    def tearDown(self):
        pass

    def setUp(self):
        self.nid_number = '29203022300145'

    def test_get_national_id_information(self):
        """
        Test get_national_id_information get the correct info from ID number
        """
        # Given
        nid_service = NIDService()
        # When
        extracted_data = nid_service.get_national_id_information(
            nid=self.nid_number)
        # Then
        self.assertEqual(str(extracted_data.__dict__.get("birthdate")),
                         "1992-03-02")
        self.assertEqual(extracted_data.__dict__.get("governorate"), "Fayoum")
        self.assertEqual(extracted_data.__dict__.get("gender"), "female")

    def test_get_gender(self):
        """
        Test get_gender that returns the gender based on the index 12 if it is even number then it is female
        """
        # Given
        nid_service = NIDService()
        nid_number_male = self.nid_number.replace("4", "5")
        # When
        gender_female = nid_service._NIDService__get_gender(
            nid=self.nid_number)
        gender_male = nid_service._NIDService__get_gender(nid=nid_number_male)
        # Then
        self.assertEqual(gender_female, "female")
        self.assertEqual(gender_male, "male")


class TestNidValidation(TestCase):
    def tearDown(self):
        pass

    def setUp(self):
        pass

    def test_pass_char_to_nid_validation(self):
        """
        On passing a charcter to nid_validation an error should be raised
        """
        # Given
        nid = "a9203022300145"
        # When, Then
        with self.assertRaisesMessage(ValidationError, "national id should only contain integers"):
            nid_validation(nid=nid)

    def test_pass_first_number_zero(self):
        """
        On passing a zero as leading number in nid
        """
        # Given
        nid = "09203022300145"
        # When, Then
        with self.assertRaisesMessage(ValidationError, "leading number of national id may not be 0"):
            nid_validation(nid=nid)

    def test_pass_more_than_14_charcs(self):
        """
        On passing more than 14 number nid
        """
        # Given
        nid = "29969203022300145"
        # When, Then
        with self.assertRaisesMessage(ValidationError, "national id should be 14 integers"):
            nid_validation(nid=nid)

    def test_pass_wrong_month(self):
        """
        On passing a wrong month in nid index [3:5]
        """
        # Given
        nid = "29250022300145"
        # When, Then
        with self.assertRaisesMessage(ValidationError, "Invalid month for national id"):
            nid_validation(nid=nid)

    def test_pass_wrong_day(self):
        """
        On passing a wrong day in nid index [5:7]
        """
        # Given
        nid = "29203662300145"
        # When, Then
        with self.assertRaisesMessage(ValidationError, "Invalid day for national id"):
            nid_validation(nid=nid)

    def test_pass_wrong_governate_code(self):
        """
        On passing a wrong day in nid index [7:9]
        """
        # Given
        nid = "29203029900145"
        # When, Then
        with self.assertRaisesMessage(ValidationError, "Invalid Governorate code"):
            nid_validation(nid=nid)
