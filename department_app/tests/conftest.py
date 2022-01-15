"""Module with base test case."""

import unittest
import datetime
from department_app import db, create_app
from department_app.config import TestConfig
from department_app.models import Department, Employee


class BaseTestCase(unittest.TestCase):
    """Class for base test case."""

    @staticmethod
    def create_records():
        """For creating records to db for tests.

        :return: dict with department and employee object
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
        return {'department': department, 'employee': employee}

    def setUp(self):
        """Calls before any test case."""
        self.app = create_app(test_config=TestConfig)
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        """Calls after any test case."""
        db.session.remove()
        db.drop_all()
