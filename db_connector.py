import psycopg2

def get_db_connection():
    try:
        # Replace these values with your actual database settings
        conn = psycopg2.connect(
            dbname="postgres",      # Your database name
            user="postgres",        # Your username
            password="Myself@123", # Your actual password
            host="localhost",       # Since it's on your computer
            port="5432"             # Default Postgres port
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

# Test the connection immediately
if __name__ == "__main__":
    connection = get_db_connection()
    if connection:
        print("Successfully connected to SupplyIQ Database!")
        connection.close()