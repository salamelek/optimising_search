import time

# try optimising the search of a specific string

# index 999628:999636
string_to_find = "qyibkjhi"
results = []

with open("string.txt", "r") as file:
    char_string = file.read()


def alg_v1():
    counter = 0
    for i in range(len(char_string)):
        if char_string[i] == string_to_find[0]:
            counter = 0
            for j in range(len(string_to_find)):
                if char_string[i + j] == string_to_find[j]:
                    counter += 1
                if counter == len(string_to_find):
                    break


def alg_v2():
    for i in range(len(char_string)):
        if char_string[i:i + 8] == string_to_find:
            break


def alg_v3():
    for i in range(0, len(char_string), len(string_to_find)):
        if char_string[i] in string_to_find:
            pass


for attempt in range(100):
    start_time = time.monotonic()

    alg_v3()

    end_time = time.monotonic()
    elapsed_time = end_time - start_time
    results.append(elapsed_time)
    print(f"Elapsed time: {elapsed_time} ({attempt + 1}/100)")

print(f"\n====================================\n\nAverage time: {sum(results) / len(results)}")
