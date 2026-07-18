from db_connector import get_db_connection

def get_all_products_as_list():
    conn = get_db_connection()
    if conn is None:
        return []

    cursor = conn.cursor()
    try:
        # Fetch data
        cursor.execute("SELECT name, price FROM Products;")
        products = cursor.fetchall()
        
        # Convert the raw database tuples into a list of dictionaries
        product_list = []
        for p in products:
            product_list.append({"name": p[0], "price": p[1]})
            
        return product_list

    except Exception as e:
        print(f"Error fetching data: {e}")
        return []
    
    finally:
        cursor.close()
        conn.close()