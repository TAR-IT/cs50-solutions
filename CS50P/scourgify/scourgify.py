import csv
import sys

def clean_csv(input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
            reader = csv.DictReader(infile)
            fieldnames = ['first', 'last', 'house']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                full_name = row['name']
                last_name, first_name = full_name.split(', ')
                writer.writerow({'first': first_name, 'last': last_name, 'house': row['house']})

        print(f"Data cleaned and saved to '{output_file}'.")

    except FileNotFoundError:
        print("Error: The input file could not be found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python scourgify.py <input_file.csv> <output_file.csv>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    clean_csv(input_file, output_file)
