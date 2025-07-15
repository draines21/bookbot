import sys 
from stats import get_word_count 
from stats import character_count, sorted_character_count 

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        book_text = f.read()
    return book_text 




def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
   
    text = get_book_text(sys.argv[1])
    total_words = get_word_count(text)
    print(f'Found {total_words} total words.')
   
    print("--------- Character Count -------")

    char_counts = character_count(text) 
    sorted_counts = sorted_character_count(char_counts)
    
    for char_dict in sorted_counts:
        print(f"{char_dict['char']}: {char_dict['num']}")

    print("============= END ===============")









main()