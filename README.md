-----------MyFlaskApp----------------

**Framework Used**
  This project is built using Flask, a lightweight web framework for Python.



**How to Run the Project (Inside Ubuntu VM)**

Follow these steps to run `myflaskapp` on your Ubuntu Virtual Machine.
Note: You have to install python3 and flask in your VM

Step 1: Launch the terminal inside your Ubuntu VM.
Step 2: Navigate to Project Directory(myflaskapp)

	If your project is inside your home folder:
	bash
	cd ~/myflaskapp

	If it is Somewhere Else
	cd /media/myflaskapp

Step 3: Create Virtual Environment
	Run this in your Vm terminal

	python3 -m venv venv
	source venv/bin/activate\
 
Step 4: Install Dependencies

	Run this in your VM terminal
	pip install -r requirements.txt
 
Step 5: Run the app

	Run this command in the VM terminal
	python3 app.py

Step 5.1: you can also run this command

	export FLASK_APP=app.py
	export FLASK_ENV=development
	flask run --host=0.0.0.0

	export FLASK_APP=myflaskapp
	flask run --host=0.0.0.0

Step 6: access the app in your VM browser
	http://localhost:5000
	http://127.x.x:5000


**How to Run the Project (in host machine)**

step1: COnfigure first the firewall and the ports

	Run this command 
	sudo ufw allow 5000
	sudo ufw enable
	sudo ufw status

	if it is activated you are good to go
	
Step 2: Run this command one by one

	cd ~/myflaskapp
	source venv/bin/activate
	export FLASK_APP=app.py
	flask run --host=0.0.0.0 --port=5000

	you will see at the bottom there are 2 running
		the first one is for you VM ip address
		the second one is for your localhost machine ip address

Step3: go to your localhost machine and go to the browser 
	Type http://localhost:5000
	http://192.168.xxx.xxx:5000























