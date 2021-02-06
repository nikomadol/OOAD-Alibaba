class Agency:
    def __init__(self):
        self.registeration_number = 0
        self.name = ""
        self.website = ""
        self.telephones = []

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

    