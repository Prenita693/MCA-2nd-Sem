from collections import Counter
import string

# Function to get the most frequent words from a file
def get_most_frequent_words(filename, top_n=5):
    try:
        # Open and read the file content
        with open(filename, 'r') as file:
            text = file.read()

        # Convert text to lowercase
        text = text.lower(

        # Remove punctuation from the text
        text = text.translate(str.maketrans("", "", string.punctuation))

        # Split the text into individual words
        words = text.split()

        # Count the frequency of each word
        word_counts = Counter(words)

        # Get the top 'n' most common words
        most_common = word_counts.most_common(top_n)

        # Display the results
        print(f"\nTop {top_n} most frequent words in '{filename}':")
        for word, count in most_common:
            print(f"'{word}' : {count} times")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

# Main program
filename = input("Enter the file name (e.g., sample.txt): ")
get_most_frequent_words(filename, top_n=5)
