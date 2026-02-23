"""
Database connection utilities.

This module:
1. Loads database settings from YAML file
2. Creates connection to MySQL server
3. Creates connection to specific database
"""

import mysql.connector
import yaml
from pathlib import Path



def load_db_config():
    """Load database configuration from YAML file."""
    config_path = Path("config/db_config.yaml")
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def get_server_connection():
    """
    Connect to MySQL server without specifying a database.
    Used for initial setup and database creation.
    """
    config = load_db_config()

    return mysql.connector.connect(
        host=config["host"],
        user=config["user"],
        password=config["password"]
    )


def get_database_connection():
    """
    Connect directly to the inventory database.
    Used to create tables.
    """
    config = load_db_config()

    return mysql.connector.connect(
        host=config["host"],
        user=config["user"],
        password=config["password"],
        database=config["database"]
    )