import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Regular expression pattern for valid IPv4 address
    ipv4_pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"

    # Check if the input matches the IPv4 pattern
    match = re.search(ipv4_pattern, ip)

    if match:
        # Convert each group to an integer and check if it is in the valid range (0 to 255)
        for group in match.groups():
            if not (0 <= int(group) <= 255):
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()
