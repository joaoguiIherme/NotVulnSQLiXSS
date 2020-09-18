# NotVulnSQLiXSS :zany_face:
Application with login page to test SQL Injection and comment session to test Cross-Site Scripting for the third project of Systems Security subject.

### Installation :cold_face:
	* Install dependencies
		-> pip install -r requirements.txt
				or
		-> pip3 install -r requirements.txt

	* Run the server
		-> python manage.py runserver
				or
		-> python3 manage.py runserver

### How to use :sunglasses:

	1. First you have to create a superuser, so you can create another normal users. Disable the server and run:
		-> python3 manage.py createsuperuser
			-> Enter the superuser name
			-> Enter the email (not required)
			-> Enter password then again to confirm

		-> python3 manage.py migrate

	2. Now run the server again:
		-> python3 manage.py runserver
	
	3. Navigate to the url 127.0.0.1:8000 or if you want to add another users: 127.0.0.1:8000/admin

	4. Now it's simple! First page is a login page where you can test SQLi commands. 

	5. After logged in, a comment session will show up. Now, you can try XSS commands to test the application.
