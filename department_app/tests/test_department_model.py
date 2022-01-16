"""Module for testing department model"""

from department_app import db
from department_app.models import Department
from department_app.tests.conftest import BaseTestCase


class TestDepartmentModel(BaseTestCase):
    """A Class for testing department model."""

    def test_department_model(self):
        """Tests department's creation

        Checks id, employees attribute on existence, also looks
        whether repr correct or not. Testing to_dict method work
        """

        department = Department(name='Test', description='Some description')
        db.session.add(department)
        db.session.commit()
        test_dict = {
            'id': department.id,
            'name': department.name,
            'description': department.description,
            'image_file': department.image_file,
            'employees': []
        }
        self.assertTrue(department.id)
        self.assertEqual(department.employees, [])
        self.assertEqual(repr(department), 'Department(Test, default_dep_img/default.png)')
        self.assertDictEqual(test_dict, department.to_dict())
