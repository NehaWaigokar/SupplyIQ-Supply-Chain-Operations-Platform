from db_connector import get_db_connection

def update_stock(product_id, new_quantity):
    conn = get_db_connection()
    if conn is None:
        return

    cursor = conn.cursor()
    try:
        # We use the WHERE clause to update only the specific product
        query = "UPDATE Inventory SET stock_level = %s WHERE product_id = %s;"
        cursor.execute(query, (new_quantity, product_id))
        
        # Check if any row was actually updated
        if cursor.rowcount == 0:
            print("No product found with that ID.")
        else:
            conn.commit()
            print(f"Success! Stock updated for Product ID {product_id}.")
            
    except Exception as e:
        print(f"Error updating stock: {e}")
        conn.rollback()
    
    finally:
        cursor.close()
        conn.close()