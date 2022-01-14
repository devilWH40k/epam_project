# Department App

-------------
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

-------------
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

-------------
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
5. Run the application:
    ```sh
    $ flask run
    ```   
6. Fill the database with some random data, otherwise you will have nothing to work with:
    ```sh
    $ python3 data.py
    ``` 
-------------
**After these steps you shoud see something like that:**

![](https://github.com/devilWH40k/epam_project/blob/main/documentation/mockups/departments.png?raw=True)

-------------

# REST API operations

-------------
to be continued...

[page]: <https://www.servermania.com/kb/articles/install-sqlite/>