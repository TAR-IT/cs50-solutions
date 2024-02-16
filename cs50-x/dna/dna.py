import csv
import sys


def main():
    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py database.csv sequence.txt")
        sys.exit(1)

    # Read database file into a variable
    database_file = sys.argv[1]
    database = read_csv(database_file)

    # Read DNA sequence file into a variable
    sequence_file = sys.argv[2]
    sequence = read_sequence(sequence_file)

    # Find longest match of each STR in DNA sequence
    str_counts = find_str_counts(database, sequence)

    # Check database for matching profiles
    match = find_match(database, str_counts)

    # Print the result
    if match:
        print(match)
    else:
        print("No match")


def read_csv(filename):
    """Read CSV file and return a list of dictionaries."""
    try:
        with open(filename, newline="") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        sys.exit(1)


def read_sequence(filename):
    """Read DNA sequence from a text file and return as a string."""
    try:
        with open(filename) as file:
            return file.read()
    except Exception as e:
        print(f"Error reading sequence file: {e}")
        sys.exit(1)


def find_str_counts(database, sequence):
    """Find the longest run of each STR in the DNA sequence."""
    str_counts = {}
    for column in list(database[0].keys())[1:]:
        str_counts[column] = longest_match(sequence, column)
    return str_counts


def find_match(database, str_counts):
    """Check database for matching profiles."""
    for row in database:
        if all(
            int(row[str_name]) == str_count
            for str_name, str_count in str_counts.items()
        ):
            return row["name"]
    return None


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
