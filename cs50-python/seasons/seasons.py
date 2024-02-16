from datetime import date
import inflect
import sys

def get_date_input():
    # Prompt the user for their date of birth
    date_input = input("Enter your date of birth in YYYY-MM-DD format: ")

    # Validate the input format
    try:
        return date.fromisoformat(date_input)
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        sys.exit(1)

def age_in_minutes(date_of_birth):
    # Get today's date
    today = date.today()

    # Calculate the age in minutes
    age_days = (today - date_of_birth).days
    age_minutes = age_days * 24 * 60

    return age_minutes

def main():
    dob = get_date_input()
    age = age_in_minutes(dob)

    # Convert the age in minutes to English words with capitalized first letter
    p = inflect.engine()
    age_words = p.number_to_words(age, zero='o', andword="").capitalize()

    print(f"{age_words} minutes")

if __name__ == "__main__":
    main()