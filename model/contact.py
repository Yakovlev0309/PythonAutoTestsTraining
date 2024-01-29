

class BirthDate:
    def __init__(self, bday=None, bmonth=None, byear=None):
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear


class Contact:
    def __init__(self, firstname=None, lastname=None, nickname=None, company=None, address=None, home=None, mobile=None, birth_date=None, notes=None):
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.birth_date = birth_date
        self.notes = notes
