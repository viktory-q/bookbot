def main():
    with open("books/frankenstein.txt") as file:
        file_contents = file.read().lower()
    char_counts = count_characters(file_contents)
    word_counts = count_words(file_contents)
    new_char_counts = convert_dict_to_list(char_counts)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_counts} words found in the document")

    for dict in new_char_counts:
        print(f"The '{dict['char']}' character was found {dict['num']} times")
    print("--- End report ---")
    
def sort_on(dict):
    return dict["num"]

def count_characters(text):
    char_counts = {}

    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def count_words(text):
   return len(text.split())


def convert_dict_to_list(dict):
    list_of_dictionaries = []
    for element in dict:
        if element.isalpha():
            new_dict = {"char": element, "num": dict[element]} 
            list_of_dictionaries.append(new_dict)
    list_of_dictionaries.sort(reverse=True, key=sort_on)
    return list_of_dictionaries

if __name__ == "__main__":
    main()