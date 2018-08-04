WebLog
=
Brief introduction :
-
  Very small and simple.It's the first time that I use python to complete a simple project.
  
Initial operating environment: 
-
  ubuntu.
  
How to use
-
  (1)Create a Python Django development environment in a linux machine.
  Command:
    sudo apt-get update
    usdo apt-get -y upgrade
    
    sudo apt-get -y install python-pip
    sudo apt-get install virtualenv
  (2)Reinstall(or update) the used suite on your local computer.
  Command:
    cd webLog
    pip install -r 'requirements.txt'
  (3)Set up a database
  I use the database server named mysql.
  You need to creat a database based on the file named admin.
  (4)Start the server running:
   Command:
    source VENB/bin/activate
    cd webLog
    python manage.py runserver [the ip address of your linux machine ]:8000
  (5)Access the server using a browser
    Enter "https://[the ip address of your linux machine]:8000" into the browser's address bar.
    
Notice:
-
  This project is so simple that it cannot be used in practical situations.It is intended for use in python web development primitives.
  And the code needs to be modified and debugged to run properly.
      Now, I share it and hope to learn and improve with you.
      
Reference:
-
  《Django 架站的16堂课》 何敏煌 著
