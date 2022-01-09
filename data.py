"""Script for uploading some randomly generated data to database.

This script firstly DROPS the database, then just creates a new one
based on modules and fills it by random data for future using by app
and application.
P.S. Departments' names always the same."""

import random
import loremipsum
import datetime
from department_app import db
from department_app.models import Department, Employee


names = (
    'James', 'David', 'Christopher', 'George', 'Ronald',
    'John', 'Richard ', 'Daniel', 'Kenneth ', 'Anthony',
    'Robert', 'Charles', 'Paul', 'Steven', 'Kevin',
    'Michael', 'Joseph', 'Mark', 'Edward', 'Jason',
    'Mary', 'Jennifer', 'Lisa', 'Sandra', 'Michelle',
    'Patricia', 'Maria', 'Nancy', 'Donna', 'Laura',
    'Linda', 'Susan', 'Karen', 'Carol', 'Sarah',
    'Barbara', 'Margaret', 'Betty', 'Ruth', 'Kimberly'
)
surnames = (
    'Smith', 'Anderson', 'Clark', 'Wright', 'Mitchell',
    'Johnson', 'Thomas', 'Rodriguez', 'Lopez', 'Perez',
    'Williams', 'Jackson', 'Lewis', 'Hill', 'Roberts',
    'Jones', 'White', 'Lee', 'Scott', 'Turner',
)
departments = (
    'Chicago Police Board', 'Buildings', 'Animal Care and Control',
    'Ethics', 'Finance', 'Fire'
)


def upload_data():
    """Function for uploading data by tuples."""

    db.drop_all()
    db.create_all()
    # for avoiding repeated emails
    email_number = 1
    for department_name in departments:
        dep_obj = Department(name=department_name,
                             description=loremipsum.generate(paragraph_count=1, prude=True))
        db.session.add(dep_obj)
        db.session.commit()
        for iter in range(0, random.randrange(9, 11)):
            emp_obj = Employee(
                name=random.choice(names),
                surname=random.choice(surnames),
                email='example' + str(email_number) + '@gmail.com',
                brief_inf=loremipsum.generate(paragraph_count=1, prude=True),
                birth_date=datetime.date(random.randrange(1995, 2005), 3, 4),
                salary=random.randrange(900, 3000, 100),
                dep_id=dep_obj.id
            )
            db.session.add(emp_obj)
            db.session.commit()
            email_number += 1


if __name__ == '__main__':
    upload_data()




