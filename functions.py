import csv

def parseCSV_by_column(column: str):
    data = []

    with open('data.csv', mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row[column])
        return data

