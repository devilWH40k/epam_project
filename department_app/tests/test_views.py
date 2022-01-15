"""Module for testing views."""

import http
from department_app.tests.conftest import BaseTestCase


class TestViews(BaseTestCase):
    """Class for testing views."""

    def test_departments_view(self):
        """Tests home view with departments."""

        response = self.client.get('/')
        assert response.status_code == http.HTTPStatus.OK
        response = self.client.get('/departments')
        assert response.status_code == http.HTTPStatus.OK

    def test_department_view(self):
        """Tests department view."""

        department = self.create_records().get('department')
        url = f'/departments/{department.id}'
        response = self.client.get(url)
        assert response.status_code == http.HTTPStatus.OK

    def test_department_delete(self):
        """Tests department's delete view."""

        department = self.create_records().get('department')
        url = f'/departments/delete/{department.id}'
        response = self.client.get(url)
        assert response.status_code == http.HTTPStatus.FOUND

    def test_employees_view(self):
        """Tests view with employees list."""

        department = self.create_records().get('department')
        url = f'/employees/{department.id}'
        response = self.client.get(url)
        assert response.status_code == http.HTTPStatus.OK

    def test_employee_view(self):
        """Tests employee's page with his information."""

        employee = self.create_records().get('employee')
        url = f'/employee/{employee.id}'
        response = self.client.get(url)
        assert response.status_code == http.HTTPStatus.OK

    def test_employee_delete(self):
        """Tests employee's delete view."""

        employee = self.create_records().get('employee')
        url = f'/employee/delete/{employee.id}'
        response = self.client.get(url)
        assert response.status_code == http.HTTPStatus.FOUND

    def test_manage_view(self):
        """Tests manage view."""

        response = self.client.get('/manage')
        assert response.status_code == http.HTTPStatus.OK
