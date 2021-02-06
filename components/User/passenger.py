from .user import User
class Passenger(User):
    def __init__(self,
        phoneNumber,
        firstName,
        lastName,
        nationalID,
        gender,
        birthdate
    ):
        self.phone_number = phoneNumber
        self.first_name = firstName
        self.last_name = lastName
        self.national_id = nationalID
        self.gender = gender
        self.birthdate = birthdate

    def setPhoneNumber(self, phoneNumber):
        self.phone_number = phoneNumber
    def getPhoneNumber(self):
        return self.phone_number
    
    def setFirstName(self, firstName):
        self.first_name = firstName
    def getFirstName(self):
        return self.first_name

    def setLastName(self, lastName):
        self.last_name = lastName
    def getLastName(self):
        return self.last_name

    def setNationalID(self, nationalID):
        self.national_id = nationalID
    def getNationalID(self):
        return self.national_id

    def setGender(self, gender):
        self.gender = gender
    def getGender(self):
        return self.gender

    def setBirthdate(self, birthdate):
        self.birthdate = birthdate
    def getBirthdate(self):
        return self.birthdate