def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text
def count_words(text):
    count = 0
    text_list = text.split(" ")
    for word in text_list():
        count = count + 1
    return count

def main():
    text = get_book_text("./books/frankenstein.txt")
    word_count = count_words(text)
    print(f"{word_count} words found in the document")

main()