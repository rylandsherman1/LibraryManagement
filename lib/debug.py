from lib.database import SessionLocal
from lib.models.Book import create_book, get_all_books


def test_database_operations():
    # Create a new database session
    db = SessionLocal()

    try:
        # Test database operations
        print("Adding a new book...")
        create_book(
            db,
            {
                "title": "Sample Book",
                "author": "Author Name",
                "isbn": "1234567890",
                "available_copies": 5,
            },
        )

        print("Retrieving all books...")
        books = get_all_books(db)
        for book in books:
            print(f"Book: {book.title}, Author: {book.author}")

    finally:
        # Close the database session
        db.close()


if __name__ == "__main__":
    test_database_operations()
