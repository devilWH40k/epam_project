"""Module that represents REST operations to work with employees."""

from flask import jsonify, request
from department_app.service import employee_service
from department_app.rest import api


@api.route('/employees', methods=['GET', 'POST'])
def get_employees():
    """Respond for POST and GET requests

    :return: if GET: all employees in json format
             if POST: If success returns an employee json,
             otherwise error(400) message in json format
    """

    if request.method == 'GET':
        employees = employee_service.get_employees()
        return jsonify(employees), 200

    if request.json is None:
        return jsonify({'message': 'No data!'}), 400
    name = request.json.get('name', '')
    surname = request.json.get('surname', '')
    email = request.json.get('email', '')
    brief_inf = request.json.get('brief_inf', '')
    birth_date = request.json.get('birth_date', '')
    salary = request.json.get('salary', '')
    dep_id = request.json.get('dep_id', '')
    if not all([name, surname, email, brief_inf,
               birth_date, salary, dep_id]):
        return jsonify({'message': 'Some data is not specified!'}), 400
    employee = employee_service.add_employee(name, surname, email, brief_inf,
                                             birth_date, salary, dep_id)
    return jsonify(employee), 201


@api.route('/employees/<emp_id>', methods=['GET'])
def get_employee(emp_id):
    """Respond for Get request

    :param emp_id: id of employee
    :return: employee in json format
    """

    employee = employee_service.get_employee_by_id(emp_id)
    return jsonify(employee), 200


@api.route('/employees/<emp_id>', methods=['PUT'])
def put_employee(emp_id):
    """Respond for PUT request

    :param emp_id: id of employee
    :return: success(201) or error(400) message in json format
    """

    if request.json is None:
        return jsonify({'message': 'No data!'}), 400
    name = request.json.get('name', '')
    surname = request.json.get('surname', '')
    email = request.json.get('email', '')
    brief_inf = request.json.get('brief_inf', '')
    birth_date = request.json.get('birth_date', '')
    salary = request.json.get('salary', '')
    dep_id = request.json.get('dep_id', '')
    if not all([name, surname, email, brief_inf,
               birth_date, salary, dep_id]):
        return jsonify({'message': 'Some data is not specified!'}), 400
    employee_service.update_employee(emp_id, name, surname, email,
                                     brief_inf, birth_date, salary, dep_id)
    return jsonify({'message': 'Employee has been updated'}), 201


@api.route('/employees/<emp_id>', methods=['PATCH'])
def patch_employee(emp_id):
    """Respond for PATCH request

    :param emp_id: id of employee
    :return: success(201) or error(400) message in json format
    """

    if request.json is None:
        return jsonify({'message': 'No data!'}), 400
    name = request.json.get('name')
    surname = request.json.get('surname')
    email = request.json.get('email')
    brief_inf = request.json.get('brief_inf')
    birth_date = request.json.get('birth_date')
    salary = request.json.get('salary')
    dep_id = request.json.get('dep_id')
    employee_service.patch_update_employee(emp_id, name, surname, email,
                                           brief_inf, birth_date, salary, dep_id)
    return jsonify({'message': 'Employee has been updated'}), 201


@api.route('/employees/<emp_id>', methods=['DELETE'])
def delete_employee(emp_id):
    """Respond for DELETE request

    :param emp_id: id of employee
    :return: success(200) message in json format
    """

    employee_service.delete_employee(emp_id)
    return jsonify({'message': 'Employee has been deleted'}), 200






