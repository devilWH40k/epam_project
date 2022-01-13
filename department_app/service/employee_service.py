"""Module for CRUD operations with employee table."""

import datetime
from department_app import db
from department_app.models import Employee


def get_employees() -> 'list[dict]':
    """Reads all the records from employee table.

    :return: list of employee dicts.
    """

    employees = Employee.query.all()
    return [employee.to_dict() for employee in employees]


def add_employee(name: str, surname: str, email: str,
                 brief_inf: str, birth_date: 'str',
                 salary: int, dep_id: str) -> None:
    """Creates employee by given values, then adds to table

    :param name: value of name field
    :param surname: value of surname field
    :param email: value of email field
    :param brief_inf: value of brief field
    :param birth_date: value of birth_date field in '%Y-%m-%d'
    :param salary: value of salary field
    :param dep_id: value of dep_id field
    """

    date_list = list(map(int, birth_date.split('-')))
    employee = Employee(
        name=name,
        surname=surname,
        email=email,
        brief_inf=brief_inf,
        birth_date=datetime.date(*date_list),
        salary=salary,
        dep_id=dep_id
    )
    db.session.add(employee)
    db.session.commit()


def update_employee(id: int, name: str, surname: str, email: str,
                    brief_inf: str, birth_date: str,
                    salary: int, dep_id: str) -> None:
    """Updates all fields of department by its id

    :param id: id of employee
    :param name: value of name field
    :param surname: value of surname field
    :param email: value of email field
    :param brief_inf: value of brief field
    :param birth_date: value of birth_date field in '%Y-%m-%d'
    :param salary: value of salary field
    :param dep_id: value of dep_id field
    """

    date_list = list(map(int, birth_date.split('-')))
    employee = Employee.query.get_or_404(id)
    employee.name = name
    employee.surname = surname
    employee.email = email
    employee.brief_inf = brief_inf
    employee.birth_date = datetime.date(*date_list)
    employee.salary = salary
    employee.dep_id = dep_id
    db.session.add(employee)
    db.session.commit()


def patch_update_employee(id: int, name: str, surname: str, email: str,
                    brief_inf: str, birth_date: str,
                    salary: int, dep_id: str) -> None:
    """Updates only specified employee fields

    :param id: id of employee
    :param name: value of name field
    :param surname: value of surname field
    :param email: value of email field
    :param brief_inf: value of brief field
    :param birth_date: value of birth_date field in '%Y-%m-%d'
    :param salary: value of salary field
    :param dep_id: value of dep_id field
    """

    employee = Employee.query.get_or_404(id)
    if name:
        employee.name = name
    elif surname:
        employee.surname = surname
    elif email:
        employee.email = email
    elif brief_inf:
        employee.brief_inf = brief_inf
    elif birth_date:
        date_list = list(map(int, birth_date.split('-')))
        employee.birth_date = datetime.date(*date_list)
    elif salary:
        employee.salary = salary
    elif dep_id:
        employee.dep_id = dep_id
    db.session.add(employee)
    db.session.commit()


def delete_employee(id) -> None:
    """Deletes employee by its id

    :param id: id of employee
    """

    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()


def get_employee_by_id(id) -> dict:
    """Reads an employee from table by id

    :param id: id of employee
    :return: employee dict
    """

    employee = Employee.query.get_or_404(id)
    return employee.to_dict()


