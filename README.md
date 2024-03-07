### Hi there 👋

<!--
**amarnathreddy0201/amarnathreddy0201** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->

if u have any issue with pip conflicting use below commands
1) curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
2) python get-pip.py
3) 

pip install robotframework-selenium2library

For Django preparation:
  pip install virtualenvwrapper-win
  mkvirtualenv myproject
  workon myproject
  pip install django
  django-admin startproject "projectname"  #Name of the project
  django-admin startapp "app name"  or python manage.py startapp appname

  python manage.py showmigrations
  python manage.py migrate
  python manage.py makemigrations
  (model in sql format)python manage.py sqlmigrate meetings 0001(Follow this :- python manage.py "this is belongs to sqllite migrations" "This is app names in our project" "in our app check the       migrations and give starting name")
  if above command not working first make the migrations(makemigrations)
  python manage.py migrate(it will put data in sqlite)
  python manage.py createsuperuser

##### Virtual env for different python versions.
windows:
1) py -3.11 -m venv pyenv_3.11
2) Ex :-  py python_version -m venv your_venv_name.

python3.11 -m pip install ultralytics

Linux:
 python3 -m venv pyven_3.11

pip install --user pipenv
pipenv install django

######    logging files ####################
import logging
logging.basicConfig(level=logging.INFO, filename='sample.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(filename)s - %(lineno)d')
logger = logging.getLogger(__name__)
logger.info("print")

######################### CPP #############################
1) Boost continuous sending data .
2) https://stackoverflow.com/questions/72293309/boost-post-request-continuously-cpp

######################### CPP #############################
1) Boost continuous sending data .
2) https://stackoverflow.com/questions/72293309/boost-post-request-continuously-cpp

3) https://github.com/lagadic/visp/blob/master/cmake/FindPylon.cmake pypylon cmake
4) Opencv include in cmake : https://gist.github.com/UnaNancyOwen/9d25d9ef66b163e0667b4b3bf3962f8a
5) Spdlog :   https://github.com/gabime/spdlog/blob/v1.x/CMakeLists.txt

This is forlearning.
###################  AWS ##############################
1) Check the table exist or not : https://stackoverflow.com/questions/42485616/how-to-check-if-dynamodb-table-exists#:~:text=You%20can%20use%20the%20ListTables,you%20request%20doesn't%20exist.

##### fastapi with lambda(windows) ###################
1) pip freeze>requirements.txt
2) pip install -t dependencies -r requirements.txt
3) Compress-Archive -Path .\dependencies -DestinationPath .\lambda_function.zip
4) Compress-Archive -Path .\main.py -DestinationPath .\lambda_function.zip -Update

Classification	Detection	Segmentation	Kind
yolov8n-cls.pt	yolov8n.pt	yolov8n-seg.pt	Nano
yolov8s-cls.pt	yolov8s.pt	yolov8s-seg.pt	Small
yolov8m-cls.pt	yolov8m.pt	yolov8m-seg.pt	Medium
yolov8l-cls.pt	yolov8l.pt	yolov8l-seg.pt	Large
yolov8x-cls.pt	yolov8x.pt	yolov8x-seg.pt	Huge

**Creating a Python virtual environment in Linux**
1) pip is not in your system : sudo apt-get install python-pip
2) pip install virtualenv
3) Create a virtual environment now,
    $ virtualenv virtualenv_name
4) virtualenv -p /usr/bin/python3 virtualenv_name
5) source virtualenv_name/bin/activate
6) deactivate
   
**Creating Python virtualenv in Windows**
1) pip install virtualenv
2) python -m venv myenv
3) myenv\Scripts\activate
4) deactivate


** Docker to build and run **
$ docker pull mysql:8.2

$ docker images

$ docker run --name test-mysql -e MYSQL_ROOT_PASSWORD=strong_password -d mysql


$ docker exec -it container_name bash  // Check your docker website.

    ex : docker exec -it test-mysql bash

$ mysql -u root -p    // Type this command it will show downside text

Enter password: ...
mysql>


docker run -e MYSQL_ROOT_PASSWORD=your_password -p 3306:3306 mysql:8.0.36-1.el8

    example : docker run -e MYSQL_ROOT_PASSWORD=your_password -p 3306:3306 mysql:8.0





