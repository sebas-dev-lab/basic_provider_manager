from core.entities.provider_contact import ProviderConctact

class ProviderServices:
    def __init__(self):
        self.entity = ProviderConctact()
    
    def addProvider(self, data):
        return self.entity.createEntity(data)
    
    def getProvidersList(self):
        return self.entity.findAll()

    def searchProvider(self, search, field):
        return self.entity.findAll("all", None, search, field)