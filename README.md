# dine-backend

The backend for Dine

## Getting started

To run this project, make sure you have Python 3.9 or higher installed
To set up and run:

```bash
# Clone project
$ git clone https://gitlab.stud.idi.ntnu.no/tdt4140/landsby-3/gruppe-48/dine-backend.git
$ cd dine-backend

# Install virtualenv, a package to make virtual environments
$ pip install virtualenv

# Set up virtual environment
$ python3 -m venv venv
$ source venv/bin/activate

# Install dependencies
$ pip install -r requirements.txt

# Activate and run (do every time)
$ source venv/bin/activate
$ python manage.py runserver

```

## Development

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

Before pushing to GitLab, deactivate the the venv with

```bash
$ deactivate
```

### Testing

Run tests with
./manage.py test

Test coverage:

```bash
# Run full tests with coverage. This will run all tests in dine.
$ coverage run --source=. manage.py test

# Generate test report
$ coverage html

# See the test report in command line
$ coverage report
```
