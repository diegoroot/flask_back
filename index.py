from flask import Flask
from flask_cors import cross_origin
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app, resources={"/ingresar_sala": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/hello', methods=['GET', 'POST'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def main():
    print('algo')
    return 'Hola, mundo!'


if __name__ == '__main__':
    app.run(debug=True, port=5000)
