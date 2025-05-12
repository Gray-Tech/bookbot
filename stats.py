def count_words(text):
    return len(text.split())

def count_characters(text):
    char_count = {}
    text = text.lower()
    for character in text:
        if character in char_count:
            char_count[character] += 1  # increment
        else:
            char_count[character] = 1  # start from 1
    return char_count  
def sort_characters(char_dict):
    sorted_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})
    sorted_list.sort(reverse=True, key=lambda d: d["num"])
    return sorted_list