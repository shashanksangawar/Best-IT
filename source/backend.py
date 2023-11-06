from flask import Flask, request, render_template,flash
from flask_cors import CORS
from sold_connector import *
from stock_connector import *
from werkzeug.utils import secure_filename


def insert_items(app):
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

        # Getting Files from User
        # device_image = request.files['device']
        # image_proof = request.files['image_proof']

        # if (device_image.filename or image_proof.filename) == "":
        #     return {'returncode': 1, 'message': 'No File Selected.'}, 400

        # Connecting To DataBase
        connection = connect_to_available_database()  
        cursor = connection.cursor()
        try:
            query = "INSERT INTO product_details(SerialNo, PurchaseDate, CompanyName, ModelName, Processor, SSD, HDD, RAM, Supplier, AvailableAt) VALUES (%s, %s, %s, %s, %s ,%s, %s, %s, %s, %s)"
            cursor.execute(query, (serial_no, date, company_name, model_name, processor, ssd, hdd, ram, supplier, available_at))
            connection.commit()
            try:
                # if device_image or image_proof:
                # # secure_filename is needed to allow using user input as string
                #     device_image_file = secure_filename(device_image.filename)
                #     image_proof_file = secure_filename(image_proof.filename)
                #     sanitized_serial_no = secure_filename(serial_no)
                # # A directory of serial_no will be created
                #     os.system(f"mkdir source/.upload/{sanitized_serial_no}")

                # # Images will be stored in .upload/ folder
                #     file =  sanitized_serial_no +"/"+device_image_file  
                #     device_path = (os.path.join(app.config['UPLOAD_FOLDER'], file))
                #     device_image.save(device_path)
                #     file =  sanitized_serial_no +"/"+image_proof_file  
                #     image_proof_path = (os.path.join(app.config['UPLOAD_FOLDER'], file))
                #     image_proof.save(image_proof_path)

                # #   Giving Path in Database
                #     query = "INSERT INTO product_images(SerialNum, Device, ImageProof) VALUES (%s, %s, %s)"
                #     cursor.execute(query, (serial_no, image_proof_path, image_proof_path))
                #     connection.commit()
                #     cursor.close()
                #     close_connection(connection)
                    return render_template('add.html',display='Data Values were inserted.')
            except Exception as e :
                # query = "DELETE FROM product_images WHERE SerialNo='%s';"
                # cursor.execute(query,(serial_no))
                connection.commit()
                cursor.close()
                close_connection(connection)
                return render_template('add.html',display=f'{e}')    
        except Exception as e :
            connection.rollback()
            cursor.close()
            close_connection(connection)
            return render_template('add.html',display=f'{e}')
    except Exception as e:
        return render_template('add.html',display=f'{e}')

def available_stock_working():
    try:

        connection = connect_to_available_database()  
        cursor = connection.cursor()
        try:
            # query = f"SELECT * FROM product_details u, product_images a WHERE a.SerialNum=u.SerialNo;"
            query = f"SELECT * FROM product_details;"
            cursor.execute(query,)
            rows = cursor.fetchall()
            
            if rows is not None:
                return render_template('available_stock.html', product_data=rows,output='')
            else:
                connection.rollback()
                cursor.close()
                close_connection(connection)
                return {'returncode': 1, 'message':'No data to be displayed'}, 400
                
        except Exception as e:
            connection.rollback()
            cursor.close()
            close_connection(connection)
            return {'returncode': 1, 'message':f'{e}'}, 503
    except:
        return {'returncode': 1, 'message': 'Connection to Database was not Formed.'}, 503

def sold_stock_working():
    try:

        connection = connect_to_sold_database()  
        cursor = connection.cursor()
        try:
            # query = f"SELECT * FROM product_details u, product_images a WHERE a.SerialNum=u.SerialNo;"
            query = f"SELECT * FROM product_details;"
            cursor.execute(query,)
            rows = cursor.fetchall()
            
            if rows is not None:
                return render_template('sold_stock.html', product_data=rows)
            else:
                connection.rollback()
                cursor.close()
                close__connection(connection)
                return {'returncode': 1, 'message':'No data to be displayed'}, 400
                
        except Exception as e:
            connection.rollback()
            cursor.close()
            close__connection(connection)
            return {'returncode': 1, 'message':f'{e}'}, 503
    except:
        return {'returncode': 1, 'message': 'Connection to Database was not Formed.'}, 503

def defective_stock_working():
    try:

        connection = connect_to_available_database()  
        cursor = connection.cursor()
        try:
            query = f"SELECT * FROM product_issues;"
            cursor.execute(query,)
            rows = cursor.fetchall()
            
            if rows is not None:
                return render_template('defective.html', product_data=rows,output='')
            else:
                connection.rollback()
                cursor.close()
                close_connection(connection)
                return {'returncode': 1, 'message':'No data to be displayed'}, 400
                
        except Exception as e:
            connection.rollback()
            cursor.close()
            close_connection(connection)
            return {'returncode': 1, 'message':f'{e}'}, 503
    except:
        return {'returncode': 1, 'message': 'Connection to Database was not Formed.'}, 503


def available_issue_working(request_json):
    issues = request_json.get('issues')
    serial_no = request_json.get('serial_no')
    try:
        connection_available = connect_to_available_database()
        cursor_available = connection_available.cursor()
        try:
            query = f"INSERT INTO product_issues(SerialNum, Issue) VALUES ('{serial_no}', '{issues}') ;"
            cursor_available.execute(query, )
            connection_available.commit()
            cursor_available.close()
            close_connection(connection_available)
            return {'returncode': 10, 'message': f'Issue Received'}, 200

        except Exception as e:
            connection_available.rollback()
            cursor_available.close()
            close_connection(connection_available)
            return {'returncode': 1, 'message': f'{e}'}, 503
    except Exception as e:
        cursor_available.close()
        close_connection(connection_available)
        return {'returncode': 1, 'message': 'Connection to Available Database was not formed.'}, 503

def sold_issue_working(request_json):
    issues = request_json.get('issues')
    serial_no = request_json.get('serial_no')
    try:
        connection_sold = connect_to_sold_database()
        cursor_sold = connection_sold.cursor()
        try:
            query = f"INSERT INTO product_issues(SerialNum, Issue) VALUES ('{serial_no}', '{issues}');"
            cursor_sold.execute(query, )
            connection_sold.commit()
            cursor_sold.close()
            close__connection(connection_sold)

        except Exception as e:
            connection_sold.rollback()
            cursor_sold.close()
            close__connection(connection_sold)
            return {'returncode': 1, 'message': f'{e}'}, 503

    except Exception as e:
        cursor_sold.close()
        close__connection(connection_sold)
        return {'returncode': 1, 'message': 'Connection to Available Database was not formed.'}, 503


def sell_working():
    request_json = request.json
    customer_name = request_json.get('customer_name')
    customer_contact = request_json.get('customer_contact')
    selling_date = request_json.get('selling_date')
    serial_no = request_json.get('serial_no')
    try:
        connection_available = connect_to_available_database()
        cursor_available = connection_available.cursor()
        try:
            query = f"SELECT * FROM product_details WHERE SerialNo = '{serial_no}';"
            cursor_available.execute(query)
            row = cursor_available.fetchone()
            if row is not None:
                serial_no, purchase_date, company_name, model_name, processor, ssd, hdd, ram, supplier, available_at = row
                del purchase_date; del supplier; del available_at
                query = f"DELETE FROM product_details WHERE SerialNo = '{serial_no}';"
                cursor_available.execute(query)
                connection_available.commit()
                cursor_available.close()
                close_connection(connection_available)
                sell_working_2(serial_no, selling_date, company_name, model_name, processor, ssd, hdd, ram, customer_name, customer_contact)
            else:
                connection_available.rollback()
                cursor_available.close()
                close_connection(connection_available)
                flash(f"{e}.")
                return {'returncode': 1, 'message': 'No data to be inserted'}, 400
        except Exception as e:
            connection_available.rollback()
            cursor_available.close()
            close_connection(connection_available)
            flash(f"{e}.")
            return {'returncode': 1, 'message': f'{e}'}, 503
    except Exception as e:
        cursor_available.close()
        close_connection(connection_available)
        return {'returncode': 1, 'message': 'Connection to Available Database was not formed.'}, 503

def sell_working_2(serial_no, selling_date, company_name, model_name, processor, ssd, hdd, ram, customer_name, customer_contact):
    connection_sold = connect_to_sold_database()
    cursor_sold = connection_sold.cursor()
    try:
        query = "INSERT INTO product_details(SerialNo, SellDate, CompanyName, ModelName, Processor, SSD, HDD, RAM, CustomerName, CustomerContact) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor_sold.execute(query, (serial_no, selling_date, company_name, model_name, processor, ssd, hdd, ram, customer_name, customer_contact))
        connection_sold.commit()
        cursor_sold.close()
        close__connection(connection_sold)
        flash("Item Sold.")
        
    except Exception as e:
        connection_sold.rollback()
        cursor_sold.close()
        close__connection(connection_sold)
        return {'returncode': 1, 'message': f'{e}'}, 503

        
def issue_handler():
    issue_details = request.form.get('issue')
    