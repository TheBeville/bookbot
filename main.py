import sys
from stats import get_num_words, character_frequency, sorted_char_frequency

filepath = ''

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        report_text = f"""============ BOOKBOT ============
    Analyzing book found at {filepath}...
    ----------- Word Count ----------
    Found {get_num_words(get_book_text(filepath))} total words
    --------- Character Count -------
    """
        for char in sorted_char_frequency(get_book_text(filepath)):
            report_text += f"{char['char']}: {char['num']}\n"
        print(f'{report_text}')
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
main()