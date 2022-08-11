from flask import Blueprint, redirect, jsonify, abort
from database_functions.utils import find_by_title, find_by_release_year, \
    find_by_rating, find_by_listed_in

sql_blueprint = Blueprint('sql_blueprint', __name__)


@sql_blueprint.get('/')
def page_index():
    return redirect('/movie/3%/')


@sql_blueprint.get('/movie/<title>/')
def show_by_title_page(title):
    """Выводит данные о фильме по title - 'названию' """

    film = find_by_title(title)
    if not film:
        abort(404)
    return jsonify(film)


@sql_blueprint.get('/movie/<int:year_from>/to/<int:year_to>/')
def show_by_release_year(year_from, year_to):
    """ Выводит фильмы ОТ и ДО введенного промежутка лет в количестве 100 штук. """

    films = find_by_release_year(year_from, year_to)
    if not films:
        abort(404)
    return jsonify(films)


@sql_blueprint.get('/rating/<rating_name>/')
def show_by_rating(rating_name):
    """ Показывает список фильмов в количестве 100 штук в зависимости от рейтинга """

    films = find_by_rating(rating_name)
    if not films:
        abort(404)
    return films


@sql_blueprint.get('/genre/<genre>/')
def show_by_genre(genre):
    """ Показывает фильмы по жанру в количестве 100 штук """

    films = find_by_listed_in(genre)
    if not films:
        abort(404)
    return films
