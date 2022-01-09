from department_app import app, db
from flask import render_template, redirect, flash, url_for
from department_app.models import Department, Employee


@app.route("/")
@app.route("/departments")
def show_departments():
    """Main page with all departments in db."""
    try:
        departments = Department.query.all()
    except:
        departments = None
    return render_template('departments.html', departments=departments)


@app.route("/departments/<dep_id>")
def show_department(dep_id):
    """Department page with its full information."""
    department = Department.query.get_or_404(dep_id)
    return render_template('department.html', department=department)


@app.route("/departments/delete/<dep_id>")
def delete_department(dep_id):
    """Route for deleting the department and all related employees by department id."""
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
    employee = Employee.query.get_or_404(emp_id)
    return render_template('employee.html', employee=employee)


@app.route("/employee/delete/<emp_id>")
def delete_employee(emp_id):
    """Route for deleting employee by his id."""
    employee = Employee.query.get_or_404(emp_id)
    db.session.delete(employee)
    db.session.commit()
    flash(f'{employee.name} {employee.surname[0]}. was successfully deleted!', category='success')

    # redirecting to the employees page
    return redirect(url_for('show_employees', dep_id=employee.dep_id))


@app.route("/manage")
def manage():
    return render_template('manage.html')
