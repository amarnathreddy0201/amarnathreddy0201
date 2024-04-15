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


# Docker for running the docker fastapi
  docker run --name nervous_kowalevski -d fastapi-app-simple:latest 



### Build the Docker image: Once you have your Dockerfile and application files ready, navigate to the directory containing these files and run the following command to build the Docker image:

1) docker build -t my-image .
   
Replace my-image with the desired name for your image.

Run a Docker container: After successfully building the Docker image, you can run a container using the following command:

2) docker run -d --name my-container -p 8080:80 my-image


### Docker commands ########
1) stop the docker : sudo docker stop count-web-application-container
2) remove the docker : sudo docker rm count-web-application-container
3)  For clear : docker system prune -a


#### for pushing to docker hub #########
4) For checking log files : docker exec container_id_or_name cat /path/to/log/file

5) docker tag count-web-application(name of the image) docker/web-app

6) docker push dockerhub/web-app

7) docker images

8) sudo docker rmi 5323383c00e8(pid of image)


###  python 3.11 in ec2 instance commands ##
MEmory checking : df -h

1) sudo apt update
2) sudo apt install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python3-openssl git
3) wget https://www.python.org/ftp/python/3.11.0/Python-3.11.0.tgz
4) tar -xf Python-3.11.0.tgz
5) cd Python-3.11.0
6) ./configure --enable-optimizations
7) make -j 8  # Adjust the number according to the number of CPU cores
8) sudo make altinstall
   
6) python3.11 -m venv myenv
7) source myenv/bin/activate


########################## For ip address finding #######
1) lsof -i :8000
2) lsof -i -P -n | grep LISTEN


#### For docker installation in ec2 ###################
1) sudo apt update
2)  sudo apt install -y apt-transport-https ca-certificates curl software-properties-common

3) curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
4) sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
5) sudo apt update
6) sudo apt install -y docker-ce docker-ce-cli containerd.io
7) sudo systemctl start docker
8) sudo systemctl enable docker
9) docker --version



 


