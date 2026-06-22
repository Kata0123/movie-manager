from movie_service import (
    add_movie,
    get_all_movies,
    delete_movie,
    update_movie,
    filter_by_genre,
    filter_by_year
)


def show_movies(movies):
    if not movies:
        print("Список пуст")
        return

    for movie in movies:
        print(
            f"{movie['title']} | "
            f"{movie['year']} | "
            f"{movie['rating']} | "
            f"{movie['genre']}"
        )


while True:
    print("\n Movie Manager")
    print("1. Добавить фильм")
    print("2. Показать все фильмы")
    print("3. Удалить фильм")
    print("4. Изменить фильм")
    print("5. Фильтр по жанру")
    print("6. Фильтр по году")
    print("0. Выход")

    choice = input("Выберите пункт: ")

    try:
        if choice == "1":
            title = input("Название: ")
            year = int(input("Год: "))
            rating = float(input("Рейтинг: "))
            genre = input("Жанр: ")

            add_movie(title, year, rating, genre)

            print("Фильм добавлен")

        elif choice == "2":
            show_movies(get_all_movies())

        elif choice == "3":
            title = input("Название фильма: ")
            delete_movie(title)
            print("Удалено")

        elif choice == "4":
            old_title = input("Название фильма: ")

            new_title = input("Новое название: ")
            year = int(input("Новый год: "))
            rating = float(input("Новый рейтинг: "))
            genre = input("Новый жанр: ")

            update_movie(
                old_title,
                {
                    "title": new_title,
                    "year": year,
                    "rating": rating,
                    "genre": genre
                }
            )

            print("Обновлено")

        elif choice == "5":
            genre = input("Жанр: ")
            show_movies(filter_by_genre(genre))

        elif choice == "6":
            year = int(input("Год: "))
            show_movies(filter_by_year(year))

        elif choice == "0":
            break

        else:
            print("Неверный пункт")

    except Exception as e:
        print("Ошибка:", e)