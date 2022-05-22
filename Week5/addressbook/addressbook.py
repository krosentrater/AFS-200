class Contact():
    def __init__(self, fname, lname, email, number, photo):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.number = number
        self.photo = photo

    def getFirstName(self):
        print(self.fname)

    def getLastName(self):
        print(self.lname)

    def getEmail(self):
        print(self.email)

    def getNumber(self):
        print(self.number)

    def getPhoto(self):
        print(self.photo)
    
    def __str__(self):
        return f'{self.fname} {self.lname} ({self.email})'

    def __repr__(self):
        return f'{self.fname} {self.lname} ({self.email})'


class AddressBook():
    def __init__(self):
        self.addresses = []
        
    def addAddress(self, address):
        self.addresses.append(address)
        
    def getAllAddresses(self):
        print(self.addresses)
        return self.addresses
    
    def findAllMatching(self,searchStr):
        results = []
        for address in self.addresses:
            
            if address.getFirstName().lower().startswith(searchStr.lower()) or address.getLastName().lower().startswith(searchStr.lower()):
                results.append(address)
                
        return results
