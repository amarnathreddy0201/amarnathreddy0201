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
1) py -3.11 -m venv pyenv_3.11
2) Ex :-  py python_version -m venv your_venv_name.

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


This is forlearning.
###################  AWS ##############################
1) Check the table exist or not : https://stackoverflow.com/questions/42485616/how-to-check-if-dynamodb-table-exists#:~:text=You%20can%20use%20the%20ListTables,you%20request%20doesn't%20exist. 

