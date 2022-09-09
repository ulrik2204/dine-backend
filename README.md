# dine-backend

The backend for Dine

## Getting started

To run this project, make sure you have Python 3.9 or higher installed
You also have to create a .env file, which if you runa development environment, can be a copy of `.env.example`.
To set up and run:

```bash
# Clone project
$ git clone https://gitlab.stud.idi.ntnu.no/tdt4140/landsby-3/gruppe-48/dine-backend.git
$ cd dine-backend

# Install virtualenv, a package to make virtual environments
$ pip install virtualenv

# Set up virtual environment named venv
$ python3 -m venv venv
# Activate the venv on Linux/Mac
$ source venv/bin/activate
# Activate the venv on Windows
$ venv/Scripts/activate

# Install dependencies
$ pip install -r requirements.txt

# Set up dev database (requires docker installed)
$ sh ./scripts/devdb.sh
# Run
$ python manage.py migrate
$ python manage.py runserver

```

## Development

**Everything should be done with the virtual environment active** 

It is activated with:
```bash
# On Mac/Linux
$ source venv/bin/activate

# On Windows
$ venv/Scrips/activate
```

### Changes and dependencies

After making changes

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

Install new dependencies with

```bash
$ pip install packagename
```

`Where 'packagename' is the name of the package `

After making a change to the projects dependencies, add them to requirements.txt with

```bash
$ pip freeze > requirements.txt
```

Deactivate the the venv with

```bash
$ deactivate
```

### Testing

Run tests with
```bash
$ python manage.py test
```

Test coverage:

```bash
# Run all tests with coverage. This will run all tests in dine.
$ coverage run --source=. manage.py test

# See the test report in command line
$ coverage report

# Generate test report as html
$ coverage html

```
