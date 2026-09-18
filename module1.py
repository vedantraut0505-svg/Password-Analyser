import hashlib


def hash_password(password):
    
    password_bytes = password.encode("utf-8")


    hashed_password = hashlib.sha256(password_bytes).hexdigest()

    return hashed_password


def main():
    print("=== Password Hashing Module ===")

    
    password = input("Enter your password: ")

    
    hashed = hash_password(password)

    print("\nOriginal Password:", password)
    print("SHA-256 Hash:", hashed)


if __name__ == "__main__":
    main()