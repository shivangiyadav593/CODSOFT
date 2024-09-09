import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

def main():
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length < 1:
                raise ValueError("Length must be at least 1")
            break
        except ValueError as e:
            print(f"Invalid input: {e},Please enter a positive integer.")
    

    password = generate_password(length)
    print(f"Your Password: {password}")

if __name__ == "__main__":
    main()
