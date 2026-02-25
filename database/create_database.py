"""
Create database if it does not exist.
"""

from database.connection import get_server_connection, get_database_connection
from utils.parser import load_config, parse_args


def create_database():
    args = parse_args()
    config = load_config()
    conn = get_server_connection()
    cursor = conn.cursor()

    cursor.execute(
        f"CREATE DATABASE IF NOT EXISTS {args.database_name}"
    )


    cursor.close()
    conn.close()