from main import app


class TestApi:

    def test_page_index(self):
        response = app.test_client().get('/movie/3%/')
        assert response.status_code == 200, 404
        assert type(response.json) == dict, 'Это не словарь!'

    def test_show_by_title_page(self):
        response = app.test_client().get('/movie/2015/to/2020/')
        assert response.status_code == 200, 404
        assert type(response.json) == list, 'Это не список!'

    def test_show_by_rating_children(self):
        response = app.test_client().get('/rating/children/')
        assert response.status_code == 200, 404
        assert type(response.json) == list, 'Это не список!'

    def test_show_by_rating_family(self):
        response = app.test_client().get('/rating/family/')
        assert response.status_code == 200, 404
        assert type(response.json) == list, 'Это не список!'

    def test_show_by_rating_adult(self):
        response = app.test_client().get('/rating/adult/')
        assert response.status_code == 200, 404
        assert type(response.json) == list, 'Это не список!'

    def test_show_by_genre(self):
        response = app.test_client().get('/genre/horror/')
        assert response.status_code == 200, 404
        assert type(response.json) == list, 'Это не список!'

    #  -------- > Помогите пожалуйста с этим тестом. < ---------- #

    # def test_page_index_nof_found(self):
    #     response = app.test_client().get('/movie/99999/')
    #     assert response.status_code == 404

    # ------------------------------------------------------------ #

    def test_show_by_title_page_not_found(self):
        response = app.test_client().get('/movie/9999/to/99999/')
        assert response.status_code == 404

    def test_show_by_rating_not_found(self):
        response = app.test_client().get('/rating/qwerty/')
        assert response.status_code == 404

    def test_show_by_genre_not_found(self):
        response = app.test_client().get('/genre/qwerty/')
        assert response.status_code == 404









