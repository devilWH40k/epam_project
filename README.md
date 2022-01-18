# Department App 
[![Build Status](https://app.travis-ci.com/devilWH40k/epam_project.svg?branch=main)](https://app.travis-ci.com/devilWH40k/epam_project)
[![Coverage Status](https://coveralls.io/repos/github/devilWH40k/epam_project/badge.svg)](https://coveralls.io/github/devilWH40k/epam_project)

Department app is quite simple web application for managing departments and its employees also.
It uses a RESTful service to perform CRUD and some other useful operations. There are a couple
of actions user is allowed to do:
- Get some information about departments on the main page
- Have a closer look at the department via its link
- Check all the related employees by the 'employees' link
- Add more departments or employees on the manage page
- Delete all the stuff by clicking on the white cross
-------------

## Preinstall usages

You need to have Python 3.6+ installed, also app uses the sqlite3 database, to install sqlite db on
Linux follow commands down there.

**(Debian/Ubuntu)**
```sh
$ sudo apt-get install sqlite3
```
**(CentOS / Fedora / RedHat)**
```sh
$ yum install sqlite3
```

If you have another OS visit this ----> **[page]** 

-------------

# Deployment

1. Clone the repository:
    ```sh
    $ git clone https://github.com/devilWH40k/epam_project.git
    ```
2. Move to project directory:
    ```sh
    $ cd epam_project
    ```
3. Create and activate the virtual environment:
    ```sh
    $ python3 -m venv venv
    $ source venv/bin/activate
    ```
4. Install application requirements:
    ```sh
    $ pip install -r requirements.txt
    ```
5. Fill the database with some random data, otherwise you will have nothing to work with:
    ```sh
    $ python3 data.py
    ``` 
6. Run the application in development mode by setting flask environment variables(http://127.0.0.1:5000 ):
    ```sh
    $ export FLASK_ENV=development
    $ flask run
    ```
   or you can run the application in production mode with gunicorn:
    ```sh
    $ gunicorn -w 4 "department_app:create_app()"
    ```
   will be available at http://127.0.0.1:8000 
-------------
**After these steps you shoud see something like that:**

![](https://github.com/devilWH40k/epam_project/blob/main/documentation/mockups/departments.png?raw=True)

-------------

# REST API operations

**api/departments**
- GET: to get all departments in json format
- POST: to add a new department
    ```sh
    {"name": "Name", "description": "Some description"}
    ```
-------------
**api/departments/id**
- GET: to get the department by its id in json format
- PUT: to completely update the department
    ```sh
    {"name": "New name", "description": "Some new description"}
    ```
- PATCH: to update only specified fields of department
    ```sh
    {"name": "New name"}
    ```
  or
    ```sh
    {"description": "Some new description"}
    ```
- DELETE: to delete the department by id
-------------
**api/employees**
- GET: to get all employees in json format
- POST: to add a new employee
    ```sh
    {"name": "Name", "surname": "Surname", "email": "test@gmail.com", 
    "brief_inf": "some brief info", "birth_date": "2001-03-02",
    "salary": 1000, "dep_id": "1"}
    ```
-------------
**api/departments/id**
- GET: to get the employee by id in json format
- PUT: to completely update the employee
    ```sh
    {"name": "New ame", "surname": "New Surname", "email": "new_test@gmail.com", 
    "brief_inf": "some new brief info", "birth_date": "2001-03-02",
    "salary": 1000, "dep_id": "1"}
    ```
- PATCH: to update only specified fields of employee
    ```sh
    {"name": "New ame", "surname": "New Surname"}
    ```
  or anything else you want to update
    ```sh
    {"birth_date": "2001-03-02", "salary": 1000}
    ```
- DELETE: to delete the employee by id


[page]: <https://www.servermania.com/kb/articles/install-sqlite/>