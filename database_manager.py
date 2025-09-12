import mysql.connector

# You MUST replace these with your actual MySQL Workbench credentials.
DB_CONFIG = {
    'user': 'root',
    #'password': 'your_mysql_password',
    'host': '127.0.0.1', # or 'localhost'
    'database': 'e_hospital'
}

def connect_db():
    """Establishes a connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            return connection
    except mysql.connector.Error as e:
        st.error(f"Error connecting to MySQL database: {e}")
        return None

def user_exists(username, email):
    """
    Checks if a user with the given username or email already exists.
    Returns True if a user exists, False otherwise.
    """
    conn = connect_db()
    if conn is None:
        return True # Assume user exists to prevent new registrations on DB error
    
    cursor = conn.cursor()
    try:
        query = "SELECT * FROM users WHERE username = %s OR email = %s"
        cursor.execute(query, (username, email))
        result = cursor.fetchone()
        return result is not None
    except mysql.connector.Error as e:
        st.error(f"Error checking for existing user: {e}")
        return True
    finally:
        cursor.close()
        conn.close()

def register_user(username, email, password):
    """
    Registers a new user in the database.
    Returns True on success, False on failure.
    """
    conn = connect_db()
    if conn is None:
        return False

    cursor = conn.cursor()
    try:
        # Check if user already exists
        if user_exists(username, email):
            st.warning("Username or email already exists. Please choose a different one.")
            return False

        # If user does not exist, insert the new user
        query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, email, password))
        conn.commit()
        return True
    except mysql.connector.Error as e:
        st.error(f"Error during user registration: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

def login_user(username, password):
    """
    Checks if the provided username and password match a record in the database.
    Returns True on success, False on failure.
    """
    conn = connect_db()
    if conn is None:
        return False
    
    cursor = conn.cursor()
    try:
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        return result is not None
    except mysql.connector.Error as e:
        st.error(f"Error during user login: {e}")
        return False
    finally:
        cursor.close()
        conn.close()
