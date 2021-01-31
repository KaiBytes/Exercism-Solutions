import re

class Phone(object):
    #constructor
    def __init__(self, phone_number):
        #attributes
        self.number = re.sub('[^0-9]','', phone_number)

    def hello()

test = Phone("+1 (613)-995-0253")
print(test.number)
