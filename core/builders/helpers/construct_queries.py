class ConstructQueries:
    def __init__(self):
        self.table = None
        self.keys = []
        self.values = []
        self.items_keys = []

    def setTable(self, table):
        self.table = table

    def setKeysValues(self, entity):
        self.keys = entity.keys()
        self.values = entity.values()
        n = 1
        self.items_keys = [f"${n + x}" for x in range(len(self.keys))]
        print(self.items_keys)

    def selectAllQuery(self, condition=None, search=None, search_field=None):
        if condition:
            return self.selectQuery(condition, search, search_field)
        elif search and search_field:
            query = f"SELECT * FROM {self.table} WHERE {search_field} ILIKE '%{search}%';"
        else:
            query = f"SELECT * FROM {self.table};"

        return query

    def selectOneQuery(self, condition, search=None, search_field=None):
        return self.selectQuery(condition, search, search_field, limit=1)

    def selectQuery(self, condition, search=None, search_field=None, limit=None):
        if isinstance(condition, dict):
            condiciones = []
            for columna, valor in condition.items():
                if isinstance(valor, str):
                    if search and search_field == columna:
                        condiciones.append(f"{columna} ILIKE '%{valor}%'")
                    else:
                        condiciones.append(f"{columna} = '{valor}'")
                elif isinstance(valor, (int, float)):
                    condiciones.append(f"{columna} = {valor}")
                elif isinstance(valor, dict):
                    subcondicion = " AND ".join([f"{k} = '{v}'" if isinstance(v, str) else f"{k} = {v}" for k, v in valor.items()])
                    condiciones.append(f"({subcondicion})")
            where_clause = " AND ".join(condiciones)
        elif isinstance(condition, list):
            subcondiciones = []
            for subcondition in condition:
                subcondicion_query = self.selectQuery(subcondition, search, search_field)
                subcondiciones.append(f"({subcondicion_query})")
            where_clause = " OR ".join(subcondiciones)
        else:
            raise ValueError("\nCondition is not a valid dictionary or list.")
        
        limit_clause = f" LIMIT {limit}" if limit else ""
        consulta = f"SELECT * FROM {self.table} WHERE {where_clause}{limit_clause}"
        return consulta

    def insertQuery(self, data):
        columns = ", ".join(data.keys())
        values = tuple(data.values())
        marks = ", ".join(["%s"] * len(values))
        query = f"INSERT INTO {self.table} ({columns}) VALUES ({marks})"
        return {
            'query': query,
            'values': values
        }
    
    def updateQuery(self, condition, data):
        set_values = ", ".join([f"{key} = %s" for key in data.keys()])
        values = tuple(data.values())
        where_clause = self._constructWhereClause(condition)
        query = f"UPDATE {self.table} SET {set_values} WHERE {where_clause}"
        return {
            'query': query,
            'values': values
        }
    
    def deleteQuery(self, condition):
        where_clause = self._constructWhereClause(condition)
        query = f"DELETE FROM {self.table} WHERE {where_clause}"
        return query
    
    def _constructWhereClause(self, condition):
        if isinstance(condition, dict):
            condiciones = []
            for columna, valor in condition.items():
                if isinstance(valor, str):
                    condiciones.append(f"{columna} = '{valor}'")
                elif isinstance(valor, (int, float)):
                    condiciones.append(f"{columna} = {valor}")
                elif isinstance(valor, dict):
                    subcondicion = " AND ".join([f"{k} = '{v}'" if isinstance(v, str) else f"{k} = {v}" for k, v in valor.items()])
                    condiciones.append(f"({subcondicion})")
            where_clause = " AND ".join(condiciones)
        elif isinstance(condition, list):
            subcondiciones = []
            for subcondition in condition:
                subcondicion_query = self._constructWhereClause(subcondition)
                subcondiciones.append(f"({subcondicion_query})")
            where_clause = " OR ".join(subcondiciones)
        else:
            raise ValueError("\nCondition is not a valid dictionary or list.")
        
        return where_clause
