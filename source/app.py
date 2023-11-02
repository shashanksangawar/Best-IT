from flask import Flask, request
from flask_cors import CORS
from sold_connector import *
from stock_connector import *
app = Flask(__name__)
CORS(app)


@app.route('/insert', methods=['POST'])
def insert():
    try:
        # Getting Data Values from User
        data = request.get_json()
        date = data.get('date')
        company_name = data.get('company_name')
        model_name = data.get('model_name')
        processor = data.get('processor')
        ssd = data.get('ssd')
        hdd = data.get('hdd')
        ram = data.get('ram')
        supplier = data.get('supplier')
        available_at = data.get('available_at')


        # Connecting To DataBase
        connection = connect_to_database()  
        cursor = connection.cursor()
        try:
            query = "INSERT INTO product_details(Date, CompanyName, ModelName, Processor, SSD, HDD, RAM, Supplier, AvailableAt) VALUES (%s, %s, %s, %s ,%s, %s, %s, %s, %s)"
            cursor.execute(query, (date, company_name, model_name, processor, ssd, hdd, ram, supplier, available_at))
            connection.commit()
            return {'returncode': 10, 'message':'Data Values were inserted.'}, 200
        except :
            connection.rollback()
            cursor.close()
            close_connection(connection)
            return {'returncode': 1, 'message':'Data Values were not inserted.'}, 503
    except:
        return {'returncode': 1, 'message': 'Either Connection to Database was not Formed or the JSON is invalid.'}, 503


@app.route("/test")
def test():
    return "Test Approved from Best IT Computer Services"


if __name__ == "__main__":
    app.run()