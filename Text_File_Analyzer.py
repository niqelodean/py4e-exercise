try:
    filename = input("Enter filename: ")
    file = open(filename, "r")
    content = file.read()
    lines = content.split("\n")
    total_lines = len(lines)
    words = content.split()
    total_words = len(words)
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    print(f"total lines: {total_lines}")
    print (f"total words: {total_words}")
    print(f"longest word: {longest_word}")

except FileNotFoundError:
    print(f"Error: Can't find {filename}")
