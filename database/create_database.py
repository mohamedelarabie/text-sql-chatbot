"""
Create database if it does not exist.
"""

from database.connection import get_server_connection, load_db_config

def create_database():
    config = load_db_config()

    conn = get_server_connection()
    cursor = conn.cursor()

    cursor.execute(
        f"CREATE DATABASE IF NOT EXISTS {config['database']}"
    )

    print("Database ready.")

    cursor.close()
    conn.close()