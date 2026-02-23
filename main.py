
from database.create_database import create_database
from database.create_tables import create_tables


def main():
    create_database()
    create_tables()


if __name__ == "__main__":
    main()