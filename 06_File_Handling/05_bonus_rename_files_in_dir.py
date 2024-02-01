import os
import re

directory = input("Enter a directory: ")
string_to_replace = input("Enter a string to replace: ")
string_to_replace_with = input("Enter a string to replace with: ")

for filename in os.listdir(directory):
    file = os.path.join(directory, filename)  # .\hello/file 1 => .\hello/file_1
    # [., hello, file 1][:-1] => ./hello + "/" + new_name => ./hello/new_name
    if os.path.isfile(file):
        new_name = filename.replace(string_to_replace, string_to_replace_with)
        new_file = "/".join(re.split(r"[\\/]", file)[:-1]) + "/" + new_name
        os.rename(file, new_file)
