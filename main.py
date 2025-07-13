import sys
from stats import count_words, count_chars, sorted_dict

def get_book_text(filepath):
    contents = ''
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    print("============ BOOKBOT ============")
    path = sys.argv[1]
    print(f"Analyzing book found at {path}...")

    num_words = count_words(get_book_text(path))

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    counted_chars = sorted_dict(count_chars(get_book_text(path)))
    for elem in counted_chars:
        if elem["char"].isalpha():
            print(elem["char"]+":", elem["num"])

    print("============= END ===============")
    return 0

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>") 
    sys.exit(1)
main()

