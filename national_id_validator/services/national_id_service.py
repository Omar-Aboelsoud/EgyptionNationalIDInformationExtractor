from datetime import datetime
from ..common import GOVERNORATES
from ..utils import nid_get_birth_century


class NIDService:

    def __init__(self):
        pass

    def get_birth_date(nid):
        """
        return birthdate from NID
        """
        day = nid[5:7]
        month = nid[3:5]
        century = nid_get_birth_century(nid[0])
        year = f'{century}{nid[1:3]}'
        date_str = f"{day}/{month}/{year}"
        birthday = datetime.strptime(date_str, '%d/%m/%Y')
        return birthday.date()

    def get_governorate(nid):
        """
        get Governorate from NID
        """
        code = nid[7:9]
        return GOVERNORATES.get(code)

    def get_gender(nid):
        """
        return gender
        """
        if int(nid[12]) % 2 == 0:
            return "female"
        return "male"

    def get_national_id_information(self):
        return {"birthdate": self.get_birth_date(),
                "governorate": self.get_governorate(),
                "gender": self.get_gender()}
