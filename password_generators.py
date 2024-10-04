import string
import secrets

def has_uppercase(password: str) -> bool:
    # Check if the password contains any uppercase letters
    for character in password:
        if character.isupper():
            return True
    return False  # No uppercase characters found

def has_special_chars(password: str) -> bool:
    # Check if the password contains any punctuation symbols
    for character in password:
        if character in string.punctuation:
            return True
    return False  # No special characters found

def create_password(pwd_length: int, allow_symbols: bool, allow_uppercase: bool) -> str:
    # Basic character set includes lowercase letters and digits
    char_set: str = string.ascii_lowercase + string.digits

    # Optionally add symbols and uppercase letters
    if allow_symbols:
        char_set += string.punctuation
    if allow_uppercase:
        char_set += string.ascii_uppercase

    max_index: int = len(char_set)
    generated_password: str = ""

    # Create the password by randomly selecting characters
    for _ in range(pwd_length):
        generated_password += char_set[secrets.randbelow(max_index)]

    return generated_password

if __name__ == "__main__":
    # Generate and display 5 random passwords with conditions
    for idx in range(1, 6):
        pwd: str = create_password(pwd_length=15, allow_symbols=True, allow_uppercase=True)
        pwd_checks: str = f"Contains Uppercase: {has_uppercase(pwd)}, Contains Symbols: {has_special_chars(pwd)}"

        print(f"{idx}: {pwd} ({pwd_checks})")
