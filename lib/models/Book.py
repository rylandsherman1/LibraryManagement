from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session, relationship
from lib.database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    isbn = Column(String, unique=True)
    available_copies = Column(Integer, default=1)

    borrow_records = relationship("BorrowRecord", back_populates="book")


def create_book(db: Session, book_data: dict):
    db_book = Book(**book_data)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: int):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
        return True
    return False


def get_all_books(db: Session):
    return db.query(Book).all()


def find_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def find_book_by_isbn(db: Session, isbn: str):
    return db.query(Book).filter(Book.isbn == isbn).first()


def find_books_by_title(db: Session, title: str):
    return db.query(Book).filter(Book.title.contains(title)).all()


def find_books_by_author(db: Session, author: str):
    return db.query(Book).filter(Book.author.contains(author)).all()
