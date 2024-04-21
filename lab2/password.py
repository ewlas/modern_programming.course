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
    if len(sys.argv) > 1:
        try:
            return int(sys.argv[1])
        except ValueError:
            pass
    try:
        length = int(input())
        return length
    except ValueError:
        sys.stderr.write("ERROR: Enter a valid integer for the length of the password\n")
        return None

def print_password(password):
    if password:
        print("Generated password:", password)

def main():
    length = get_password_length()
    if length is None:
        sys.exit(1) 

    password, error = generate_password(length)
    if error == 0:  
        print_password(password)
        sys.exit(0) 
    else:
        sys.exit(error)  
 

if __name__ == "__main__":
    main()
