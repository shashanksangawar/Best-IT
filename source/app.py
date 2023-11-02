from flask import Flask, request, render_template
from flask_cors import CORS
from sold_connector import *
from stock_connector import *
app = Flask(__name__)
CORS(app)

@app.route('/')
def add_items():
    return render_template('index.html',display='')

@app.route('/insert', methods=['POST'])
def insert():
    try:
        # Getting Data Values from User
        data = request.form
        
        date = data['date']
        company_name = data['company_name']
        model_name = data['model_name']
        processor = data['processor']
        ssd = data['ssd'] 
        hdd = data['hdd']
        ram = data['ram']
        supplier = data['supplier']
        available_at = data['available_at']
        return render_template('index.html',display='Text Received')

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