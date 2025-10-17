from stats import count_words, count_characters, sort_char_counts, sort_key
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(book_path):
    with open(book_path) as book:
        book_contents = book.read()
    return book_contents

def main():
    print("============ BOOKBOT ============")
    path = sys.argv[1]
    book = get_book_text(path)
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    word_count = count_words(book)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    char_counts = count_characters(book)
    ordered_chars = sort_char_counts(char_counts)
    ordered_chars.sort(reverse=True, key=sort_key)
    for char in ordered_chars:
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")

main()
