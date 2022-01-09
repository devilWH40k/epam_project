from department_app import db


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    brief_inf = db.Column(db.Text, nullable=False)
    birth_date = db.Column(db.DateTime, nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    image_file = db.Column(db.String(40), nullable=False, default='default_emp_img/default.png')
    dep_id = db.Column(db.String(40), db.ForeignKey('department.id'), nullable=False)

    def __repr__(self):
        return f'Employee({self.name}, {self.surname}, {self.salary})'
