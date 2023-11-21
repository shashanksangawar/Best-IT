from flask import render_template
from sold_connector import *
from stock_connector import *
from backend import *
import base64
def full_info_available_working(serial_no):
    try:
        connection_available = connect_to_available_database()
        cursor_available = connection_available.cursor()
        try:
            query = f"SELECT * FROM product_details WHERE SerialNo={serial_no};"
            cursor_available.execute(query,)
            rows = cursor_available.fetchone()
            try:
                    query = f"SELECT Device, ImageProof FROM product_images WHERE SerialNum={serial_no};"
                    cursor_available.execute(query,)
                    row = cursor_available.fetchone()
                    device ,image_proof = row
                    device = f"data:image/*;base64,{base64.b64encode(device).decode('utf-8')}"
                    image_proof = f"data:image/*;base64,{base64.b64encode(image_proof).decode('utf-8')}"
                    if row is not None:
                        return render_template('full_info_available.html', product_data=rows, device=device, image_proof=image_proof)
                    else:
                        connection_available.rollback()
                        cursor_available.close()
                        close_connection(connection_available)
                        return {'returncode': 1, 'message':'No data to be displayed'}, 400
        
            except Exception as e:
                connection_available.rollback()
                cursor_available.close()
                close_connection(connection_available)
                return {'returncode': 1, 'message':f'{e}'}, 503
        except Exception as e:
                connection_available.rollback()
                cursor_available.close()
                close_connection(connection_available)
                return {'returncode': 1, 'message':f'{e}'}, 503
    except Exception as e:
        cursor_available.close()
        close_connection(connection_available)
        return {'returncode': 1, 'message': 'Connection to Available Database was not formed.'}, 503


def full_info_sold_working(serial_no):
    try:
        connection_sold = connect_to_sold_database()
        cursor_sold = connection_sold.cursor()
        try:
            query = f"SELECT * FROM product_details WHERE SerialNo='{serial_no}';"
            print(query)
            cursor_sold.execute(query,)
            rows = cursor_sold.fetchone()
            try:
                query = f"SELECT Device, ImageProof FROM product_images WHERE SerialNum='{serial_no}';"
                cursor_sold.execute(query,)
                row = cursor_sold.fetchone()
                device ,image_proof = row
                device = f"data:image/*;base64,{base64.b64encode(device).decode('utf-8')}"
                image_proof = f"data:image/*;base64,{base64.b64encode(image_proof).decode('utf-8')}"
                if rows is not None:
                    return render_template('full_info_sold.html', product_data=rows, device=device, image_proof=image_proof)
                else:
                    connection_sold.rollback()
                    cursor_sold.close()
                    close__connection(connection_sold)
                    return {'returncode': 1, 'message':'No data to be displayed'}, 400
            except Exception as e:
                connection_sold.rollback()
                cursor_sold.close()
                close__connection(connection_sold)
                return {'returncode': 1, 'message':f'{e}'}, 503
            
        except Exception as e:
            connection_sold.rollback()
            cursor_sold.close()
            close__connection(connection_sold)
            return {'returncode': 1, 'message':f'{e}'}, 503
    except Exception as e:
        cursor_sold.close()  
        close__connection(connection_sold)
        return {'returncode': 1, 'message': 'Connection to Available Database was not formed.'}, 503
