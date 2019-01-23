# ... after removing and extra lines and having a symmetric file.
# NOTE: the code changes depending on the schema of the given file.

original_file_name = "./original/internet-de.num"
new_file_name = "./top-5k.txt"

raw_data = open(original_file_name, 'r').read().decode("utf-8")
lines = raw_data.split("\n")
words_array = []

for line in lines:
    split_line = line.split(" ")
    if len(split_line) == 3:
        words_array.append(split_line[2].strip())

open(new_file_name, 'w').write(",".join(words_array).encode("utf-8"))
