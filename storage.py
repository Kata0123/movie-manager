import json
import os

DEFAULT_FILE = "movies.json"


def load_movies(filename=DEFAULT_FILE):
    if not os.path.exists(filename):
        return []

    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def save_movies(movies, filename=DEFAULT_FILE):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(movies, file, indent=4, ensure_ascii=False)