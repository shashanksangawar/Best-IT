from flask import request, render_template
from sold_connector import *
from stock_connector import *


def delete_items(request_json):
    try:
        serial_nos = request_json.getlist('serial')
        try:
            flag=0
            connection_available = connect_to_available_database()
            cursor_available = connection_available.cursor()
            for serial in serial_nos:
                #query = "DELETE FROM product_issues WHERE SerialNum = '%s';" 
                query = f"DELETE FROM product_issues WHERE SerialNum = '{serial}';" 
                #cursor_available.execute(query,(serial))
                cursor_available.execute(query, )
                connection_available.commit()
                flag=1

                #query = "DELETE FROM product_images WHERE SerialNum = '%s';" 
                query = f"DELETE FROM product_images WHERE SerialNum = '{serial}';" 
                #cursor_available.execute(query,(serial))
                cursor_available.execute(query, )               
                connection_available.commit()
                flag=2

                #query = "DELETE FROM product_details WHERE SerialNo = '%s';" 
                #cursor_available.execute(query,(serial))
                query = f"DELETE FROM product_details WHERE SerialNo = '{serial}';" 
                cursor_available.execute(query, )
                connection_available.commit()
                flag=3

            cursor_available.close()
            close_connection(connection_available)
            if flag==3:
                return {'returncode': 10, 'message': 'Items deleted.'}, 200
            else:
                return flag
        except Exception as e :
            connection_available.commit()
            cursor_available.close()
            close_connection(connection_available)
            return {'returncode': 1, 'message': f'{e}'}, 503

    except Exception as e:
        cursor_available.close()
        close_connection(connection_available)
        return {'returncode': 1, 'message': 'Connection to Available Database was not formed.'}, 503


def update_items(serial_no, request_json):
    try:
        date = request_json['date']        
        serial = request_json['serial']        
        company_name = request_json['company_name']
        model_name = request_json['model_name']
        processor = request_json['processor']
        ssd = request_json['ssd'] 
        hdd = request_json['hdd']
        ram = request_json['ram']
        supplier = request_json['supplier']
        available_at = request_json['available_at']
        remarks = request_json['remarks']
        device_image = request.files['device'].read()

        try:
            connection_available = connect_to_available_database()
            cursor_available = connection_available.cursor()    
            query = f"UPDATE product_details SET PurchaseDate = '{date}', CompanyName= '{company_name}', ModelName='{model_name}', Processor='{processor}', SSD='{ssd}', HDD='{hdd}',  RAM='{ram}', Supplier='{supplier}', AvailableAt='{available_at}', Remarks='{remarks}' WHERE SerialNo = '{serial}';" 
            cursor_available.execute(query,)
            connection_available.commit()
            try:
                
                query = "UPDATE product_images SET Device = %s WHERE SerialNum = %s"
                cursor_available.execute(query, (device_image, serial_no))
                connection_available.commit()
                cursor_available.close()
                close_connection(connection_available)
                return {'returncode': 10, 'message': 'Items Updated.'}, 200
            except Exception as e :
                connection_available.commit()
                cursor_available.close()
                close_connection(connection_available)
                return {'returncode': 1, 'message': f'{e}'}, 503
        except Exception as e :
            connection_available.commit()
            cursor_available.close()
            close_connection(connection_available)
            return {'returncode': 1, 'message': f'{e}'}, 503

    except Exception as e:
        cursor_available.close()
        close_connection(connection_available)
        return {'returncode': 1, 'message': 'Connection to Available Database was not formed.'}, 503



def serial_no_pulling():
    try:
        connection = connect_to_available_database()  
        cursor = connection.cursor()
        try:
            query = f"SELECT SerialNo FROM product_details;"
            cursor.execute(query,)
            rows = cursor.fetchall()
            if rows is not None:
                return {'returncode': 10, 'message':'Data Retrieved', 'output':rows }
            else:
                connection.rollback()
                cursor.close()
                close_connection(connection)
                return {'returncode': 1, 'message':'No data to be displayed', 'output':[]}, 400
            
        except Exception as e:
            return {'returncode': 1, 'message':f'{e}', 'output':[]}
    except Exception as e:
        return {'returncode': 1, 'message':f'{e}', 'output':[]}

def insert_items():
    try:
        serial_nos = serial_no_pulling()
        condition = serial_nos['returncode']
        message = serial_nos['message']
        serial_nos = serial_nos['output']
        if condition != []:
            # Getting Data Values from User
            data = request.form
            serial_no = data['serial_no']
            for sno in serial_nos:
                s_no, = sno
                if s_no == serial_no:
                    return f'<h1>Duplicate Entry for {serial_no} please use another Serial No.</h1>'
            date = data['date']
            company_name = data['company_name']
            model_name = data['model_name']
            processor = data['processor']
            ssd = data['ssd'] 
            hdd = data['hdd']
            ram = data['ram']
            supplier = data['supplier']
            available_at = data['available_at']
            remarks = data['remarks']

            # Getting Files from User
            device_image = request.files['device'].read()
            # Connecting To DataBase
            connection = connect_to_available_database()  
            cursor = connection.cursor()
            try:
                query = "INSERT INTO product_details(SerialNo, PurchaseDate, CompanyName, ModelName, Processor, SSD, HDD, RAM, Supplier, AvailableAt, Remarks) VALUES (%s, %s, %s, %s, %s ,%s, %s, %s, %s, %s, %s)"
                cursor.execute(query, (serial_no, date, company_name, model_name, processor, ssd, hdd, ram, supplier, available_at, remarks))
                connection.commit()
                try:
                    
                    query = "INSERT INTO product_images(SerialNum, Device) VALUES (%s, %s)"
                    cursor.execute(query, (serial_no, device_image))
                    connection.commit()
                    cursor.close()
                    close_connection(connection)
                    return '<h1>Data Values were inserted.</h1>'

                except Exception as e :
                    query = "DELETE FROM product_images WHERE SerialNo='%s';"
                    cursor.execute(query,(serial_no))
                    connection.commit()
                    cursor.close()
                    close_connection(connection)
                    return f'{e}'
            except Exception as e :
                connection.rollback()
                cursor.close()
                close_connection(connection)
                return f'{e}'
        else:
            return message
    except Exception as e:
        return f'{e}'

def available_stock_working():
    try:
        connection = connect_to_available_database()  
        cursor = connection.cursor()
        try:
            # query = f"SELECT pd.* FROM product_details pd LEFT JOIN product_issues pi ON pd.SerialNo = pi.SerialNum WHERE pi.SerialNum IS NULL OR pi.SerialNum IS NULL;"
            query = f"SELECT * FROM product_details;"
            cursor.execute(query,)
            rows = cursor.fetchall()
            if rows is not None:
                return render_template('available_stock.html', product_data=rows)
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
            query = f"SELECT * FROM product_details;"
            cursor.execute(query,)
            rows = cursor.fetchall()
            if rows is not None:
                return render_template('sold_stock.html', product_data=rows)
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


def available_issue_working(serial_no,request_json):
    issues = request_json['issue']
    try:
        connection_available = connect_to_available_database()
        cursor_available = connection_available.cursor()
        try:
            # query = f"INSERT INTO product_issues(SerialNum, Issue) VALUES ('{serial_no}', '{issues}') ;"
            query = "INSERT INTO product_issues(SerialNum, Issue) VALUES ('%s', '%s') ;"
            cursor_available.execute(query, (serial_no, issues))
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

def sell_working(serial_no, request_json):
    customer_name = request_json['customer_name']
    customer_contact = request_json['customer_contact']
    selling_date = request_json['selling_date']
    warranty = request_json['warranty']
    image_proof = request.files['image_proof'].read()
    try:
        connection_available = connect_to_available_database()
        cursor_available = connection_available.cursor()
        try:
            query = f"SELECT * FROM product_details WHERE SerialNo = '{serial_no}';"
            cursor_available.execute(query)
            row = cursor_available.fetchone()
            if row is not None:
                serial_no, purchase_date, company_name, model_name, processor, ssd, hdd, ram, supplier, available_at, remarks = row
                del purchase_date; del supplier; del available_at; del remarks
                try:
                    query_images = f"SELECT Device FROM product_images WHERE SerialNum = '{serial_no}';"
                    cursor_available.execute(query_images)
                    row = cursor_available.fetchone()
                    if row is not None:
                        device, = row

                        # Deleting the Images
                        query = f"DELETE FROM product_images WHERE SerialNum = '{serial_no}';"
                        cursor_available.execute(query)
                        connection_available.commit()

                        # Deleting the Issues
                        query = f"DELETE FROM product_issues WHERE SerialNum = '{serial_no}';"
                        cursor_available.execute(query)
                        connection_available.commit()

                        # Deleting the details
                        query = f"DELETE FROM product_details WHERE SerialNo = '{serial_no}';"
                        cursor_available.execute(query)
                        connection_available.commit()

                        # Closing the Connection 
                        cursor_available.close()
                        close_connection(connection_available)
                        output = sell_working_2(serial_no, selling_date, company_name, model_name, processor, ssd, hdd, ram, customer_name, customer_contact, device, image_proof, warranty)
                        return {'returncode': 0, 'message': f'{output}'}, 200
                except Exception as e:
                    connection_available.rollback()
                    cursor_available.close()
                    close_connection(connection_available)
                    return {'returncode': 1, 'message': f'{e}'}, 503
            else:
                connection_available.rollback()
                cursor_available.close()
                close_connection(connection_available)
                return {'returncode': 1, 'message': 'No data to be inserted'}, 400
        except Exception as e:
            connection_available.rollback()
            cursor_available.close()
            close_connection(connection_available)
            return {'returncode': 1, 'message': f'{e}'}, 503
    except Exception as e:
        cursor_available.close()
        close_connection(connection_available)
        return {'returncode': 1, 'message': 'Connection to Available Database was not formed.'}, 503

def sell_working_2(serial_no, selling_date, company_name, model_name, processor, ssd, hdd, ram, customer_name, customer_contact, device, image_proof, warranty):
    connection_sold = connect_to_sold_database()
    cursor_sold = connection_sold.cursor()
    try:
        query = "INSERT INTO product_details(SerialNo, SellDate, CompanyName, ModelName, Processor, SSD, HDD, RAM, CustomerName, CustomerContact, Warranty) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor_sold.execute(query, (serial_no, selling_date, company_name, model_name, processor, ssd, hdd, ram, customer_name, customer_contact, warranty))
        connection_sold.commit()
        try:
            query = "INSERT INTO product_images(SerialNum, Device, ImageProof) VALUES (%s, %s, %s)"
            cursor_sold.execute(query, (serial_no, device, image_proof))
            connection_sold.commit()
            cursor_sold.close()
            close__connection(connection_sold)
            return "<h1>Item Sold!</h1>"
        except Exception as e:
            connection_sold.rollback()
            cursor_sold.close()
            close__connection(connection_sold)
            return {'returncode': 1, 'message': f'{e}'}, 503
    except Exception as e:
        connection_sold.rollback()
        cursor_sold.close()
        close__connection(connection_sold)
        return {'returncode': 1, 'message': f'{e}'}, 503
