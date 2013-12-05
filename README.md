# {{ project_name|title }} Django Project #
## Prerequisites ##

- python >= 2.7
- pip
- virtualenv/wrapper (optional)

## Installation ##
### Creating the environment ###
Create a virtual python environment for the project.
If you're not using virtualenv you may skip this step.

#### Virtualenv ####
```bash
virtualenv --no-site-packages venv
source venv/bin/activate
```
or if using global packages (eg: mysql driver)
```bash
virtualenv --system-site-packages venv
```

### Install requirements ###
```bash
cd {{ project_name }}
pip install -r requirements.txt
```

### Configure project ###
For development environement
```bash
vim {{ project_name }}/settings_dev.py
```
For production environement
```bash
vim {{ project_name }}/settings.py
```

### Sync database ###
```bash
python manage.py syncdb
```

### Load initial data ###
```bash
python manage.py loaddata auth
```

## Running ##
```bash
python manage.py runserver
```

Open browser to http://127.0.0.1:8000
