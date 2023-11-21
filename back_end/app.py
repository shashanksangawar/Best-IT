from flask import Flask, request, render_template, session
from flask_cors import CORS
from backend import *
from backend2 import *
# from global_variables import issue_serial, sold_serial
import os, secrets
app = Flask(__name__)
CORS(app)

issue_serial = None
sold_serial = None
# Directory Path of current file 
source_path = os.path.dirname(__file__)
source_path = str(source_path)

# Configuration for Flask App
app._static_folder = "templates/static/"
app.secret_key = secrets.token_hex(16)


# Display & backend
@app.route('/add')
def add_items():
    return render_template('add.html',display='')

@app.route('/sold_stock')
def sold_stock():
    return sold_stock_working()

@app.route('/available_stock')
def available_stock():
    return available_stock_working()

@app.route('/full_info')
def full_info():
    info_type = request.args.get('info_type')
    serial = request.args.get('serial_no')
    if info_type == 'Available':
        return full_info_available_working(serial_no=serial)
    if info_type == 'Sold':
        return full_info_sold_working(serial_no=serial)




@app.route('/defective_stock')
def defective_stock():
        return defective_stock_working()

@app.route('/issue')
def issue():
    value = request.args.get('serial_no')
    global issue_serial
    issue_serial = value
    return render_template('issue.html', serial_no=issue_serial)

@app.route("/issue_backend", methods=["GET", "POST"])
def issue_backend():
    form = request.form
    try:
        serial_no = issue_serial
        message, statuscode = available_issue_working(serial_no=serial_no, request_json=form)
        return f"<h1>{message['message']}</h1>"
    except Exception as err:
        return {'returncode': 1, 'message': f'{err}'}, 503


@app.route('/sell')
def sell():
    value = request.args.get('serial_no')
    global sold_serial
    sold_serial = value
    return render_template('sell.html', serial_no=sold_serial)

@app.route("/sell_backend", methods=["GET", "POST"])
def sell_backend():
    form = request.form
    try:
        serial_no = sold_serial
        message, statuscode = sell_working(serial_no=serial_no, request_json=form)
        return f"<h1>{message['message']}</h1>"
    except Exception as err:
        return {'returncode': 1, 'message': f'{err}'}, 503



@app.route('/insert', methods=['POST'])
def insert():
    return insert_items(app=app)

# Index Page
@app.route('/')
def main_page():
    return render_template('index.html')

@app.route("/test")
def test():
    return "<h1> Test Approved From Back-End </h1>"


if __name__ == "__main__":
    app.run(debug=True)