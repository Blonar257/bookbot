def get_book_text (filepath: str) -> str:
    with open (filepath) as f:
        file_content = f.read()
    return file_content

def word_count(text: str) -> None:
    splitted: list[str] = text.split()
    num_words = len(splitted)
    print(f"{num_words} words found in the document")

def main():
    text = get_book_text("./books/frankenstein.txt")
    word_count(text)

main()
