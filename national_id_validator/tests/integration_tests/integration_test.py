from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class TestNationalIdViewSet(TestCase):
    def tearDown(self):
        pass

    def setUp(self):
        self.url = reverse('validate_national_id-list')

    def test_success_input(self):
        """
        Test on providing valide ID number to NationalIdViewSet
        """
        # Given
        body = {
            "national_id": "29203022300145"
        }
        # when
        response = self.client.post(self.url, body)
        response_json = response.json()

        # Then
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_json.get('birthdate'), '1992-03-02')
        self.assertEqual(response_json.get('gender'), 'female')
        self.assertEqual(response_json.get('governorate'), 'Fayoum')

    def test_having_charcater_input(self):
        """
        Test on providing charcter in national_id
        """
        # Given
        body = {
            "national_id": "292030223001a5"
        }
        # When
        response = self.client.post(self.url, body)
        response_json = response.json()

        # Then
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response_json.get('national_id'), [
                         'national id should only contain integers'])

    def test_nid_more_than_14_charcter(self):
        """
        Test on providing more than 14 charcters in national_id
        """
        # Given
        body = {
            "national_id": "2920302230015"
        }
        # When
        response = self.client.post(self.url, body)
        response_json = response.json()
        # Then
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response_json.get('national_id'), [
                         'national id should be 14 integers'])
