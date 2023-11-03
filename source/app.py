from flask import Flask, request, render_template
from flask_cors import CORS
from sold_connector import *
from stock_connector import *
app = Flask(__name__)
CORS(app)
app._static_folder = "/home/joker/Desktop/backend/source/templates/static"

@app.route('/available_stock')
def available_stock():
    try:
        connection = connect_to_database()  
        cursor = connection.cursor()
        try:
            query = f"SELECT * FROM product_details;"
            cursor.execute(query,)
            rows = cursor.fetchall()
            # headings = ('Date', 'CompanyName', 'ModelName', 'Processor', 'SSD', 'HDD', 'RAM', 'Supplier', 'AvailableAt')
            if rows is not None:
                return render_template('available_stock.html', product_data=rows)
            else:
                connection.rollback()
                cursor.close()
                close_connection(connection)
                return {'returncode': 1, 'message':'No data to be displayed'}, 400
            
        except :
            connection.rollback()
            cursor.close()
            close_connection(connection)
            return {'returncode': 1, 'message':'Data Values were not inserted.'}, 503
    except:
        return {'returncode': 1, 'message': 'Connection to Database was not Formed.'}, 503
   

@app.route('/add_items')
def add_items():
    return render_template('add.html',display='')

@app.route('/insert', methods=['POST'])
def insert():
    try:
        # Getting Data Values from User
        data = request.form
        serial_no = data['serial_no']
        date = data['date']
        company_name = data['company_name']
        model_name = data['model_name']
        processor = data['processor']
        ssd = data['ssd'] 
        hdd = data['hdd']
        ram = data['ram']
        supplier = data['supplier']
        available_at = data['available_at']

        # Connecting To DataBase
        connection = connect_to_database()  
        cursor = connection.cursor()
        try:
            query = "INSERT INTO product_details(SerialNo, PurchaseDate, CompanyName, ModelName, Processor, SSD, HDD, RAM, Supplier, AvailableAt) VALUES (%s, %s, %s, %s, %s ,%s, %s, %s, %s, %s)"
            cursor.execute(query, (serial_no, date, company_name, model_name, processor, ssd, hdd, ram, supplier, available_at))
            connection.commit()
            cursor.close()
            close_connection(connection)
            return render_template('add.html',display='Data Values were inserted.')
        except Exception as e :
            connection.rollback()
            cursor.close()
            close_connection(connection)
            return render_template('add.html',display=f'{e}')
    except Exception as e:
        return render_template('add.html',display=f'{e}')

        return render_template('add.html',display='Either Connection to Database was not Formed or the JSON is invalid.')


@app.route("/test")
def test():
    return "Test Approved from Best IT Computer Services"


if __name__ == "__main__":
    app.run(debug=True)