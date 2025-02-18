def word_count(text):
    return len(text.split())

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(word_count(file_contents))

if __name__=="__main__":
    main()