def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("=" * 40)
    print("       Caesar Cipher Tool")
    print("=" * 40)

    while True:
        print("\n1. Encrypt\n2. Decrypt\n3. Exit")
        choice = input("Choose option: ").strip()

        if choice == '3':
            print("Exiting.")
            break
        elif choice not in ('1', '2'):
            print("Invalid choice.")
            continue

        message = input("Enter message: ")
        try:
            shift = int(input("Enter shift value (1-25): ")) % 26
        except ValueError:
            print("Invalid shift value.")
            continue

        if choice == '1':
            output = caesar_encrypt(message, shift)
            print(f"Encrypted: {output}")
        else:
            output = caesar_decrypt(message, shift)
            print(f"Decrypted: {output}")

if __name__ == "__main__":
    main()
