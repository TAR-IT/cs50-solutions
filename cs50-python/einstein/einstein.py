def calculate_energy_in_joules(mass_kg):
    speedoflight = 300000000
    energy_joules = mass_kg * speedoflight ** 2
    return energy_joules

def main():
    try:
        mass_kg = int(input())
        energy_joules = calculate_energy_in_joules(mass_kg)
        print(energy_joules)

    except ValueError:
        print("Error: Please enter a valid integer for mass.")

if __name__ == "__main__":
    main()