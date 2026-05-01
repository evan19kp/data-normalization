import csv
import copy

def parseCSV_fields(filename:str):
    with open(filename, mode='r') as f:
        reader = csv.reader(f)
        fields = next(reader)
        return fields

def parseCSV(filename: str):
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
        try:
            if '.' in value[col]:
                the_values.append(float(value[col]))
            else:
                the_values.append(int(value[col]))
        except ValueError:
            return None

    normalized = []

    biggest = max(the_values)
    smallest = min(the_values)

    for num in the_values:
        temp = float(((num - smallest) / (biggest - smallest)))
        temp = round(temp, 1)
        normalized.append(temp)
    return normalized

def rewrite_data(col: str, data: list, normalized: list):
    temp_data = copy.deepcopy(data)

    for i, value in enumerate(temp_data):
        temp_data[i][col] = normalized[i]
    return temp_data

def wrapper(filename:str):
    fieldnames = parseCSV_fields(filename)
    CSVdata = parseCSV(filename)
    final = []

    for col in fieldnames:
        norm = normalize(col, CSVdata)
        if norm is None:
            continue
        if not final:
            temp_final = rewrite_data(col, CSVdata, norm)
        else:
            temp_final = rewrite_data(col, final, norm)
        final = temp_final

    return final