# Django Mars Rover Photo Search App

Function
Finds and displays all pictures taken by the Nasa mars rovers on a specific date.

### Resources used:

NASA's Mars Rover Photos API:

https://api.nasa.gov/

## How to use

1. Type a date into the search bar using a dd-mm-yyyy format date and hit enter.
2. Results will appear. You now have te ability to filter by rover and camera.
3. To start a new search, click on the date field and enter a new date 
    or click the home button and enter a new date at the homepage.

## Directions 

### 1. Clone the project
```sh
Git clone https://github.com/E-A-Gee/Django-Mars-Rover.git
```


### 2. Create and activate virtual environment
More on virtual environments [here](https://realpython.com/python-virtual-environments-a-primer/).
```sh
#create local evironment
python -m venv project_env

#activate the environment
project_env\Scripts\activate.ps1

```


### 3. Install Python dependencies
```sh
pip install -r requirements.txt
```


### 4. Create environment variables for 'ROVER_SECRET_KEY' and 'ROVER_DEBUG_VALUE'
More on environment variables [here](https://kb.wisc.edu/cae/page.php?id=24500/) and [here](https://djangocentral.com/environment-variables-in-django/).

Set 'ROVER_DEBUG_VALUE to 'True'

An easy way to generate a new secret key (ROVER_SECRET_KEY) is the Python interpreter using secrets:
```sh
python
# secrets is a built-in Python module, so no need to install
import secrets
secrets.token_hex(24)
```


### 5. Create SQLite database, run migrations, create admin user
cd into the project directory (should be the folder with the manage.py file)
```sh
cd rover_project
python manage.py make migrations
python manage.py migrate
python manage.py createsuperuser
```


### 6. Run Django development server
```sh
python manage.py runserver
```

Note: if you see a Disallowed Host error message, you may want to add '127.0.0.1' or '0.0.0.0' to ALLOWED_HOSTS in rover_project/settings.py. Another possibility is setting ALLOWED_HOSTS = ['*']