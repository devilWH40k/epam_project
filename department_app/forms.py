"""Module for storing web form classes."""

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, DateField, IntegerField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from department_app.models import Department, Employee


class DepartmentForm(FlaskForm):
    """Class that represents the Department form."""

    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=25)])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Create')

    def validate_name(self, name):
        """Method that checks the name uniqueness

        :param name: name of field to check
        :raises ValidationError: if validation was failed
        """

        validate_name = Department.query.filter_by(name=name.data).first()
        if validate_name:
            raise ValidationError('That department name is taken. Please choose a different one.')


class EmployeeForm(FlaskForm):
    """Class that represents the Employee form

    Checks on the email uniqueness
    """

    dep_id = SelectField('Works for?',
                         choices=[(dep.id, dep.name) for dep in Department.query.all()])
    emp_name = StringField('Name', validators=[DataRequired(), Length(min=2, max=25)])
    surname = StringField('Surname', validators=[DataRequired(), Length(min=2, max=25)])
    email = StringField('Email address', validators=[DataRequired(), Email()])
    brief_inf = TextAreaField('Brief resume', validators=[DataRequired()])
    birth_date = DateField('Birth date')
    salary = IntegerField('Salary', validators=[DataRequired()])
    submit = SubmitField('Create')

    def validate_email(self, email):
        """Method that checks the name uniqueness

        :param email: name of field to check
        :raises ValidationError: if validation was failed
        """

        validate_email = Employee.query.filter_by(email=email.data).first()
        if validate_email:
            raise ValidationError('That email is taken. Please choose a different one.')
