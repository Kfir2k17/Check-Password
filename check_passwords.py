# Globals

COMMON_PASSWORDS = [
    "123456",
    "password",
    "123456789",
    "12345678",
    "12345",
    "123123",
    "qwerty",
    "abc123",
    "password1",
    "111111"
]


def check_password(password): # Main Checking function
    points = 0
    points += check_length(len(password))

    points += 1 if password.islower() else 0 # Checks if contains lower case
    points += 1 if password.isupper() else 0 # Checks if contains upper case
    points += 1 if any(i.isdigit() for i in password) else 0 # Checks if contains numbers
    points += 1 if any(not c.isalnum() for c in password) else 0 # Checks if contains special characters

    points += check_common(password) # Checks if password is common

    security_level = measure_security(points)
    return points, security_level

def measure_security(points):
    if points < 0:
        return "Weak"

    elif 1 < points < 3:
        return "Medium"

    return "Strong"


def check_common(password): # Checks if password is common
    return -2 if password in COMMON_PASSWORDS else 0

def check_length(l): # Returns points on the basis of the Length of the password
    if l < 8:
        return 0

    elif 8 < l < 11:
        return 1

    return 2

if __name__ == '__main__':
    pas = input('Enter password: ')
    point, security = check_password(pas)

    print(f"The password valued with {point} points, So your security level is {security}")