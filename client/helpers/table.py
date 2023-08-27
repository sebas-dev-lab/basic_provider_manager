from tabulate import tabulate

class Table:
    def __init__(self):
        self.__headers = None
        self.__table = None

    def setTableHeaders(self, headers):
        self.__headers = headers
    
    def setTableContent(self, content):
        self.__table = []
        n = 0
        for x in content:
            l = list(x)
            l.insert(0, n)
            self.__table.append(l)
            n += 1

    def printTable(self):
        if isinstance(self.__headers, list) and isinstance(self.__table, list) and all(isinstance(row, list) for row in self.__table):
            try:
                print("\nResultados: \n")
                print(tabulate(self.__table, headers=self.__headers))
            except IndexError:
                print("\nError table.")
        else:
            print("\nContent does not exist.")