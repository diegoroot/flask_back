from flask import Flask
from flask_cors import cross_origin
from flask_cors import CORS
import psycopg2
import sys
from psycopg2 import OperationalError, errorcodes, errors, DatabaseError


app = Flask(__name__)
connection_bd = None

cors = CORS(app, resources={"/ingresar_sala": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

def connect():
    """ Connect to the PostgreSQL database server """
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        connection_bd = psycopg2.connect(
            host="ec2-34-201-95-176.compute-1.amazonaws.com",
            database="d6q0eu2isu1sgr",
            user="italbqvqzxpfjm",
            password="f608e6bd5c0206e27439f25335bb5ef86a986fb4961ae0a40c2309ed3adf47ab"
        )
        return connection_bd
    except (Exception, DatabaseError, OperationalError) as error:
        print(error)


def disconnect(connection_bd):
    """ disconnect to the PostgreSQL database server """
    try:
        connection_bd.close()
    except (Exception, DatabaseError, OperationalError) as error:
        print(error)


def execute_query(query):
    try:
        connection_bd = connect()
        cursor = connection_bd.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        disconnect(connection_bd)
        return data
    except (Exception, DatabaseError, OperationalError, errors.InFailedSqlTransaction) as error:
        print(error)
        # rollback the previous transaction before starting another
        if connection_bd:
            connection_bd.rollback()

def serialize_data(data):
    result = {
        'users': []
    }

    for dato in data:
        result.get('users').append({
            'code': dato[0],
            'name': dato[1]
        })
    return result




@app.route('/hello', methods=['GET', 'POST'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def main():
    print('algo')
    data = execute_query('select * from users_flask;')
    return serialize_data(data)


if __name__ == '__main__':
    app.run()
