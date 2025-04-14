from cypher import *
def main():
    plaintext = input("Enter your full name to encrypt: ")
    ciphertext = encrypt(plaintext)
    print(f"Encrypted text: {ciphertext}")

    print("\nTry to guess the encryption key!")
    maxAttempts = 2
    attempts = 0
    while True:
        try:
            guess = int(input("Enter your guess for the key (1-25): "))
            if correctGuess(guess):
                print("/nCorrect! You've guessed the key.")
                print(f"Decrypted text: {decrypt(ciphertext)}")
                break
            elif maxAttempts <= attempts:
                print("\nIncorrect key. Max tried reached. Cipher has been redone.")
                attempts = 0
                ciphertext = encrypt(plaintext, True) #redo cipher
                print(f"Encrypted text: {ciphertext}")
            else:
                attempts +=1
                print("Incorrect key. Try again.")

        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
