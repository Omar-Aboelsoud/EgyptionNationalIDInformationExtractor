from datetime import datetime
from ..common import GOVERNORATES
from ..utils import nid_get_birth_century
from ..DTOs import NIDDTO


class NIDService:

    def __init__(self):
        pass

    def __get_birth_date(self, nid):
        """
        return birthdate from NID, private function
        """
        day = nid[5:7]
        month = nid[3:5]
        century = nid_get_birth_century(nid[0])
        year = f'{century}{nid[1:3]}'
        date_str = f"{day}/{month}/{year}"
        birthday = datetime.strptime(date_str, '%d/%m/%Y')
        return birthday.date()

    def __get_governorate(self, nid):
        """
        get Governorate from NID, private function
        """
        code = nid[7:9]
        return GOVERNORATES.get(code)

    def __get_gender(self, nid):
        """
        return gender, private function
        """
        if int(nid[12]) % 2 == 0:
            return "female"
        return "male"

    def get_national_id_information(self, nid):
        nid_dto = NIDDTO()
        nid_dto.birthdate = self.__get_birth_date(nid)
        nid_dto.governorate = self.__get_governorate(nid)
        nid_dto.gender = self.__get_gender(nid)
        return nid_dto
