"""Module with Employee class for engaging with employee table."""

from department_app import db
from department_app.models import Department


class Employee(db.Model):
    """Class for representing the employee table."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    brief_inf = db.Column(db.Text, nullable=False)
    birth_date = db.Column(db.DateTime, nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    image_file = db.Column(db.String(40), nullable=False, default='default_emp_img/default.png')
    dep_id = db.Column(db.String(40), db.ForeignKey('department.id'))

    def to_dict(self):
        """Serializer that returns a dictionary from employee fields.

        :return: the employee in dictionary format
        """
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
            'brief_inf': self.brief_inf,
            'birth_date': self.birth_date.strftime('%Y-%m-%d'),
            'salary': self.salary,
            'image_file': self.image_file,
            'dep_id': self.dep_id,
            'department': Department.query.get(self.dep_id).name
        }

    def __repr__(self):
        """Method that represents employee object

        :return: string with some information for identifying
        """

        return f'Employee({self.name}, {self.surname}, {self.salary})'
