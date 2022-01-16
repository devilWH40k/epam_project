"""Views module for app routing logic."""

from flask import render_template, redirect, flash, url_for, request
from department_app.service import department_service, employee_service
from department_app.views import main


@main.route("/")
@main.route("/departments")
def show_departments():
    """Main page with all departments in db."""

    departments = department_service.get_departments()
    return render_template('departments.html', departments=departments)


@main.route("/departments/<dep_id>")
def show_department(dep_id):
    """Department page with its full information

    :param dep_id: id of department
    :return: rendered department page
    """

    department = department_service.get_department_by_id(dep_id)
    department['average_salary'] = department_service.get_average_salary(department)
    department['number'] = len(department['employees'])
    return render_template('department.html', department=department)


@main.route("/departments/delete/<dep_id>")
def delete_department(dep_id):
    """Route for deleting the department and all related employees by department id

    :param dep_id: id of department
    Redirects to departments page after deleting.
    """

    department = department_service.get_department_by_id(dep_id)
    for employee in department.get('employees'):
        employee_service.delete_employee(employee.get('id'))
    department_service.delete_department(department.get('id'))
    dep_name = department.get('name')
    flash(f'{dep_name} was successfully deleted!', category='success')
    return redirect(url_for('main.show_departments'))


@main.route("/employees/<dep_id>")
def show_employees(dep_id):
    """Route for page with employees from chosen department

    :param dep_id: id of department
    :return: rendered employees page
    """

    department = department_service.get_department_by_id(dep_id)
    employees = department['employees']
    return render_template('employees.html', employees=employees, dep_name=department['name'])


@main.route("/employee/<emp_id>")
def show_employee(emp_id):
    """Route for employee page got by his id.

    :param emp_id: id of employee
    :return: rendered employee page
    """

    employee = employee_service.get_employee_by_id(emp_id)
    return render_template('employee.html', employee=employee)


@main.route("/employee/delete/<emp_id>")
def delete_employee(emp_id):
    """Route for deleting employee by his id

    :param emp_id: id of employee
    Redirects to employees page after deleting.
    """

    employee = employee_service.get_employee_by_id(emp_id)
    employee_service.delete_employee(employee['id'])
    emp_name, emp_surname = employee['name'], employee['surname']
    flash(f'{emp_name} {emp_surname[0]}. was successfully deleted!', category='success')

    # redirecting to the employees page
    return redirect(url_for('main.show_employees', dep_id=employee['dep_id']))


@main.route("/manage", methods=['POST', 'GET'])
def manage():
    """Page with forms for adding departments and employees to database

    Firstly validates the forms.
    After POST request from the department's form redirects to departments page.
    In case with the employee's form redirects to employees page.
    Releases the flash messages after success.
    :return: rendered manage page
    """
    from department_app.forms import DepartmentForm, EmployeeForm

    dep_form = DepartmentForm()
    emp_form = EmployeeForm()

    # for avoiding both forms validation
    if request.form.get('description'):
        if dep_form.validate_on_submit():
            department_service.add_department(
                dep_form.name.data,
                dep_form.description.data
            )
            flash(f'{dep_form.name.data} was successfully created!', category='success')
            return redirect(url_for('main.show_departments'))
    else:
        if emp_form.validate_on_submit():
            employee_service.add_employee(
                emp_form.emp_name.data,
                emp_form.surname.data,
                emp_form.email.data,
                emp_form.brief_inf.data,
                emp_form.birth_date.data.strftime('%Y-%m-%d'),
                emp_form.salary.data,
                emp_form.dep_id.data
            )
            flash(f'{emp_form.emp_name.data} {emp_form.surname.data[0]}. was successfully added!',
                  category='success')
            return redirect(url_for('main.show_employees', dep_id=emp_form.dep_id.data))
    return render_template('manage.html', dep_form=dep_form, emp_form=emp_form)
