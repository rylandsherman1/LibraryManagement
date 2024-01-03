from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Session
from lib.database import Base


class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True)
    membership_number = Column(String, unique=True)

    borrow_records = relationship("BorrowRecord", back_populates="member")


def create_member(db: Session, member_data: dict):
    db_member = Member(**member_data)
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member


def delete_member(db: Session, member_id: int):
    db_member = db.query(Member).filter(Member.id == member_id).first()
    if db_member:
        db.delete(db_member)
        db.commit()
        return True
    return False


def get_all_members(db: Session):
    return db.query(Member).all()


def find_member_by_id(db: Session, member_id: int):
    return db.query(Member).filter(Member.id == member_id).first()


def find_member_by_name(db: Session, name: str):
    return db.query(Member).filter(Member.name.contains(name)).all()


def find_member_by_email(db: Session, email: str):
    return db.query(Member).filter(Member.email == email).first()
