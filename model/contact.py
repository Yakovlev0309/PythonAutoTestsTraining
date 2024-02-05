from sys import maxsize


class BirthDate:
    def __init__(self, bday=None, bmonth=None, byear=None):
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear


class Contact:
    def __init__(self, id=None, firstname=None, middlename=None, lastname=None, nickname=None, 
                 company=None, address=None, 
                 homephone=None, mobilephone=None, workphone=None, secondaryphone=None, 
                 email=None, email2=None, email3=None, 
                 birth_date=None, notes=None, 
                 all_phones_from_home_page=None, all_names_from_view_page=None, all_emails_from_home_page=None):
        self.id = id
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.birth_date = birth_date
        self.notes = notes
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_names_from_view_page = all_names_from_view_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "Contact(%s, %s, %s)" % (self.id, self.firstname, self.lastname)
    
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
