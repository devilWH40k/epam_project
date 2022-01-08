from department_app import db


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    employees = db.relationship('Employee', backref='department', lazy=True)

    def __repr__(self):
        return f'Department({self.name}, {self.image_file})'