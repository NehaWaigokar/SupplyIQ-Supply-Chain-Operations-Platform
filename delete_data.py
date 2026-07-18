from db_connector import get_db_connection

def delete_product(product_id):
    conn = get_db_connection()
    if conn is None:
        return

    cursor = conn.cursor()
    try:
        # Check if the product exists first
        cursor.execute("SELECT name FROM Products WHERE product_id = %s;", (product_id,))
        result = cursor.fetchone()
        
        if result:
            confirm = input(f"Are you sure you want to delete '{result[0]}'? (y/n): ")
            if confirm.lower() == 'y':
                cursor.execute("DELETE FROM Products WHERE product_id = %s;", (product_id,))
                conn.commit()
                print("Product deleted successfully.")
            else:
                print("Delete cancelled.")
        else:
            print("Product ID not found.")
            
    except Exception as e:
        print(f"Error deleting product: {e}")
        conn.rollback()
    
    finally:
        cursor.close()
        conn.close()