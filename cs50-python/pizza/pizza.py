import sys
import csv
from tabulate import tabulate

def read_csv_file(file_name):
    data = []
    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        headers = reader.fieldnames
        for row in reader:
            data.append([row[headers[0]], row[headers[1]], row[headers[2]]])
    return headers, data

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pizza.py <file_name.csv>")

    file_name = sys.argv[1]
    if not file_name.endswith('.csv'):
        sys.exit("Invalid file name. File must end with '.csv'.")

    headers, data = read_csv_file(file_name)
    table = tabulate(data, headers=headers, tablefmt='grid')
    print(table)

if __name__ == "__main__":
    main()
