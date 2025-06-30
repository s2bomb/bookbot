from stats import word_counter
from stats import letter_counter
from stats import sort_dic
import sys

# file to string
def get_book_text(filepath):

    with open(filepath) as file:
        file_contents = file.read()

    return file_contents



#-------------main----------------

def main():
    if len(sys.argv) == 2:
        print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}")
        
        
        print("----------- Word Count ----------")
        words_counted = word_counter(get_book_text(sys.argv[1]))
        print(f"Found {words_counted} total words")


        print("--------- Character Count -------")
        letters_counted_sorted = sort_dic(letter_counter(get_book_text(sys.argv[1])))
    
        for letter in letters_counted_sorted:
            if letter["char"].isalpha():
                print(f"{letter["char"]}: {letter["num"]}")

        print("============= END ===============")

    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()
