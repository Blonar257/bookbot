def get_num_words(text: str) -> None:
    splitted: list[str] = text.split()
    num_words = len(splitted)
    print(f"{num_words} words found in the document")

def get_num_character(text: str) -> dict:
    char_dict = {}
    for c in text.lower():
        try:
            char_dict[c] += 1
        except Exception as e:
            char_dict[c] = 1
    return char_dict
