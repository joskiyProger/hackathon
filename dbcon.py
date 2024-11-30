from os import getenv
from dotenv import load_dotenv
from datetime import datetime
from sqlalchemy import insert
from sqlalchemy import create_engine, Integer, String, Numeric, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


load_dotenv("config.env")
DATABASE_URL = getenv("CONNECTION_STRING")
engine = create_engine(DATABASE_URL)


class Base(DeclarativeBase):
    pass


class Branch(Base):
    __tablename__ = "branches"
    
    city: Mapped[str] = mapped_column(String(30), primary_key=True)
    total_money: Mapped[Numeric] = mapped_column(Numeric, nullable=False)
    
    employees = relationship("Employee", back_populates="branch")
    

    def __repr__(self):
        return f"Branch(city='{self.city}', total_money={self.total_money})"


class Employee(Base):
    __tablename__ = "employees"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    uid: Mapped[str] = mapped_column(String(50), nullable=True)
    surname: Mapped[str] = mapped_column(String(25), nullable=False)
    name: Mapped[str] = mapped_column(String(25), nullable=False)
    patronymic: Mapped[str] = mapped_column(String(25), nullable=True)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    password: Mapped[str] = mapped_column(String(50), nullable=False)
    branch: Mapped[str] = mapped_column(String(30), ForeignKey("branches.city"), nullable=False)
    total_money: Mapped[Numeric] = mapped_column(Numeric, nullable=False)
    
    branch_relation = relationship("Branch", back_populates="employees")
    transactions = relationship("Transaction", back_populates="employee") 


    def __repr__(self):
        return (f"Employee(id={self.id}, uid='{self.uid}', surname='{self.surname}', "
                f"name='{self.name}', patronymic='{self.patronymic}', "
                f"email='{self.email}', branch='{self.branch}', total_money={self.total_money})")


class Transaction(Base):
    __tablename__ = 'transactions'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    employee_id: Mapped[int] = mapped_column(Integer, ForeignKey('employees.id'), nullable=False)
    money: Mapped[Numeric] = mapped_column(Numeric, nullable=False)
    date_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    
    employee = relationship("Employee", back_populates="transactions")
    

    def __repr__(self):
        return (f"<Transaction(id={self.id}, employee_id={self.employee_id}, "
                f"money={self.money}, date_time='{self.date_time}')>")


def add_oleg_to_db():
    with engine.connect() as conn:
        stmt = insert(Employee).values(surname="Олегов", name="Олег", patronymic="Фёдрович",
            email="heh@gmail.com", password="hihihaha", branch="Новосибирск", total_money=0)
        result = conn.execute(stmt)
        # conn.commit()
