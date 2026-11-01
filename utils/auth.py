import sqlite3
import hashlib
from typing import Optional, Tuple, Dict
import config

def hash_password(password: str) -> str:
    """Hashes a plaintext password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def get_connection():
    """Returns a SQLite connection to health_records.db."""
    conn = sqlite3.connect(str(config.DB_PATH), check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_auth_db():
    """Initializes the accounts table and pre-seeds the demo user."""
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        full_name TEXT NOT NULL,
        mobile TEXT,
        email TEXT,
        aadhaar TEXT,
        dob TEXT,
        gender TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()

    # Pre-seed demo user if not present
    demo_username = "ViddyaKS"
    demo_hash = hash_password("Viddya@5")
    c.execute("SELECT id FROM accounts WHERE username = ?", (demo_username,))
    if not c.fetchone():
        c.execute("""
        INSERT INTO accounts (username, password_hash, full_name, mobile)
        VALUES (?, ?, ?, ?)
        """, (demo_username, demo_hash, "Viddya KS (Demo User)", "9063209584"))
        conn.commit()
    conn.close()

def register_account(username, password, full_name, mobile, email="", aadhaar="", dob="", gender="") -> Tuple[bool, str]:
    """Registers a new user in the SQLite database."""
    init_auth_db()
    conn = get_connection()
    c = conn.cursor()
    try:
        c.execute("SELECT id FROM accounts WHERE username = ?", (username,))
        if c.fetchone():
            return False, "Username already exists. Please choose another."

        pwd_hash = hash_password(password)
        c.execute("""
        INSERT INTO accounts (username, password_hash, full_name, mobile, email, aadhaar, dob, gender)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (username, pwd_hash, full_name, mobile, email, aadhaar, str(dob), gender))
        conn.commit()
        return True, "Account successfully created!"
    except Exception as e:
        return False, f"Database error: {str(e)}"
    finally:
        conn.close()

def authenticate_user(username: str, password: str) -> Optional[Dict]:
    """Authenticates a user by username and password."""
    init_auth_db()
    conn = get_connection()
    c = conn.cursor()
    pwd_hash = hash_password(password)
    c.execute("SELECT * FROM accounts WHERE username = ? AND password_hash = ?", (username, pwd_hash))
    row = c.fetchone()
    conn.close()
    if row:
        return dict(row)
    return None

def get_user_by_mobile(mobile: str) -> Optional[Dict]:
    """Retrieves an account by registered mobile number."""
    init_auth_db()
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM accounts WHERE mobile = ?", (mobile,))
    row = c.fetchone()
    conn.close()
    if row:
        return dict(row)
    return None