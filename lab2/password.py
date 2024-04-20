import sys
import random
import string

def generate_password(length):
    if not isinstance(length, int) or length <= 0:
        sys.stderr.write("ERROR: Length must be a natural number\n")
        return -1  

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password, 0  

def get_password_length():
    try:
        length = int(input())
        return length
    except ValueError:
        sys.stderr.write("enter a valid integer for the length of the password\n")
        return None

def print_password(password):
    if password:
        print("Generated password:", password)

def main():
    length = get_password_length()
    if length is not None:
        password, error = generate_password(length)
        if error == 0:  
            print_password(password)

if __name__ == "__main__":
    main()
