"""
Database connection utilities.

This module:
1. Loads database settings from YAML file
2. Creates connection to MySQL server
3. Creates connection to specific database
"""

import mysql.connector
import yaml
from utils.parser import parse_args , load_config


args = parse_args()

def get_server_connection():
    """
    Connect to MySQL server without specifying a database.
    Used for initial setup and database creation.
    """
    config = load_config()

    return mysql.connector.connect(
        host=config["database"]["host"],
        user=args.database_user,
        password=args.database_password
    )


def get_database_connection():
    """
    Connect directly to the inventory database.
    Used to create tables.
    """
    config = load_config()

    return mysql.connector.connect(
        host=config["database"]["host"],
        user=args.database_user,
        password=args.database_password,
        database=args.database_name
    )