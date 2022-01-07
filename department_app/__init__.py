from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route("/")
@app.route("/home")
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


if __name__ == '__main__':
    app.run(debug=True)