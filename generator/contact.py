from model.contact import Contact, BirthDate
import random
import string
import getopt
import sys
import jsonpickle
import os


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="Elon", lastname="Musk", nickname="elona51",
                    company="Tesla, SpaceX", address="California, Silicon Valley",
                    homephone="48-22-56", mobilephone="8-800-555-35-35", workphone="666-666", secondaryphone="1-234-567-89-10",
                    birth_date=BirthDate(bday="28", bmonth="June", byear="1971"), notes="Smart person (not an alian)")] + \
                    [Contact(firstname=random_string("", 10), lastname=random_string("", 10))
                     for i in range(n)]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
