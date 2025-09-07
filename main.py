from stats import get_num_words, get_num_character, sorted_list

def get_book_text (filepath: str) -> str:
    with open (filepath) as f:
        file_content = f.read()
    return file_content

def main():
    filepath = r"./books/frankenstein.txt"
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    num_chars_dict = get_num_character(text)
    sorted = sorted_list(num_chars_dict)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted:
        print(f"{i["char"]}: {i["num"]}")

main()
