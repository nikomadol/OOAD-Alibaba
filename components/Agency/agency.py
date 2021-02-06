class Agency:
    def __init__(self, registeration_number, name, telephones, website=""):
        self.registeration_number = registeration_number
        self.name = name
        self.website = website
        self.telephones = telephones

    def getRegisterationNumber(self):
        return self.registeration_number
    
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