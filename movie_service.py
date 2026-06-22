from storage import load_movies, save_movies


def add_movie(title, year, rating, genre, filename="movies.json"):
    if not title.strip():
        raise ValueError("Название не может быть пустым")

    if year < 1888:
        raise ValueError("Некорректный год")

    if rating < 0 or rating > 10:
        raise ValueError("Рейтинг должен быть от 0 до 10")

    movies = load_movies(filename)

    movie = {
        "title": title,
        "year": year,
        "rating": rating,
        "genre": genre
    }

    movies.append(movie)
    save_movies(movies, filename)

    return movie


def get_all_movies(filename="movies.json"):
    return load_movies(filename)


def delete_movie(title, filename="movies.json"):
    movies = load_movies(filename)

    filtered = [m for m in movies if m["title"] != title]

    if len(filtered) == len(movies):
        raise ValueError("Фильм не найден")

    save_movies(filtered, filename)


def update_movie(old_title, new_data, filename="movies.json"):
    movies = load_movies(filename)

    found = False

    for movie in movies:
        if movie["title"] == old_title:
            movie.update(new_data)
            found = True
            break

    if not found:
        raise ValueError("Фильм не найден")

    save_movies(movies, filename)


def filter_by_genre(genre, filename="movies.json"):
    movies = load_movies(filename)
    return [m for m in movies if m["genre"].lower() == genre.lower()]


def filter_by_year(year, filename="movies.json"):
    movies = load_movies(filename)
    return [m for m in movies if m["year"] == year]