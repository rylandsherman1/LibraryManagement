from .database import init_db, SessionLocal
from .cli import main_menu
# from .seed import main as seed_main


def main():
    # Initialize the database
    init_db()

    # seed_main()
    # Start the CLI interface
    main_menu()


if __name__ == "__main__":
    main()
