class Agency:
    def __init__(self, registration_number, name, telephones, website=""):
        self.registration_number = registration_number
        self.name = name
        self.website = website
        self.telephones = telephones

    def getRegistrationNumber(self):
        return self.registration_number
    
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name

    def setWebsite(self, website):
        self.website = website
    def getWebsite(self):
        return self.website

    def setTelephones(self, telephones):
        self.telephones = telephones
    def getTelephone(self):
        return self.telephones
    def addTelephone(self, telephone):
        self.telephones.append(telephone)
    def removeTelephone(self, telephone):
        self.telephones.remove(telephone)