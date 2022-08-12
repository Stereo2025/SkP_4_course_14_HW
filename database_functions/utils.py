import sqlite3
from global_variables import DATABASE_PATH


with sqlite3.connect(DATABASE_PATH, check_same_thread=False) as file:
    cursor = file.cursor()


def find_by_title(title: str) -> dict:
    """
    Шаг 1.
    Функция возвращает 1 фильм по введенному title, либо TypeError если такого нет.
    :param title: Параметр ввода для поиска.
    """

    sql_query = f"""
                SELECT title, country, release_year, listed_in, description
                FROM netflix
                WHERE title LIKE '%{title}%'
                ORDER BY release_year DESC
                """
    cursor.execute(sql_query)
    result = cursor.fetchone()

    if not result:
        return result

    movie = {
        'title': result[0],
        'country': result[1],
        'release_year': result[2],
        'listed_in': result[3],
        'description': result[4]
    }
    return movie


def find_by_release_year(year_from: int, year_to: int) -> list[dict]:
    """
    Шаг 2.
    Возвращает фильмы по диапазону лет выпуска.

    :param year_from: С какого года осуществляется поиск.
    :param year_to: До какого года осуществляется поиск.
    :return: Возвращает 100 фильмов отсортированные с помощью DESC.
    """
    sql_query = f"""
                SELECT title, release_year
                FROM netflix
                WHERE release_year BETWEEN {year_from} AND {year_to}
                ORDER BY release_year DESC
                LIMIT 100
                """
    cursor.execute(sql_query)
    result = cursor.fetchall()

    movie_list = []
    for row in result:
        movie = {'title': row[0], 'release_year': row[1]}
        movie_list.append(movie)

    return movie_list


# def find_move_for_children() -> list[dict]:
#     """
#     Шаг 3.
#     Реализует поиск фильмов для детей.
#     :return: Список с фильмами.
#     """
#     sql_query = f"""
#                 SELECT title, rating, description
#                 FROM netflix
#                 WHERE rating = 'G'
#                 LIMIT 100
#                 """
#     cursor.execute(sql_query)
#     result = cursor.fetchall()
#
#     movie_list = []
#     for row in result:
#         movie = {'title': row[0], 'rating': row[1], 'description': row[2]}
#         movie_list.append(movie)
#
#     return movie_list
#
#
# def find_move_for_family() -> list[dict]:
#     """
#     Шаг 3.
#     Реализует поиск фильмов для семьи.
#     :return: Список с фильмами.
#     """
#     sql_query = f"""
#                 SELECT title, rating, description
#                 FROM netflix
#                 WHERE rating IN ('G', 'PG', 'PG-13')
#                 ORDER BY rating DESC
#                 LIMIT 100
#                 """
#     cursor.execute(sql_query)
#     result = cursor.fetchall()
#
#     movie_list = []
#     for row in result:
#         movie = {'title': row[0], 'rating': row[1], 'description': row[2]}
#         movie_list.append(movie)
#
#     return movie_list
#
#
# def find_move_for_adult() -> list[dict]:
#     """
#     Шаг 3.
#     Реализует поиск фильмов с ограничениями.
#     :return: Список с фильмами.
#     """
#     sql_query = f"""
#                 SELECT title, rating, description
#                 FROM netflix
#                 WHERE rating IN ('R', 'NC-17')
#                 ORDER BY rating DESC
#                 LIMIT 100
#                 """
#     cursor.execute(sql_query)
#     result = cursor.fetchall()
#
#     movie_list = []
#     for row in result:
#         movie = {'title': row[0], 'rating': row[1], 'description': row[2]}
#         movie_list.append(movie)
#
#     return movie_list


def find_by_rating(rating: str) -> list[dict] | None:
    """
    Шаг 3.
    Реализует поиск по рейтингу.
    :param rating: Параметр поиска.
    :return: Возвращает список доступных фильмов согласно введенному рейтингу.
    """

    list_rating = ['children', 'family', 'adult']

    if rating == list_rating[0]:
        sql_query = f"""
                    SELECT title, rating, description
                    FROM netflix
                    WHERE rating = 'G'
                    LIMIT 100
                    """
        cursor.execute(sql_query)
        result = cursor.fetchall()

    elif rating == list_rating[1]:
        sql_query = f"""
                    SELECT title, rating, description
                    FROM netflix
                    WHERE rating IN ('G', 'PG', 'PG-13')
                    ORDER BY rating DESC
                    LIMIT 100
                    """
        cursor.execute(sql_query)
        result = cursor.fetchall()

    elif rating == list_rating[2]:
        sql_query = f"""
                    SELECT title, rating, description
                    FROM netflix
                    WHERE rating IN ('R', 'NC-17')
                    ORDER BY rating DESC
                    LIMIT 100
                    """
        cursor.execute(sql_query)
        result = cursor.fetchall()

    else:
        return None

    movie_list = []
    for row in result:
        movie = {'title': row[0], 'rating': row[1], 'description': row[2]}
        movie_list.append(movie)

    return movie_list


def find_by_listed_in(genre: str) -> list[dict]:
    """
    Шаг 4.
    Реализует поиск по жанру.
    :param genre: Вводимые данные.
    :return: Название фильма и его описание.
    """

    sql_query = f"""
                SELECT title, description, release_year
                FROM netflix
                WHERE listed_in LIKE '%{genre}%'
                ORDER BY release_year DESC
                LIMIT 100
                """
    cursor.execute(sql_query)
    result = cursor.fetchall()

    movie_list = []
    for row in result:
        movie = {'title': row[0], 'description': row[1], 'release_year': row[2]}
        movie_list.append(movie)

    return movie_list


def search_by_actor(actor_name_1: str, actor_name_2: str) -> str:
    """
    Шаг 5.
    Ищет актеров, которые сыграли с actor_name_1 и actor_name_2 больше двух фильмов.
    :param actor_name_1: Имя актёра 1.
    :param actor_name_2: Имя актёра 2.
    :return: Актёров игравших с актёр 1 и актёр 2.
    """

    sqlite_query = f"""
                    SELECT netflix.cast
                    FROM netflix
                    WHERE netflix.cast LIKE '%{actor_name_1}%' 
                    AND netflix.cast LIKE '%{actor_name_2}%'
                    """
    cursor.execute(sqlite_query)
    result = cursor.fetchall()

    if not len(result):
        return f'Нет фильмов, в которых {actor_name_1} и {actor_name_2} играют вместе.'

    actor_list = []
    for row in result:
        actor = row[0].split(', ')
        actor_list.extend(actor)

    actors = {act for act in actor_list if actor_list.count(act) > 2} - {actor_name_1, actor_name_2}
    return '\n'.join(actors)


def get_movie_by_type_year_and_genre(type_movie: str, release_year: int, genre: str) -> list[dict] | str:
    """
    Шаг 6.
    Получает на выходе список названий картин с их описаниями в JSON.
    :param type_movie: Тип видео.
    :param release_year: Дата выхода.
    :param genre: Жанр видео.
    :return: Список[словарь] с введенными данными.
    """

    sqlite_query = f"""
                   SELECT title, description
                   FROM netflix
                   WHERE type LIKE '%{type_movie}%'
                   AND release_year LIKE {release_year}
                   AND listed_in LIKE '%{genre}%'
                   LIMIT 5
                   """
    cursor.execute(sqlite_query)
    result = cursor.fetchall()

    movie_list = []
    for row in result:
        movie = {'title': row[0], 'description': row[1]}
        movie_list.append(movie)

    if not len(movie_list):
        return 'Отсутствуют фильмы с такими параметрами'

    return movie_list
