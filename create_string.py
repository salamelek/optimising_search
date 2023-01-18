import random
import string

char_string = ""

for i in range(1000000):
    char_string += random.choice(list(string.ascii_lowercase))

with open("string.txt", "w") as file:
    file.write(char_string)