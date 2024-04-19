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





 ##  interview questions ##
 1) How yolo works?
    
      a) The basic behind idea behind yolo is to divide the i/p image into a grid of cellsand , for each cell, predict the probabilities of the presence of object and bounding box coordinates of the object.
    
      Inputting an image: The image is resized to 448x448, then passed through a CNN to extract features
    
      Dividing the image into a grid: The grid size can be 13x13 or 19x19, with each cell containing 5 boxes
    
      Predicting bounding boxes and class probabilities: Each cell predicts a set of bounding boxes and class probabilities
    
      Removing overlapping guesses: YOLO uses non-maximum suppression to remove any guesses that overlap with other guesses
    
      Outputting the remaining guesses: YOLO outputs the remaining guesses as rectangles and object labels
    
2) Object detection vs segmentation
   
   a) Finding the object and location of the object.
   
   b) Fine-grained information
   
   Object detection:
     Focuses on identifying and localizing specific objects within an image or video. It involves finding bounding boxes around objects and classifying them.
   
   Segmentation:
     Focuses on dividing an image into meaningful regions and assigning class labels to each pixel. It provides fine-grained information about object boundaries and regions.

3) Different types of filters:
   
   a) Smoothing filters:
   
     Gaussian filter: This filter applies a two-dimensional Gaussian function to the neighborhood pixels to smoothen the image. The greater the standard deviation of the Gaussian distribution, the greater the blur will be.
   
     Median filter: This filter replaces each pixel value with the median of the neighboring pixels. It is effective in reducing the salt and pepper noise from the images.
   
   b) Sharpening filters
   
     Laplacian filter: This filter convolves over the image based on the principle of the Laplace transform. It calculates the image matrix's second-order derivative and highlights its edges and details by emphasizing regions of rapid intensity changes.
   
   c) Edge detection filters:
   
     Sobel filter: It detects the edges by calculating the horizontal and vertical derivatives of the image and then combining them.
   
     Robert filter: It detects the edges by calculating and combining derivatives of both the image diagonals.
   
   d) Thresholding filters:
   
      Binary threshold filter: This filter converts a greyscaled image into a binary image by setting pixel values above a threshold to white and values below the threshold to black.
   
      Adaptive threshold filter: It is similar to the binary threshold filter, but it determines its threshold based on the local neighborhood of each pixel.
      
   e) Morphological filters:
   
      Dilation filter: This filter expands the boundaries of regions in an image by replacing each pixel with a maximum value in its neighborhood. It helps fill gaps, join broken lines, and enlarge objects.
   
      Erosion filter: This filter shrinks the boundaries of regions by replacing each pixel with the minimum value with its neighborhood. It helps remove noise, separates connected objects, and reduces object size.

   f) The anisotropic diffusion filter (ADF) is a technique used in image processing and computer vision to reduce image noise while preserving image content.
  
   g) The Bilateral Filter is a non-linear, edge-preserving smoothing filter that is commonly used in Computer Vision as a simple noise-reduction stage in a pipeline.
  
   h) Morphological operations include dilation, erosion, opening, closing, and boundary extraction. For example, dilation can expand image pixels or add pixels on object boundaries, while erosion can shrink the image pixels or remove pixels on object boundaries. Compound operations often combine dilation and erosion, such as closing, which performs dilation and then erosion, or opening, which performs erosion and then dilation.
   
4) Different types of segmentation(Semantic vs instance segmentation):
   
   a) Semantic segmentation : One class consider as same entity.
   
   b) Instane segmentation : Distinguishes between different instances of the same class
   
   c) Semantic segmentation treats all objects within a category as one entity. Instance segmentation treats multiple objects in the same class as unique individual instances. 
      Semantic and instance segmentation have real-world applications such as: Urban planning and smart city management, Medical diagnostics and research, Autonomous vehicles and advanced driver-assistance systems (ADAS), Analyzing  medical scans, and Satellite or aerial imagery. 
     

5) How RT-DERT works?
   
    Efficient Hybrid Encoder: Baidu's RT-DETR uses an efficient hybrid encoder that processes multiscale features by decoupling intra-scale interaction and cross-scale fusion. This unique Vision Transformers-based design reduces computational costs and allows for real-time object detection.
  
    **Key Features**
      Efficient Hybrid Encoder: Baidu's RT-DETR uses an efficient hybrid encoder that processes multiscale features by decoupling intra-scale interaction and cross-scale fusion. This unique Vision Transformers-based design reduces computational costs and allows for real-time object detection.
      IoU-aware Query Selection: Baidu's RT-DETR improves object query initialization by utilizing IoU-aware query selection. This allows the model to focus on the most relevant objects in the scene, enhancing the detection accuracy.
      Adaptable Inference Speed: Baidu's RT-DETR supports flexible adjustments of inference speed by using different decoder layers without the need for retraining. This adaptability facilitates practical application in various real-time object detection scenarios.

6) Difference between low level and highlevel languages?
   
    High-level languages are easy to understand, debug, and are widely used today. They are portable and do not depend on machines. Low-level languages, on the other hand, are machine-friendly, difficult to understand, and not portable. They are machine-dependent and not commonly used for programming today.

7) Difference between pytorch and tensorflow:
   
     a) PyTorch and TensorFlow are two of the most popular deep learning frameworks. Both frameworks have their own strengths and weaknesses, and the best choice for you will depend on your specific needs.
   
     b) PyTorch is a Python-based deep learning framework that is known for its flexibility and ease of use. PyTorch uses a dynamic computation graph, which allows you to create and modify your models on the fly. This makes PyTorch a good choice for rapid prototyping and experimentation.
   
     c) TensorFlow is another Python-based deep learning framework that is known for its scalability and performance. TensorFlow uses a static computation graph, which means that you need to define your model before you can start training it. This can make TensorFlow less flexible than PyTorch, but it also makes TensorFlow more efficient for training large models.


8) What is CUDA and why it is used?
   
    Compute Unified Device Architecture (CUDA) is a parallel computing platform and application programming interface (API) that allows software to use certain types of graphics processing units (GPUs) for accelerated general-purpose processing, an approach called general-purpose computing on GPUs (GPGPU).
     
   
9) CUDA using pytorch:
    
    a) Check if CUDA is available:
   
       import torch
       print(torch.cuda.is_available())
   
    b) Check the CUDA device count:
   
       print(torch.cuda.device_count())

    c) Check the CUDA device properties:

       for i in range(torch.cuda.device_count()):

         print(torch.cuda.get_device_properties(i))

    d) Check the current CUDA device:

       print(torch.cuda.current_device())


10) CUDA using tensorflow:
    
      a) Check if CUDA is available:

          import tensorflow as tf
    
          print(tf.test.is_built_with_cuda())
    
      b) Check the CUDA device count:

          print(len(tf.config.experimental.list_physical_devices('GPU')))


      c) Check the CUDA device properties:

          gpus = tf.config.experimental.list_physical_devices('GPU')
          for gpu in gpus:
              print("Name:", gpu.name, "  Type:", gpu.device_type)

      d) Check the current CUDA device:

          print(tf.config.experimental.get_visible_devices('GPU'))


11) What is a tensor?
    
      A tensor is a mathematical object representing a multi-dimensional array of numerical values. In the context of machine learning frameworks like TensorFlow and PyTorch, tensors are the fundamental data structures used for computation.

    a) Dimensionality:
    
    b) Data Types:

    c) Operations:

    d) Memory Layout:

    e) Gradient Computation:

12) Difference between Tensor and Numpy:

    Tensors and NumPy arrays are both used to represent multi-dimensional arrays of numerical data, but they have some differences, especially in the context of machine learning frameworks like TensorFlow and PyTorch.

    a) Integration with Deep Learning Frameworks:

    b) Computation on Accelerators:

    c) Automatic Differentiation:

    d) Memory Sharing:

13) What is REST API?
    
      REST API stands for Representational State Transfer Application Programming Interface. It is an architectural style for designing networked applications. RESTful APIs are designed to be simple, lightweight, and scalable, making them popular for building web services and APIs.

      a) Statelessness:

      b) Resources and URIs:

      c) HTTP Methods:

      d) Representation:

      e) Uniform Interface:

      f) State Transfer:

      RESTful APIs are widely used in web development for building web services, mobile applications, and IoT (Internet of Things) devices. They provide a flexible and scalable way to expose functionality over the web, allowing different clients to interact with server-side resources using standard protocols and formats.


13) Tensor CPU to GPU using pythorch and tensorflow:

    Pytorch :
    
      import torch

      ##Create a tensor on CPU 
      tensor_cpu = torch.tensor([1, 2, 3])
      
      #Transfer tensor from CPU to GPU
      tensor_gpu = tensor_cpu.to('cuda')  # or tensor_cpu.cuda()
      
      #Transfer tensor from GPU to CPU
      tensor_cpu_again = tensor_gpu.to('cpu')  # or tensor_gpu.cpu()

    TensorFlow:
    
      Model1:
    
        import tensorflow as tf
    
        #Create a tensor on CPU
        tensor_cpu = tf.convert_to_tensor([1, 2, 3])
        
        #Transfer tensor from CPU to GPU
        with tf.device('/gpu:0'):  # Change '0' to the GPU device index you want to use
            tensor_gpu = tf.identity(tensor_cpu)  # or tf.identity(tensor_cpu).gpu()
        
        #Transfer tensor from GPU to CPU
        tensor_cpu_again = tf.identity(tensor_gpu)  # or tf.identity(tensor_gpu).cpu()
  
      Model2:
  
        import tensorflow as tf
  
        #Create a tensor on CPU
        tensor_cpu = tf.constant([1, 2, 3])
        
        #Transfer tensor from CPU to GPU
        tensor_gpu = tf.convert_to_tensor(tensor_cpu)
        with tf.device('/gpu:0'):  # Change '0' to the GPU device index you want to use
            tensor_gpu = tf.identity(tensor_gpu)
        
        #Transfer tensor from GPU to CPU
        tensor_cpu_again = tensor_gpu.numpy()

  
      
    
    
