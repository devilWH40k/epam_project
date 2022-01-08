from department_app import app
from flask import render_template, url_for
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


@app.route("/employees/<dep_id>")
def show_employees(dep_id):
    department = Department.query.get_or_404(dep_id)
    employees = department.employees
    return render_template('employees.html', employees=employees, dep_name=department.name)


@app.route("/employee")
def employee():
    return render_template('employee.html')


@app.route("/manage")
def manage():
    return render_template('manage.html')
