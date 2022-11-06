# Django Mars Rover Photo Search App

### Function:
Finds and displays all pictures taken by the Nasa Mars Exploration Rovers on a specific date.

### Resources Used:

NASA's Mars Rover Photos API:

https://api.nasa.gov/

## How to Use

1. Type a date into the search bar using a mm-dd-yyyy format date and hit enter.
2. Results will appear. You now have the ability to filter by rover and camera.
3. To start a new search, click on the date field and enter a new date 
    or click the home button and enter a new date at the homepage.

## Directions 

### 1. Clone the project
```sh
git clone https://github.com/E-A-Gee/Django-Mars-Rover.git
```


### 2. Create and activate virtual environment
More on virtual environments [here](https://realpython.com/python-virtual-environments-a-primer/).
```sh
# create local evironment
python -m venv <environment name>

# activate the environment -- Windows
<environment name>\Scripts\activate.ps1

# activate the environment -- Linux
source <environment name>/bin/activate

```


### 3. Install Python dependencies
```sh
pip install -r requirements.txt
```


### 4. Create environment variables for 'SECRET_KEY' and 'DEBUG_VALUE'
More on environment variables [here](https://djangocentral.com/environment-variables-in-django/).

Here is one way to set environment variables for Windows:
- Head to Control Panel > System and Security > System > Advanced System Systems
- Click the **Environment Variables** button (on the Advanced tab)
- Click **Edit** under *User variables for (User)*, not *System variables*

Set 'DEBUG_VALUE' to 'True' -- or 'False' if in production.

Generate a secret key and set 'SECRET_KEY' to this new value.

An easy way to generate a new secret key is the Python interpreter using secrets:
```sh
python
# secrets is a built-in Python module, so no need to install
import secrets
secrets.token_hex(24)
```



### 5. Update ALLOWED_HOSTS in rover_project/settings.py
Set allowed hosts to '*' to allow all hosts. '127.0.0.1' or '0.0.0.0' are other popular options.
More info on Django ALLOWED_HOSTS [here](https://docs.djangoproject.com/en/4.1/ref/settings/#allowed-hosts).
```sh
ALLOWED_HOSTS = ['*']
```


### 6. Run Django development server
```sh
# make sure you are in the same directory as manage.py
# or give the relative path to manage.py
python manage.py runserver
```
