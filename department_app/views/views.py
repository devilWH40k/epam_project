from department_app import app
from flask import render_template


@app.route("/")
@app.route("/departments")
def departments():
    return render_template('departments.html')


@app.route("/department")
def department():
    return render_template('department.html')


@app.route("/employees")
def employees():
    return render_template('employees.html')


@app.route("/employee")
def employee():
    return render_template('employee.html')


@app.route("/manage")
def manage():
    return render_template('manage.html')
