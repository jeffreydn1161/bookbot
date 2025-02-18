def char_counts(text):
    char_count_dict = {}
    for char in text.lower():
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    return char_count_dict

def word_count(text):
    return len(text.split())

def word_counting_report(book):
    formatted_output = f"--- Begin report of {book} ---\n"
    with open(book) as f:
        file_contents = f.read()
        formatted_output += f"{word_count(file_contents)} words found in the document\n\n"
        char_dict = char_counts(file_contents)
        for letter in "abcdefghijklmnopqrstuvwxyz":
            if letter in char_dict:
                formatted_output += f"The '{letter}' character was found {char_dict[letter]} times\n"
    formatted_output += "--- End report ---"
    return formatted_output

def main():
    print(word_counting_report("books/frankenstein.txt"))
        # print(word_count(file_contents))
        # print(char_counts(file_contents))

if __name__=="__main__":
    main()