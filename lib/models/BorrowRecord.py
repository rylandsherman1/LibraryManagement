from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship, Session
from lib.database import Base
import datetime


class BorrowRecord(Base):
    __tablename__ = "borrow_records"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    member_id = Column(Integer, ForeignKey("members.id"))
    borrow_date = Column(DateTime, default=datetime.datetime.utcnow)
    return_date = Column(DateTime)

    book = relationship("Book", back_populates="borrow_records")
    member = relationship("Member", back_populates="borrow_records")


def create_borrow_record(db: Session, borrow_data: dict):
    db_borrow_record = BorrowRecord(**borrow_data)
    db.add(db_borrow_record)
    db.commit()
    db.refresh(db_borrow_record)
    return db_borrow_record


def delete_borrow_record(db: Session, record_id: int):
    db_record = db.query(BorrowRecord).filter(BorrowRecord.id == record_id).first()
    if db_record:
        db.delete(db_record)
        db.commit()
        return True
    return False


def get_all_borrow_records(db: Session):
    return db.query(BorrowRecord).all()


def get_borrow_records_by_member_id(db: Session, member_id: int):
    return db.query(BorrowRecord).filter(BorrowRecord.member_id == member_id).all()


def get_borrow_records_by_book_id(db: Session, book_id: int):
    return db.query(BorrowRecord).filter(BorrowRecord.book_id == book_id).all()
