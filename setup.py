from setuptools import setup, find_packages

setup(
    name='department_app',
    version='1.0.0',
    description='simple web application for managing departments',
    author='Volodymyr Artemchuk',
    author_email='devilwork123123@gmail.com',
    url='https://github.com/devilWH40k/epam_project.git',
    install_requires=[
        'email-validator==1.1.3',
        'Flask>=2.0.2',
        'Flask-SQLAlchemy>=2.5.1',
        'Flask-WTF>=1.0.0',
        'py-loremipsum==1.1.0'
    ],
    include_package_data=True,
    packages=find_packages(exclude=['tests*'])
)
