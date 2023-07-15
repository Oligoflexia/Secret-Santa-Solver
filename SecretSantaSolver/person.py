class Person:
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.banlist = []
    
    #adds a person object to the blacklist
    def banUser(self, Person):
        self.banlist.append(Person)
    
    #returns the list of banned users
    def getBanlist(self):
        return self.banlist
    
    #returns the name of the person
    def getName(self):
        return self.name
    
    #returns the email of the person
    def getEmail(self):
        return self.email




    
        
    
        