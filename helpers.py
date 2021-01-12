import os
import random
import requests

# Fetches a list of all words from an api and splits them into files
def generate_word_files():
    url = "https://www.tilvitnun.is/Api/GetSearchWords?searchType=A&word="
    data = requests.get(url).json()
    word_number = 0 
    file_number = 1 
    f = None
    MAX = 15000 # Determines the max number of words per file
    for d in data["list"]:
        if word_number % MAX == 0:
            if f:
                f.close()
            f = open(f"files/words{file_number}.txt", "w+", encoding="utf-8")
            file_number += 1
        word_number += 1
        f.write(d['word'] + "\n")

# Returns random word file
def get_random_file():
    return f"files/{random.choice(os.listdir('files'))}"

# Fetches a random file, reads all words and selects a random word
def get_random_word_from_file():
    filename = get_random_file()
    f = open(filename, "r", encoding="utf-8")
    words = [line for line in f.readlines()]
    return random.choice(words)