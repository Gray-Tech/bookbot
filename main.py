import sys
from stats import count_words, count_characters, sort_characters

def get_book_text(filepath):
    with open(filepath, encoding='utf-8') as f:
        text = f.read()
    return text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    
    word_count = count_words(text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    
    all_characters = count_characters(text)
    sorted_characters = sort_characters(all_characters)

    print("--------- Character Count -------")
    for item in sorted_characters:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
