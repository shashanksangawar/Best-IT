from flask import Flask, request, render_template
from flask_cors import CORS
from backend import *
import os
app = Flask(__name__)
CORS(app)

# Directory Path of current file 
source_path = os.path.dirname(__file__)
source_path = str(source_path)

# Configuration for Flask App
app._static_folder = "templates/static/"
app.secret_key = "secret key"

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

@app.route('/defective_stock')
def defective_stock():
        return defective_stock_working()



# Pure backend
@app.route("/issue",  methods=['POST'])
def issue():
    request_json = request.json
    issue_type = request_json.get('type')
    try:
        if issue_type == "Available":
            available_issue_working(request_json)
            return {'returncode': 10, 'message': f'Issue Received'}, 200
        elif issue_type == "Sold":
            sold_issue_working(request_json)
            return {'returncode': 10, 'message': f'Issue Received'}, 200
    except:
        return {'returncode': 1, 'message': 'No Issue Type Selected'}, 503


@app.route('/sell',  methods=['POST'])
def sell():
    return sell_working()

@app.route('/insert', methods=['POST'])
def insert():
    return insert_items(app=app)

# Index Page
@app.route('/')
def main_page():
    return render_template('index.html')

@app.route("/test")
def test():
    return "Test Approved from Best IT Computer Services"


if __name__ == "__main__":
    app.run(debug=True)