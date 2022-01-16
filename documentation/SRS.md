# Department App

The main purpose of this application is managing departments online by using
web browser on computer or smartphone. This site provides such functionality as:
- Getting information about departments on the main page
- Having a closer look at the department via its own page
- Check all the related employees by the 'employees' link
- Add more departments or employees on the manage page
- Delete all the stuff by clicking on the white cross
- Accessing the data by REST API architecture structure
-----
## Development software

- **Front-end**: HTML, CSS, Bootstrap
- **Back-end**: Flask, SQLite
-----
## User guide

You will see all the features of the application with example pictures down there

-----
### Home Page

At first, you will see the main page with all available departments which are stored
in database and shown as a cards

![](https://github.com/devilWH40k/epam_project/blob/main/documentation/mockups/home_page.png?raw=True)

Right on the card you will see Department title, brief information and two links

![](https://github.com/devilWH40k/epam_project/blob/main/documentation/mockups/department_card.png?raw=True)

If you click on 'Department link' you will be redirected to **Department Page**, 'Employees' link
to **Employees Page**, you can delete it from database by white cross, that action will delete
all the related employees also
-----
### Department Page
This page consist of full department information, its image, and some information
about related employees

![](https://github.com/devilWH40k/epam_project/blob/main/documentation/mockups/department.png?raw=True)

'Back' button brings you back to the 'Home Page'

-----
### Employees Page
There is a list of all related employees on this page, represented as cards

![](https://github.com/devilWH40k/epam_project/blob/main/documentation/mockups/employees.png?raw=True)

On employee's card you can see his fullname, brief resume and 'Employee link' that leads to
the 'Employee page'

![](https://github.com/devilWH40k/epam_project/blob/main/documentation/mockups/employee_card.png?raw=True)

You are able to delete the employee by same way as a department, just click on cross

-----
### Employee Page
This page consists of full information about employee and his picture, 'Back' button
leads you back to the 'Employee Page'

![](https://github.com/devilWH40k/epam_project/blob/main/documentation/mockups/employee.png?raw=True)

-----
### Manage Page
The main purpose of this page is adding new departments and employees to the database
by using forms with validation. Name of department must be unique

![](https://github.com/devilWH40k/epam_project/blob/main/documentation/mockups/department_form.png?raw=True)

In an employee form email must be unique

![](https://github.com/devilWH40k/epam_project/blob/main/documentation/mockups/employee_form.png?raw=True)

-----