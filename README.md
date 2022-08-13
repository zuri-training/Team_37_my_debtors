# Team_37_my_debtors
CoDebt is a web application that allows schools within a particular locality view, interact, and verify all debt information about a potential, present or past student. It's for school administrators, debtors and people who are interested in confirming their debt status. School administrators are able to create, retrieve, update and delete data upon authentication. Debtors can only view and contend in cases of perceived wrongful debt status.

## Prerequisites
Before you continue, ensure you have met the following requirements:

* You have python 3.5 and/or higher installed.
* You have a basic understanding of python.

### To Do
* Clone this repo and open the project on your preferred code editor 
```bash
git clone https://github.com/zuri-training/Team_37_my_debtors

```

* Change directory to the CoDebt directory `cd CoDebt`

* Install a virtual environment for your project
```bash
pip install virtualenv

```
* Install a virtual environment for your project
```bash
virtualenv <environment_name>
```

* Activate the virtual environment

```bash
env\scripts\activate

```

* Install all dependencies for the project 
```bash
pip install -r requirements.txt

```

### Running the App

--> To run the App, we use :
```bash
python manage.py runserver

```
###
```
For local development server.
In settings.py
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 
For production server
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
```
> ⚠ Then, the development server will be started at http://127.0.0.1:8000/

