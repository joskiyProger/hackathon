from os import getenv
from dotenv import load_dotenv
from datetime import datetime
from sqlalchemy import insert, select, update, delete
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
    total_money: Mapped[Numeric] = mapped_column(Numeric, nullable=False, default=0)
    max_month_money: Mapped[Numeric] = mapped_column(Numeric, nullable=False, default=0) 

    branch_relation = relationship("Branch", backref="employees")


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
    
    employee = relationship("Employee", backref="transactions")
    

    def __repr__(self):
        return (f"Transaction(id={self.id}, employee_id={self.employee_id}, "
                f"money={self.money}, date_time='{self.date_time}')")


def is_login_valid(email, password):
    with engine.connect() as conn:
        return len(conn.execute(select(Employee).filter_by(email=email, \
           password=password)).all()) == 1


def is_uid_exist(uid):
    with engine.connect() as conn:
        return len(conn.execute(select(Employee).filter_by(uid=uid)).all()) == 1


def set_uid(email, uid):
    with engine.connect() as conn:
        stmt = conn.execute(update(Employee).where(Employee.email == email).values(uid=uid))
        conn.commit()


def get_employee_by_uid(uid):
    with engine.connect() as conn:
        employee = conn.execute(select(Employee).filter_by(uid=uid)).all()[0]
        employee = \
            { 'id': employee.id, 'uid': employee.uid, 'surname': employee.surname, \
            'name': employee.name, 'patronymic': employee.patronymic, 'email': employee.email, \
            'branch': employee.branch, 'total_money': float(employee.total_money), \
            'max_month_money': float(employee.max_month_money), 'transactions': [] }

        transactions = conn.execute(select(Transaction).filter_by(employee_id=employee['id'])).all()
        for transaction in transactions:
            employee['transactions'].append( \
                { 'datetime': str(transaction.date_time), 'money': float(transaction.money) })

        return { "employee": employee }


def get_all_data():
    with engine.connect() as conn:
        employees = conn.execute(select(Employee))
        employees = \
            [{ 'uid': empl.uid, 'surname': empl.surname, 'name': empl.name, \
              'patronymic': empl.patronymic, 'email': empl.email, \
              'branch': empl.branch, 'total_money': int(empl.total_money), \
              'max_month_money': int(empl.max_month_money) } for empl in employees]

        branches = conn.execute(select(Branch))
        branches_list = [{ 'city': branch.city, 'money': int(branch.total_money) } \
                for branch in branches]

        transactions = conn.execute(select(Transaction))
        transactions_list = [{ 'employee_id': t.employee_id, 'money': int(t.money), \
                'date_time': str(t.date_time)} for t in transactions]

        data = \
            { "branches": branches_list, "transactions": transactions_list, "employees": employees }
        return data


def reset_all_transactions():
    with engine.connect() as conn:
        conn.execute(delete(Transaction))
        conn.execute(update(Employee).values(total_money=0))
        conn.execute(update(Branch).values(total_money=0))
        conn.commit()


def add_oleg_to_db():
    """Most useful function of this module"""
    with engine.connect() as conn:
        stmt = insert(Employee).values(surname="Олегов", name="Олег", patronymic="Фёдрович",
            email="heh@gmail.com", password="hihihaha", branch="Новосибирск", total_money=0)
        result = conn.execute(stmt)
        # conn.commit()
