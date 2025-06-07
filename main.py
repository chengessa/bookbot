import sys
from stats import get_num_words, letter_count, sort_on

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    num_letters = letter_count(book_text)
    print(f"Found {num_words} total words")
    sorted_characters = sorted(num_letters.items(), key=sort_on, reverse=True)

    for char, count in sorted_characters:
        print(f"{char}: {count}")
main()