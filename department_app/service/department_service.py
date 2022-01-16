"""Module for CRUD operations with department table."""

from department_app import db
from department_app.models import Department


def get_departments() -> 'list[dict]':
    """Reads all the records from department table.

    :return: list of department dicts.
    """

    departments = Department.query.all()
    return [department.to_dict() for department in departments]


def add_department(name: str, description: str) -> dict:
    """Creates department by given values, then adds to table

    :param name: value of name field
    :param description: value of description field
    :return: dict of created department
    """

    department = Department(
        name=name,
        description=description
    )
    db.session.add(department)
    db.session.commit()
    return department.to_dict()


def update_department(id_, name: str, description: str) -> None:
    """Updates all fields of department by its id

    :param id_: id of department
    :param name: value of name field for update
    :param description: value of description field for update
    """

    department = Department.query.get_or_404(id_)
    department.name = name
    department.description = description
    db.session.add(department)
    db.session.commit()


def patch_update_department(id_, name: str, description: str) -> None:
    """Updates only specified department fields

    :param id_: id of department
    :param name: value of name field for update
    :param description: value of description field for update
    """

    department = Department.query.get_or_404(id_)
    if name:
        department.name = name
    elif description:
        department.description = description
    db.session.add(department)
    db.session.commit()


def delete_department(id_) -> None:
    """Deletes department by its id

    :param id_: id of department
    """

    department = Department.query.get_or_404(id_)
    db.session.delete(department)
    db.session.commit()


def get_department_by_id(id_) -> dict:
    """Reads a department from table by id

    :param id_: id of department
    :return: department dict
    """

    department = Department.query.get_or_404(id_)
    return department.to_dict()


def get_average_salary(department: dict) -> float:
    """Calculates the average salary of given department

    :param department: department dict
    :return: rounded number of employees
    """

    employees = department['employees']
    average_salary = 0
    if len(employees) > 0:
        for employee in employees:
            average_salary += employee['salary']
        average_salary /= len(employees)
    return round(average_salary, 1)
