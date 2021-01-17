# stomble assignment bilal qureshi <br/>
 ## Steps to run the code,  I have also added them in the documentation <br/>
 
 #### I followed PEP 8 python format as much as I can. You can see the comments for better understanding of the code. I am also adding an API documentation for your ease
Stomble Assignment made in Flask Python <br/>
Please note the following: <br/>
1. In order to run this code first connect the database with mysql and run the .sql file in your mysql server<br/>
2. Than change the credentials to your database in db_config.py file. I have added my database credentials before. <br/>
3. Than go to the windows prompt and in the user_crud folder type python main.py <br/>
4. Go to 127.0.0.1:5000 to test the website <br/>
5. How ever I will give the video demonstration if the code is not working on PC other than mine.<br/>


#### Environment needed python 3.0 and above
I have also made a requirment.txt file please type  pip install -r requirements.txt  to install all libraries <br/>
Install the following libraries and type this in your windows command prompt or mac/linux terminal <br/>
You have to run the code by typing python main.py <br/>
when you are in user_crud folder. This can be done with both windows and mac terminal. <br/>
In order to run the code please install these libraries first. <br/>
Please install by typing this in your terminal one by one. <br/>
pip install app <br/>
pip install PyMySQL <br/>
pip install regex <br/>
pip install Flask <br/>
pip install Flask-MySQL <br/>
pip install Flask-Table <br/>

### Database deployment
To make it easier for you to deploy my database you can simply follow the below steps I will also add them in readme file. <br/>
(1) Download XAMPP from https://www.apachefriends.org/download.html  for your OS <br/>
(2) Than start XAMPP and click on start mySQL and as well as apache. And click on admin button of mysql. <br/>
(3) Once you arrive at the dashboard create a new database called "stomble" <br/>
(4) Go to the sql tab and copy paste stumble.sql to create and which will create and populate all the table <br/>
(5) now run the python code, you shouldn't have a need to edit credentials. <br/>
