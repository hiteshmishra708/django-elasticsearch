#Django Rest

##Installation and Setup

###Install the latest version [Python](https://www.python.org/downloads/) and Clone the Project from Bitbucket [Repository](https://github.com/hiteshmishra708/django_rest) or take a pull from the master branch if the repository already exists on your system using the below commands.
    $ git clone https://github.com/hiteshmishra708/django_rest.git
    $ git pull origin master

###Create and activate the python virtual environment with the below commands:

    $ pip install virtualenv
    $ virtualenv venv
    $ venv\Scripts\activate

###Install the re required packages with the command:

    $ pip install -r requirements.txt

###Create a migration and run the project with the below commands:

    $ python manage.py migrate
    $ python manage.py runserver
