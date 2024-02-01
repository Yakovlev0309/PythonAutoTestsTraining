from sys import maxsize


class BirthDate:
    def __init__(self, bday=None, bmonth=None, byear=None):
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear


class Contact:
    def __init__(self, id=None, firstname=None, lastname=None, nickname=None, 
                 company=None, address=None, 
                 homephone=None, mobilephone=None, workphone=None, secondaryphone=None, 
                 birth_date=None, notes=None, 
                 all_phones_from_home_page=None):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.birth_date = birth_date
        self.notes = notes
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "Contact(%s, %s, %s)" % (self.id, self.firstname, self.lastname)
    
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
