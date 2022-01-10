"""Views module for app routing logic."""
from department_app import app, db
from flask import render_template, redirect, flash, url_for, request
from department_app.models import Department, Employee
from department_app.forms import DepartmentForm, EmployeeForm


@app.route("/")
@app.route("/departments")
def show_departments():
    """Main page with all departments in db."""
    departments = Department.query.all()
    return render_template('departments.html', departments=departments)


@app.route("/departments/<dep_id>")
def show_department(dep_id):
    """Department page with its full information."""
    department = Department.query.get_or_404(dep_id)
    return render_template('department.html', department=department)


@app.route("/departments/delete/<dep_id>")
def delete_department(dep_id):
    """Route for deleting the department and all related employees by department id.

    Redirects to departments page after deleting.
    """
    department = Department.query.get_or_404(dep_id)
    for employee in department.employees:
        db.session.delete(employee)
    db.session.delete(department)
    db.session.commit()
    flash(f'{department.name} was successfully deleted!', category='success')

    # redirecting to main page with departments after deleting
    return redirect(url_for('show_departments'))


@app.route("/employees/<dep_id>")
def show_employees(dep_id):
    """Route for page with employees from chosen department."""
    department = Department.query.get_or_404(dep_id)
    employees = department.employees
    return render_template('employees.html', employees=employees, dep_name=department.name)


@app.route("/employee/<emp_id>")
def show_employee(emp_id):
    """Route for employee page got by his id."""
    employee = Employee.query.get_or_404(emp_id)
    return render_template('employee.html', employee=employee)


@app.route("/employee/delete/<emp_id>")
def delete_employee(emp_id):
    """Route for deleting employee by his id.

    Redirects to employees page after deleting.
    """
    employee = Employee.query.get_or_404(emp_id)
    db.session.delete(employee)
    db.session.commit()
    flash(f'{employee.name} {employee.surname[0]}. was successfully deleted!', category='success')

    # redirecting to the employees page
    return redirect(url_for('show_employees', dep_id=employee.dep_id))


@app.route("/manage", methods=['POST', 'GET'])
def manage():
    """Page with forms for adding departments and employees to database.

    After POST request from the department's form redirects to departments page.
    In case with the employee's form redirects to employees page.
    """
    dep_form = DepartmentForm()
    emp_form = EmployeeForm()
    # for avoiding both forms validation
    if request.form.get('description'):
        if dep_form.validate_on_submit():
            department = Department(
                name=dep_form.name.data,
                description=dep_form.description.data
            )
            db.session.add(department)
            db.session.commit()
            flash(f'{department.name} was successfully created!', category='success')
            return redirect(url_for('show_departments'))
    else:
        if emp_form.validate_on_submit():
            employee = Employee(
                name=emp_form.emp_name.data,
                surname=emp_form.surname.data,
                email=emp_form.email.data,
                brief_inf=emp_form.brief_inf.data,
                birth_date=emp_form.birth_date.data,
                salary=emp_form.salary.data,
                dep_id=emp_form.dep_id.data
            )
            db.session.add(employee)
            db.session.commit()
            flash(f'{employee.name} {employee.surname[0]}. was successfully added to {employee.department.name}!',
                  category='success')
            return redirect(url_for('show_employees', dep_id=employee.dep_id))
    return render_template('manage.html', dep_form=dep_form, emp_form=emp_form)
