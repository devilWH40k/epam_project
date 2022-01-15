"""Module for testing department model"""

from department_app import db
from department_app.models import Department, Employee
from department_app.tests.conftest import BaseTestCase
import datetime


class TestEmployeeModel(BaseTestCase):
    """A Class for testing employee model."""

    def test_employee_model(self):
        """Tests employee's creation

        Checks id on existence, also looks
        whether repr correct or not. Testing to_dict method work
        """

        department = Department(name='Test', description='Some description')
        db.session.add(department)
        db.session.commit()
        employee = Employee(
                    name='Test',
                    surname='Tester',
                    email='test@gmail.com',
                    brief_inf='some brief information',
                    birth_date=datetime.date(2002, 8, 3),
                    salary=1337,
                    dep_id=department.id
                )
        db.session.add(employee)
        db.session.commit()
        test_dict = {
            'id': employee.id,
            'name': employee.name,
            'surname': employee.surname,
            'email': employee.email,
            'brief_inf': employee.brief_inf,
            'birth_date': employee.birth_date.strftime('%Y-%m-%d'),
            'salary': employee.salary,
            'image_file': employee.image_file,
            'dep_id': employee.dep_id,
            'department': department.name
        }
        self.assertTrue(employee.id)
        self.assertEqual(repr(employee), 'Employee(Test, Tester, 1337)')
        self.assertDictEqual(test_dict, employee.to_dict())
