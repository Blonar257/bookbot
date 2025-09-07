def get_num_words(text: str):
    splitted: list[str] = text.split()
    num_words = len(splitted)
    return num_words

def get_num_character(text: str) -> dict:
    char_dict = {}
    for c in text.lower():
        try:
            char_dict[c] += 1
        except Exception as e:
            char_dict[c] = 1
    return char_dict

def sorted_list(charcount_dict: dict):
    list_of_dicts = []
    for k, v in charcount_dict.items():
        part = {"char": k, "num": v}
        if str(k).isalpha():
            list_of_dicts.append(part)
    list_of_dicts.sort(key=lambda x: x["num"], reverse=True)
    return list_of_dicts
