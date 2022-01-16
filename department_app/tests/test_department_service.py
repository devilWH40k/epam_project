"""Module for testing department service."""

from department_app import db
from department_app.models import Department
from department_app.service import department_service
from department_app.tests.conftest import BaseTestCase


class TestDepartmentService(BaseTestCase):
    """Class for department service tests."""

    def test_get_departments(self):
        """Tests get_departments function

        At first, it creates three new departments, then
        checks the length of returned by tested function list
        """

        department_1 = Department(name='department_1', description='some desc')
        department_2 = Department(name='department_2', description='some desc')
        department_3 = Department(name='department_3', description='some desc')
        db.session.add(department_1)
        db.session.add(department_2)
        db.session.add(department_3)
        db.session.commit()
        self.assertEqual(3, len(department_service.get_departments()))

    def test_add_department(self):
        """Tests add_department function

        At first, it adds a new departments to a table, then
        checks by query the presents of this record
        """

        department_service.add_department(name='Add Test', description='some desc')
        department = Department.query.filter_by(name='Add Test').first()
        self.assertIsNotNone(department)

    def test_update_department(self):
        """Tests update_department function

        At first, it adds a new departments to a table, then
        updates the data and finally check
        """

        department = Department(name='Test', description='some desc')
        db.session.add(department)
        db.session.commit()
        department_service.update_department(id_=department.id, name='Update Test',
                                             description='some upd desc')
        upd_department = Department.query.filter_by(id=department.id).first()
        self.assertTupleEqual(('Update Test', 'some upd desc'),
                              (upd_department.name, upd_department.description))

    def test_patch_department(self):
        """Tests patch_update_department function

        At first, it adds a new departments to a table, then
        updates the data partially and finally check
        """

        department = Department(name='Test', description='some desc')
        db.session.add(department)
        db.session.commit()
        department_service.patch_update_department(id_=department.id,
                                                   name='PatchTest', description=None)
        ptch_department = Department.query.filter_by(id=department.id).first()
        self.assertTupleEqual(('PatchTest', 'some desc'),
                              (ptch_department.name, ptch_department.description))

    def test_delete_department(self):
        """Tests patch_update_department function

        At first, it adds a new departments to a table, then
        deletes the record and finally check
        """

        department = self.create_records()['department']
        department_service.delete_department(department.id)
        self.assertEqual(0, Department.query.count())

    def test_get_department_by_id(self):
        """Tests get_department_by_id function

        At first, it adds a new departments to a table, then
        gets the record and finally check
        """

        department = self.create_records()['department']
        test_department = department_service.get_department_by_id(department.id)
        self.assertEqual(department.name, test_department['name'])

    def test_get_average_salary(self):
        """Tests get_average_salary function

        At first, it imitates some employee data, then
        checks the result
        """

        department = {
            'employees': [
                {'salary': 1250},
                {'salary': 2500},
                {'salary': 760},
            ]
        }
        avg_salary = department_service.get_average_salary(department)
        self.assertEqual(avg_salary, 1503.3)
