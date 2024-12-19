def main(): 
    path_to_book = "books/frankenstein.txt"
    text = get_book_text(path_to_book)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    sorted_char_list = sort_char_count(char_count)
    
    print("--- Begin report of " + path_to_book + " ---")
    print(str(word_count) + " words found in the document")
    print()

    for item in sorted_char_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")
    
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_dict = {}
    import string
    for letter in string.ascii_lowercase:    
        letter_count = text.lower().count(letter)
        char_dict[letter] = letter_count
    return char_dict

def sort_on (dict):
    return dict["num"]

def sort_char_count(char_count):
    sorted_list = []
    for char in char_count:
        sorted_list.append({"char": char, "num": char_count[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()