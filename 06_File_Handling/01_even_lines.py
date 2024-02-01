symbols = ("-", ",", ".", "!", "?")

with open("files/file_1.txt", "r") as even_lines_file:
    text = even_lines_file.readlines()

for row in range(0, len(text), 2):

    for symbol in symbols:
        text[row] = text[row].replace(symbol, "@")

    print(text[row][::-1])
