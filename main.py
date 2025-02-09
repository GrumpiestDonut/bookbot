def myfunction(file_contents):
    my_string = file_contents
    lowercase_string = my_string.lower()
    count_a = lowercase_string.count('a')
    print(count_a)

def main():
    with open("/home/grumpydonut/workspace/github.com/GrumpiestDonut/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)
    print(word_count)
    myfunction()


if __name__ == "__main__":
    main()