import sqlite3

# Path to your SQLite database
db_path = 'C:/Users/Kamarley/customer-order-app/customer_order_app/customers_orders.db'

# Function to get all tables in the database
def get_tables(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return [row[0] for row in cursor.fetchall()]

# Function to get all columns of a table
def get_columns(cursor, table_name):
    cursor.execute(f"PRAGMA table_info(\"{table_name}\");")
    return [(row[1], row[2]) for row in cursor.fetchall()]  # Column name and type

# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

try:
    # Get all tables
    tables = get_tables(cursor)
    print("Tables in the database:")
    for table in tables:
        print(f"Table: {table}")
        
        # Get and print columns for each table
        columns = get_columns(cursor, table)
        print("  Columns:")
        for column_name, column_type in columns:
            print(f"    Column: {column_name}, Type: {column_type}")
        print()  # Blank line for better readability

except sqlite3.OperationalError as e:
    print(f"Error: {e}")
finally:
    cursor.close()
    conn.close()


//atsk_a772794f78ca3b289e4aa2d6a36ac2d803300bd92de083bae5fb6d7493796bf5f084c18d