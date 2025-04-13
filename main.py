from cypher import *
def main():
    plaintext = input("Enter your full name to encrypt: ")
    ciphertext = encrypt(plaintext)
    print(f"Encrypted text: {ciphertext}")

    print("\nTry to guess the encryption key!")
    while True:
        try:
            guess = int(input("Enter your guess for the key (1-25): "))
            if correctGuess(guess):
                print("Correct! You've guessed the key.")
                print(f"Decrypted text: {decrypt(ciphertext)}")
                break
            else:
                print("Incorrect key. Try again.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
