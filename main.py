import sys
from stats import get_num_words, get_num_character, sorted_list

def get_book_text (filepath: str) -> str:
    with open (filepath) as f:
        file_content = f.read()
    return file_content

def main():
    # filepath = r"./books/frankenstein.txt"
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    num_chars_dict = get_num_character(text)
    sorted = sorted_list(num_chars_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted:
        print(f"{i["char"]}: {i["num"]}")


main()
