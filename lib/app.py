from lib.database import init_db, SessionLocal
from lib.cli import main_menu


def main():
    # Initialize the database
    init_db()

    # Start the CLI interface
    main_menu()


if __name__ == "__main__":
    main()
