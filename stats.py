def count_words(book_contents):
    words = book_contents.split()
    return len(words)

def count_characters(book_contents):
    char_counts = {}
    chars = book_contents.lower()
    for char in chars:
        if char in char_counts:
            char_counts[char] +=1
        else:
            char_counts[char] = 1
    return char_counts

def sort_char_counts(char_counts):
    sorted_char_counts = []
    for char, num in char_counts.items():
        if char.isalpha():
            sorted_char_counts.append({"char": char, "num": num})
    
    return sorted_char_counts

def sort_key(chars):
    return chars["num"]
