import mysql.connector
from mysql.connector import errorcode

# Database configuration
config = {
    'user': 'your_username',    # Replace with your MySQL username
    'password': 'your_password',# Replace with your MySQL password
    'host': 'localhost'         # Replace with your MySQL host if it's not localhost
}

def create_database():
    try:
        # Establish the connection
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        
        # Create the database
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        
        # Commit the changes
        conn.commit()
        
        # Print success message
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        # Handle errors
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# Call the function to create the database
create_database()
