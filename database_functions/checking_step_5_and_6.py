from database_functions.utils import search_by_actor, get_movie_by_type_year_and_genre


# Шаг 5
print('Проверка шага № 5')
print('-' * 30)
print(search_by_actor(actor_name_1='Rose McIver', actor_name_2='Ben Lamb'))
print('-' * 30)
print(search_by_actor(actor_name_1='Jack Black', actor_name_2='Dustin Hoffman'))


# Шаг 6
print('-' * 30)
print('Проверка шага № 6')
print(get_movie_by_type_year_and_genre(type_movie='Movie', release_year=2020, genre='Horror'))
