"""Module that represents REST operations to work with departments."""

from flask import jsonify, request
from department_app.service import department_service, employee_service
from department_app.rest import api


@api.route('/departments', methods=['GET', 'POST'])
def get_departments():
    """Respond for POST and GET requests

    :return: if GET: all departments in json format
             if POST: If success returns a department json,
             otherwise error(400) message in json format
    """

    if request.method == 'GET':
        departments = department_service.get_departments()
        return jsonify(departments), 200

    if request.json is None:
        return jsonify({'message': 'No data!'}), 400
    name = request.json.get('name', '')
    description = request.json.get('description', '')
    if not name or not description:
        return jsonify({'message': 'Some data is not specified!'}), 400
    department = department_service.add_department(name, description)
    return jsonify(department), 201


@api.route('/departments/<dep_id>', methods=['GET'])
def get_department(dep_id):
    """Respond for Get request

    :param dep_id: id of department
    :return: department in json format
    """

    department = department_service.get_department_by_id(dep_id)
    return jsonify(department), 200


@api.route('/departments/<dep_id>', methods=['PUT'])
def put_department(dep_id):
    """Respond for PUT request

    :param dep_id: id of department
    :return: success(201) or error(400) message in json format
    """

    if request.json is None:
        return jsonify({'message': 'No data!'}), 400
    name = request.json.get('name', '')
    description = request.json.get('description', '')
    if not name or not description:
        return jsonify({'message': 'Some data is not specified!'}), 400
    department_service.update_department(dep_id, name, description)
    return jsonify({'message': 'Department has been updated'}), 201


@api.route('/departments/<dep_id>', methods=['PATCH'])
def patch_department(dep_id):
    """Respond for PATCH request

    :param dep_id: id of department
    :return: success(201) or error(400) message in json format
    """

    if request.json is None:
        return jsonify({'message': 'No data!'}), 400
    name = request.json.get('name')
    description = request.json.get('description')
    department_service.patch_update_department(dep_id, name, description)
    return jsonify({'message': 'Department has been updated'}), 201


@api.route('/departments/<dep_id>', methods=['DELETE'])
def delete_department(dep_id):
    """Respond for DELETE request

    :param dep_id: id of department
    :return: success(200) message in json format
    """

    department = department_service.get_department_by_id(dep_id)
    for employee in department['employees']:
        employee_service.delete_employee(employee['id'])
    department_service.delete_department(department['id'])
    return jsonify({'message': 'Department has been deleted'}), 200
