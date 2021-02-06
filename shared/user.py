class User:
    def __init__(self,
        username,
        email,
        bankAccount,
        avatar,
        password
    ):
        self.username = username
        self.email = email
        self.bank_account = bankAccount
        self.avatar = avatar
        self.password = password

    def setUsername(self, username):
        self.username = username
    def getUsername(self):
        return self.username
    
    def setEmail(self, email):
        self.email = email
    def getEmail(self):
        return self.email

    def setBankAccount(self, bank_account):
        self.bank_account = bank_account
    def getBankAccount(self):
        return self.bank_account

    def setAvatar(self, avatar):
        self.avatar = avatar
    def getAvatar(self):
        return self.avatar

    def setPassword(self, password):
        self.password = password
    def getPassword(self):
        return self.password