import string

# Function to check if a number is prime
def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Prime Number sum calculator
def prime_sum(start, end):
    total = 0
    for num in range(start, end + 1):
        if is_prime(num):
            total += num
    return total

# Length Unit converter (meters to feet or feet to meters)
def length_converter(value, direction):
    if direction == 'M':
        return round(value * 3.28084, 2)
    elif direction == 'F':
        return round(value / 3.28084, 2)
    else:
        raise ValueError("Invalid conversion direction. Use 'M' for meters to feet or 'F' for feet to meters.")

# Consonant counter
def consonant_counter(text):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0
    for char in text:
        if char in consonants:
            count += 1
    return count

# Min-Max number finder
def min_max(numbers):
    if not numbers:
        raise ValueError("The list is empty.")
    return min(numbers), max(numbers)

# Palindrome checker
def is_palindrome(text):
    cleaned_text = ''.join(e for e in text if e.isalnum()).lower()
    return cleaned_text == cleaned_text[::-1]

# Word counter 
def word_counter(filename, words_list):
    """Count the occurrences of specific words in a text file."""
    try:
        with open(filename, 'r') as file:
            text = file.read().lower()  # Convert text to lowercase
            # Remove punctuation
            text = text.translate(str.maketrans('', '', string.punctuation))
            
            # Split the text into words
            words_in_text = text.split()

            # Count occurrences of each word
            counts = {}
            for word in words_list:
                counts[word] = words_in_text.count(word)
            return counts
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None

# Main function to interact with the user
def main():
    while True:
        print("\nSelect a function (1-6):")
        print("1. Calculate the sum of prime numbers")
        print("2. Convert length units")
        print("3. Count consonants in string")
        print("4. Find min and max numbers")
        print("5. Check for palindrome")
        print("6. Word Counter")
        print("7. Exit program")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 0 and 6.")
            continue

        if choice == 1:
            try:
                start = int(input("Enter start range: "))
                end = int(input("Enter end range: "))
                print(f"Sum of prime numbers between {start} and {end} is: {prime_sum(start, end)}")
            except ValueError:
                print("Invalid input! Please enter valid integers for the range.")
        
        elif choice == 2:
            try:
                value = float(input("Enter the value to convert: "))
                direction = input("Enter conversion direction (M for meters to feet, F for feet to meters): ").upper()
                print(f"Converted value: {length_converter(value, direction)}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == 3:
            text = input("Enter a string: ")
            print(f"Number of consonants: {consonant_counter(text)}")
        
        elif choice == 4:
            try:
                numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
                smallest, largest = min_max(numbers)
                print(f"Smallest number: {smallest}, Largest number: {largest}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == 5:
            text = input("Enter a string: ")
            print(f"Is palindrome? {is_palindrome(text)}")
        
        elif choice == 6:
            filename = input("Enter the filename: ")
            words_list = ["the", "was", "and"]
            word_counts = word_counter(filename, words_list)
            if word_counts:
                print("Word counts in the file:")
                for word, count in word_counts.items():
                    print(f"{word}: {count}")
        
        elif choice == 0:
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice! Please choose a number between 0 and 6.")
        
        continue_choice = input("Would you like to try another function? (y/n): ").lower()
        if continue_choice != 'y':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
