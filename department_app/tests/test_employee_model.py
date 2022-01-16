"""Module for testing department model"""

from department_app.tests.conftest import BaseTestCase


class TestEmployeeModel(BaseTestCase):
    """A Class for testing employee model."""

    def test_employee_model(self):
        """Tests employee's creation

        Checks id on existence, also looks
        whether repr correct or not. Testing to_dict method work
        """

        dict_ = self.create_records()
        department = dict_['department']
        employee = dict_['employee']
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
