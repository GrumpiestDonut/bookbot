def char_counter(file_contents):
    lowercase_string = file_contents.lower()
    chardictcount = {}
    for char in lowercase_string:
        chardictcount[char] = chardictcount.get(char, 0) + 1
    return chardictcount

def main():
    bookpath = "books/frankenstein.txt"
    with open(bookpath) as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)
    print(f"--- Begin report of {bookpath} ---")
    print(f"{word_count} words found in the document\n")
    chardictcount = char_counter(file_contents)
    # print(chardictcount) 
    for char, count in chardictcount.items():
       if char.isalpha():
    #       print(f"The SPACE character was found {count} times")
    #    else:
          print(f"The '{char}' character was found {count} times")
    print("--- End report ---")



if __name__ == "__main__":
    main()