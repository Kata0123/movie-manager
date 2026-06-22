import pytest

from movie_service import (
    add_movie,
    delete_movie,
    get_all_movies,
    update_movie,
    filter_by_genre,
    filter_by_year
)


def test_add_movie(tmp_path):
    file = tmp_path / "movies.json"

    add_movie("Avatar", 2009, 7.8, "Fantasy", file)

    movies = get_all_movies(file)

    assert len(movies) == 1


def test_delete_movie(tmp_path):
    file = tmp_path / "movies.json"

    add_movie("Avatar", 2009, 7.8, "Fantasy", file)

    delete_movie("Avatar", file)

    assert get_all_movies(file) == []


def test_update_movie(tmp_path):
    file = tmp_path / "movies.json"

    add_movie("Avatar", 2009, 7.8, "Fantasy", file)

    update_movie(
        "Avatar",
        {
            "title": "Avatar 2",
            "year": 2022,
            "rating": 8.0,
            "genre": "Sci-Fi"
        },
        file
    )

    movies = get_all_movies(file)

    assert movies[0]["title"] == "Avatar 2"


def test_filter_by_genre(tmp_path):
    file = tmp_path / "movies.json"

    add_movie("Avatar", 2009, 7.8, "Fantasy", file)
    add_movie("Titanic", 1997, 8.5, "Drama", file)

    result = filter_by_genre("Drama", file)

    assert len(result) == 1


def test_filter_by_year(tmp_path):
    file = tmp_path / "movies.json"

    add_movie("Avatar", 2009, 7.8, "Fantasy", file)

    result = filter_by_year(2009, file)

    assert len(result) == 1


def test_empty_title():
    with pytest.raises(ValueError):
        add_movie("", 2009, 8.0, "Fantasy")


def test_invalid_year():
    with pytest.raises(ValueError):
        add_movie("Movie", 1000, 8.0, "Fantasy")


def test_invalid_rating():
    with pytest.raises(ValueError):
        add_movie("Movie", 2020, 15, "Fantasy")