# Django-Blog-Website
A Django blog website where you can delve into captivating articles and easily become a contributor. You can contact the administrator through the website to share your own insightful content.

## Set up
1. Install python version>=3.11 and clone the repo
2. Create a virtual environment python -m venv venv
3. Activate the virtual environment source venv/bin/activate for unix based systems, venv\Scripts\activate for windows powershell, call venv\Scripts\activate for windows cmd
4. Install the requirements pip install -r requirements.txt
5. Enter the command in compiler terminal cd blog
6. Run the server python manage.py runserver

## Become a super user as an administrator of website
Go to the compiler terminal after completion of step 5 from above, and then enter python manage.py createsuperuser. Enter your desired username , password and press enter. Now you can access the admin pag of the website.
