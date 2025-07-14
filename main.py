from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    
    book_text = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    number_of_words =  word_count(book_text)
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    char_dict = unique_chars(book_text)
    print("--------- Character Count -------")
    dict_sort(char_dict)


main()