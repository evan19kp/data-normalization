import csv

def parseCSV_fields(filename:str):
    with open(filename, mode='r', newline='') as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        return fields

def parseCSV_by_column(filename: str):
    CSVdata = []
    with open(filename, mode='r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            CSVdata.append(row)
    return CSVdata

def writeCSV(data: list, columns: list, filename: str): # list of dictionaries,
    with open(filename, mode='w', newline='') as f:     # list of fieldnames,
        writer = csv.DictWriter(f, fieldnames=columns)  # filename
        writer.writeheader()
        writer.writerows(data)

def normalize(col:str, data: list): # data is a list of dicts
    the_values = []

    for i, value in enumerate(data):
        if '.' in value[col]:
            the_values.append(float(value[col]))
        else:
            the_values.append(int(value[col]))

    normalized = []

    biggest = max(the_values)
    smallest = min(the_values)

    for num in the_values:
        temp = float(((num - smallest) / (biggest - smallest)))
        temp = round(temp, 1)
        normalized.append(temp)
    return normalized

all = parseCSV_by_column('data.csv')
print(all)
pop = normalize('population', all)
print(pop)
area = normalize('area', all)
print(area)
