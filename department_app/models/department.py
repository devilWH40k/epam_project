"""Module with Department class for engaging with department table."""

from department_app import db


class Department(db.Model):
    """Class for representing the department table."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(40), nullable=False, default='default_dep_img/default.png')
    employees = db.relationship('Employee', backref='department', lazy='dynamic')

    def to_dict(self):
        """Serializer that returns a dictionary from employee fields

        :return: the department in dictionary format
        """

        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'image_file': self.image_file,
            'employees': [employee.to_dict() for employee in self.employees]
        }

    def __repr__(self):
        """Method that represents department object

        :return: string with some information for identifying
        """

        return f'Department({self.name}, {self.image_file})'