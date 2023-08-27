import csv

class ExportToCsv:
    def __init__(self):
        self.content = None
        self.filename = "default.csv"

    def setFilename(self, filename):
        self.filename = filename    

    def setContent(self, content):
        self.content = content


    def exportCsv(self):
        with open (f"{self.filename}.csv", 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['ID', "Nombre", "Teléfono", "Email", "Dirección"])
            writer.writerows(self.content)
        print(f"\nCSV creado correctamente: {self.filename}.csv")