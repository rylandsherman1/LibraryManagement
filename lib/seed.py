from .database import SessionLocal
from .models.Book import create_book
from .models.Members import create_member
from .models.BorrowRecord import create_borrow_record
import datetime


def seed_books(db):
    books = [
        {
            "title": "The Hobbit",
            "author": "J.R.R. Tolkien",
            "isbn": "9780547928227",
            "available_copies": 3,
        },
        {
            "title": "The Lord of the Rings",
            "author": "J.R.R. Tolkien",
            "isbn": "9780547928203",
            "available_copies": 5,
        },
        {
            "title": "Fahrenheit 451",
            "author": "Ray Bradbury",
            "isbn": "9781451673319",
            "available_copies": 7,
        },
        {
            "title": "Jane Eyre",
            "author": "Charlotte Brontë",
            "isbn": "9780141441146",
            "available_copies": 8,
        },
        {
            "title": "Animal Farm",
            "author": "George Orwell",
            "isbn": "9780451526342",
            "available_copies": 4,
        },
        {
            "title": "Brave New World",
            "author": "Aldous Huxley",
            "isbn": "9780060850524",
            "available_copies": 6,
        },
        {
            "title": "Wuthering Heights",
            "author": "Emily Brontë",
            "isbn": "9780141439556",
            "available_copies": 9,
        },
        {
            "title": "Little Women",
            "author": "Louisa May Alcott",
            "isbn": "9780142408766",
            "available_copies": 20,
        },
        {
            "title": "Great Expectations",
            "author": "Charles Dickens",
            "isbn": "9780141439563",
            "available_copies": 15,
        },
        {
            "title": "Moby Dick",
            "author": "Herman Melville",
            "isbn": "9780142437247",
            "available_copies": 6,
        },
        {
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "isbn": "9780743273565",
            "available_copies": 10,
        },
        {
            "title": "To Kill a Mockingbird",
            "author": "Harper Lee",
            "isbn": "9780061120084",
            "available_copies": 5,
        },
        {
            "title": "1984",
            "author": "George Orwell",
            "isbn": "9780451524935",
            "available_copies": 2,
        },
        {
            "title": "Pride and Prejudice",
            "author": "Jane Austen",
            "isbn": "9780553213102",
            "available_copies": 8,
        },
        {
            "title": "The Catcher in the Rye",
            "author": "J.D. Salinger",
            "isbn": "9780316769488",
            "available_copies": 4,
        },
        # Add more books as needed
    ]

    for book_data in books:
        create_book(db, book_data)


def seed_members(db):
    members = [
        {
            "name": "Alex Johnson",
            "email": "alexjohnson98@hotmail.com",
            "membership_number": "84908608",
        },
        {
            "name": "Bethany Smith",
            "email": "bethanysmith98@yahoo.com",
            "membership_number": "89269608",
        },
        {
            "name": "Carlos Gomez",
            "email": "carlosgomez35@yahoo.com",
            "membership_number": "74084287",
        },
        {
            "name": "Diana Roberts",
            "email": "dianaroberts57@gmail.com",
            "membership_number": "83071385",
        },
        {
            "name": "Ethan Wright",
            "email": "ethanwright30@hotmail.com",
            "membership_number": "11606805",
        },
        {
            "name": "Fiona Taylor",
            "email": "fionataylor52@hotmail.com",
            "membership_number": "87645283",
        },
        {
            "name": "George Brown",
            "email": "georgebrown76@hotmail.com",
            "membership_number": "15200678",
        },
        {
            "name": "Hannah Evans",
            "email": "hannahevans40@yahoo.com",
            "membership_number": "11425187",
        },
        {
            "name": "Isaac Clark",
            "email": "isaacclark27@hotmail.com",
            "membership_number": "30872400",
        },
        {
            "name": "Jessica Lee",
            "email": "jessicalee52@gmail.com",
            "membership_number": "65720648",
        },
        {
            "name": "Kyle Martin",
            "email": "kylemartin4@hotmail.com",
            "membership_number": "52783225",
        },
        {
            "name": "Laura Davis",
            "email": "lauradavis91@gmail.com",
            "membership_number": "82242471",
        },
        {
            "name": "Michael Allen",
            "email": "michaelallen72@gmail.com",
            "membership_number": "35766245",
        },
        {
            "name": "Nina Harris",
            "email": "ninaharris65@outlook.com",
            "membership_number": "75891032",
        },
        {
            "name": "Owen Thompson",
            "email": "owenthompson65@outlook.com",
            "membership_number": "98249243",
        },
        # Add more members as needed
    ]

    for member_data in members:
        create_member(db, member_data)


def seed_borrow_records(db):
    borrow_records = [
        # {"book_id": 1, "member_id": 1, "borrow_date": datetime.datetime.utcnow()},
        # {"book_id": 2, "member_id": 2, "borrow_date": datetime.datetime.utcnow()},
        {
            "book_id": 9,
            "member_id": 12,
            "borrow_date": datetime.datetime(2024, 1, 4, 0, 47, 19, 861907),
        },
        {
            "book_id": 11,
            "member_id": 7,
            "borrow_date": datetime.datetime(2024, 1, 4, 0, 47, 19, 861913),
        },
        {
            "book_id": 10,
            "member_id": 4,
            "borrow_date": datetime.datetime(2024, 1, 4, 0, 47, 19, 861916),
        },
        {
            "book_id": 2,
            "member_id": 5,
            "borrow_date": datetime.datetime(2024, 1, 4, 0, 47, 19, 861920),
        },
        {
            "book_id": 4,
            "member_id": 8,
            "borrow_date": datetime.datetime(2024, 1, 4, 0, 47, 19, 861923),
        },
        {
            "book_id": 10,
            "member_id": 6,
            "borrow_date": datetime.datetime(2024, 1, 4, 0, 47, 19, 861926),
        },
        {
            "book_id": 9,
            "member_id": 9,
            "borrow_date": datetime.datetime(2024, 1, 4, 0, 47, 19, 861929),
        },
        {
            "book_id": 8,
            "member_id": 10,
            "borrow_date": datetime.datetime(2024, 1, 4, 0, 47, 19, 861933),
        },
        {
            "book_id": 1,
            "member_id": 11,
            "borrow_date": datetime.datetime(2024, 1, 4, 0, 47, 19, 861936),
        },
        {
            "book_id": 6,
            "member_id": 10,
            "borrow_date": datetime.datetime(2024, 1, 4, 0, 47, 19, 861940),
        },
        {
            "book_id": 10,
            "member_id": 15,
            "borrow_date": datetime.datetime(2024, 1, 4, 0, 47, 19, 861943),
        },
        {
            "book_id": 1,
            "member_id": 1,
            "borrow_date": datetime.datetime(2024, 1, 4, 0, 47, 19, 861947),
        },
        {
            "book_id": 13,
            "member_id": 10,
            "borrow_date": datetime.datetime(2024, 1, 4, 0, 47, 19, 861950),
        },
        {
            "book_id": 2,
            "member_id": 6,
            "borrow_date": datetime.datetime(2024, 1, 4, 0, 47, 19, 861954),
        },
        {
            "book_id": 9,
            "member_id": 9,
            "borrow_date": datetime.datetime(2024, 1, 4, 0, 47, 19, 861957),
        },
        {
            "book_id": 2,
            "member_id": 4,
            "borrow_date": datetime.datetime(2024, 1, 4, 0, 47, 19, 861961),
        },
        {
            "book_id": 8,
            "member_id": 13,
            "borrow_date": datetime.datetime(2024, 1, 4, 0, 47, 19, 861964),
        },
        {
            "book_id": 6,
            "member_id": 9,
            "borrow_date": datetime.datetime(2024, 1, 4, 0, 47, 19, 862396),
        },
        {
            "book_id": 4,
            "member_id": 8,
            "borrow_date": datetime.datetime(2024, 1, 4, 0, 47, 19, 862402),
        },
        {
            "book_id": 5,
            "member_id": 3,
            "borrow_date": datetime.datetime(2024, 1, 4, 0, 47, 19, 862405),
        },
        # Add more records as needed
    ]

    for record_data in borrow_records:
        create_borrow_record(db, record_data)


def main():
    db = SessionLocal()
    try:
        seed_books(db)
        seed_members(db)
        seed_borrow_records(db)
        print("Database seeded successfully.")
    except Exception as e:
        print(f"An error occurred while seeding the database: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    main()
