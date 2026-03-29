import time

def brute_force_wordlist(target_password, wordlist_file='wordlist.txt'):
    attempts = 0
    start_time = time.time()

    try:
        with open(wordlist_file, 'r') as f:
            words = f.read().splitlines()
    except FileNotFoundError:
        print(f"Wordlist file '{wordlist_file}' not found!")
        return

    for word in words:
        attempts += 1
        print(f"Trying: {word}")

        if word == target_password:
            end_time = time.time()
            print(f"\nPassword Found: {word}")
            print(f"Attempts: {attempts}")
            print(f"Time Taken: {end_time - start_time:.2f} seconds")
            return

    print("\nPassword not found in the wordlist.")

if __name__ == "__main__":
    target = input("Enter password to simulate dictionary attack: ")
    brute_force_wordlist(target)

