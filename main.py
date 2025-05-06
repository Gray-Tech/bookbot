def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text
def count_words(text):
    return len(text.split())


def main():
    text = get_book_text("/home/user/workspace/github.com/gray-tech/bookbot/books/frankenstein.txt")
    word_count = count_words(text)
    print(f"{word_count} words found in the document")

main()