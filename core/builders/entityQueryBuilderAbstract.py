from core.builders.helpers.construct_queries import ConstructQueries

class AbstractEntityQueryBuilder(ConstructQueries):
    def __init__(self, table):
        super().__init__()
        self.setTable(table)

    def constructGetQuery(self, type = 'all', condition = None, search = None, search_field=None):
        if type == "all":
            return self.selectAllQuery(condition, search, search_field)
        elif type == "one":
            if not condition:
                raise Exception("\nGet One Query need condition.")
            return self.selectOneQuery(condition, search, search_field)
        else:
            raise Exception("\nSelect type is not valid.")

    def constructInsertQuery(self, data):
        return self.insertQuery(data)

    def constructUpdateQuery(self, condition, data):
        return self.updateQuery(condition, data)
    
    def constructDeleteQuery(self, condition):
        return self.deleteQuery(condition)