from stats import get_num_words, get_num_character

def get_book_text (filepath: str) -> str:
    with open (filepath) as f:
        file_content = f.read()
    return file_content

def main():
    text = get_book_text("./books/frankenstein.txt")
    get_num_words(text)
    num_chars = get_num_character(text)
    print(num_chars)

main()
