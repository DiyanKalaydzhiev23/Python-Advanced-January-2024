import os


def save_extensions(dir_name, first_level=False):
    for filename in os.listdir(dir_name):
        file = os.path.join(dir_name, filename)

        if os.path.isfile(file):
            extension = filename.split(".")[-1]
            extensions[extension] = extensions.get(extension, []) + [filename]
        elif os.path.isdir(file) and not first_level:
            save_extensions(file, first_level=True)


directory = input("Enter a directory: ")
extensions = {}  # [py: [python.py, hello.py], ...}
result = []

try:
    save_extensions(directory)
except FileNotFoundError:
    print("Directory not found!")

extensions = sorted(extensions.items(), key=lambda x: x[0])

for extension, files in extensions:  # extension => py, files => [one.py, two.py]...
    result.append(f".{extension}")

    for file in sorted(files):
        result.append(f"- - - {file}")

with open("files/report.txt", "w") as report_file:
    report_file.write('\n'.join(result))
