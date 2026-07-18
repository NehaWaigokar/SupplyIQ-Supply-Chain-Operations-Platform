from db_connector import get_db_connection

def add_new_product(name, price):
    conn = get_db_connection()
    if conn is None:
        return

    cursor = conn.cursor()
    try:
        # Use placeholders (%s) to prevent SQL Injection (a security best practice)
        query = "INSERT INTO Products (name, price) VALUES (%s, %s);"
        cursor.execute(query, (name, price))
        
        # IMPORTANT: Commit the change to save it permanently
        conn.commit()
        print(f"Success! {name} has been added to the system.")
        
    except Exception as e:
        print(f"Error adding product: {e}")
        conn.rollback() # Undo if something went wrong
    
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    # Test the function
    new_name = input("Enter product name: ")
    new_price = float(input("Enter product price: "))
    add_new_product(new_name, new_price)