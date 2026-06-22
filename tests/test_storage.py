from storage import load_movies, save_movies


def test_save_and_load_movies(tmp_path):
    file = tmp_path / "movies.json"

    data = [
        {
            "title": "Avatar",
            "year": 2009,
            "rating": 7.8,
            "genre": "Fantasy"
        }
    ]

    save_movies(data, file)

    result = load_movies(file)

    assert result == data