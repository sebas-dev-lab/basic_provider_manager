
from core.builders.entityQueryBuilderAbstract import AbstractEntityQueryBuilder
from config.database_connect import DatabaseConnector

class BaseEntity(AbstractEntityQueryBuilder, DatabaseConnector):
    def __init__(self, table_name):
        super().__init__(table_name)
        super(DatabaseConnector, self).__init__()

    def createEntity(self, data):
        super().connect()
        query = super().constructInsertQuery(data)
        super().execute_query(query["query"], query["values"], "insert")
        super().disconnect()
        return
    
    def findAll(self, type = "all", condition = None, search = None, search_file = None):
        super().connect()
        query = super().constructGetQuery(type, condition, search, search_file)
        print(query)
        data = super().execute_query(query)
        super().disconnect()
        return data
    
    def findOne(self, type = "one", condition = None, search = None, search_file = None):
        super().connect()
        query = super().constructGetQuery(type, condition, search, search_file)
        data = super().execute_query(query)
        super().disconnect()
        return data
    
