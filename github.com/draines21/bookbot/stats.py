def get_word_count(book_text):
    total_words = len(book_text.split())
    return total_words 



def character_count(text):
    char_counts = {}
    for char in text:
        lower_char = char.lower()
        char_counts[lower_char] = char_counts.get(lower_char, 0) + 1
    return char_counts




def sorted_character_count(char_counts):
    def get_num_from_dict(item_dict):
        return item_dict['num']
    sorted_list = sorted(
        [{'char': char, 'num': count} for char, count in char_counts.items() if char.isalpha()],
        key=get_num_from_dict,
        reverse=True
    )
    return sorted_list