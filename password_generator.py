import random
import string

def generate_password(length):
    # Characters to choose from: letters, digits, punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Welcome to the Password Generator!")
    
    try:
        length = int(input("Enter the desired length of your password: "))
        if length <= 0:
            print("Length should be greater than 0.")
            return

        password = generate_password(length)
        print(f"\nGenerated Password: {password}")
    
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
