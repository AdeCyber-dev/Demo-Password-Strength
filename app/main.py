from .utils import check_password_strength


def main():
    pwd = input("Enter a password: ")
    strength = check_password_strength(pwd)
    print(f"Password strength: {strength}")

if __name__ == "__main__":
    main()
