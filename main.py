from flask import Flask, jsonify
from sql_views.views import sql_blueprint


app = Flask(__name__)
app.json.ensure_ascii = False
app.register_blueprint(sql_blueprint)


@app.errorhandler(404)
def page_400_error(error):
    """ Обработчик ошибок на стороне сервера"""

    return jsonify({"Error": 'Проверьте правильность вводимых данных'}), 404


if __name__ == "__main__":
    app.run(debug=True)
