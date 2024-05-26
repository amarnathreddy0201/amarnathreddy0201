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


## Docker to build and run
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
  4)  For checking logs : docker logs count-web-application-container


#### for pushing to docker hub #########
  1) For checking log files : docker exec container_id_or_name cat /path/to/log/file
  
  2) docker tag count-web-application(name of the image) dockerhub/name
  
  3) docker push dockerhub/name
  
  4) docker images
  
  5) sudo docker rmi 5323383c00e8(pid of image)
  
  6) For docker logs : sudo docker logs container-name
  
  **Note : name is application name.**

#### Pull the docker image:

	1) sudo docker pull dockerhub/name:latest
	2) sudo docker run -d --name container-name -e AWS_ACCESS_KEY_ID=access_key_id -e AWS_SECRET_ACCESS_KEY=access_key -e AWS_DEFAULT_REGION=ap-south-1 -p 8001:8001 dockerhub/name
 ## Docker commands for removing container and image
 	For ec2 instance removing and new container:
	stop the container : sudo docker stop count-web-application-container
	remove the docker : sudo docker rm count-web-application-container
	Check the id of image : sudo docker images
	remove the image : sudo docker rmi 0d051dca991e(id of the image)


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

## Simple docker 

  ```
      #Use the official Python image
      FROM python:3.11.5
      
      # Install necessary system dependencies including libgl1-mesa-glx
      RUN apt-get update && apt-get install -y libgl1-mesa-glx
      
      # Set the working directory in the container
      WORKDIR /app
      
      # Copy the dependencies file to the working directory
      COPY requirements.txt .
      
      # Install REQUIREMENTS
      RUN pip install --upgrade pip && \
	    pip install -r requirements.txt && \
	    pip uninstall -y fastapi && \
	    pip install fastapi==0.97.0 && \
	    pip uninstall -y fastapi-users && \
	    pip install fastapi-users==12.1.2 && \
	    pip uninstall -y fastapi-users-db-beanie && \
	    pip install fastapi-users-db-beanie==3.0.0 && \
	    pip uninstall -y fastapi-users-db-mongodb && \
	    pip install fastapi-users-db-mongodb==1.1.0 && \
	    pip uninstall -y jwt PyJWT && \
	    pip install PyJWT && \
	    pip uninstall -y motor &&\
	    pip install motor==3.4.0
          
      
      # Copy the content of the local src directory to the working directory
      COPY . /app
      
      # Command to run the FastAPI application with Uvicorn
      CMD ["uvicorn","api1:app","--host","0.0.0.0","--port","8001"]
  ```


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



# https://bastibe.de/2013-05-30-speeding-up-matplotlib.html

 ##  interview questions ##
	 class Amar:
	    amar ="amar"
	    
	    def __init__(self,a,b):
	        self.a = a
	        self.b = b
	    
	    @staticmethod
	    def Amar_call():
	        return amar
	    
	    @classmethod
	    def Amar_call1(cls):
	        return cls.amar
	
	
	amar = Amar(1,2)
	print(amar.amar)
	print(amar.a)
	
	# classs level
	print(amar.Amar_call1())
	print(Amar.Amar_call1())
	
	# Static level
	print(amar.Amar_call().amar) # it's returning Amar_class as a object
	print(Amar.Amar_call().amar) # it's returning Amar_class as a object


 **1) How yolo works?**
    
      a) The basic behind idea behind yolo is to divide the i/p image into a grid of cellsand , for each cell, predict the probabilities of the presence of object and bounding box coordinates of the object.
    
      Inputting an image: The image is resized to 448x448, then passed through a CNN to extract features
    
      Dividing the image into a grid: The grid size can be 13x13 or 19x19, with each cell containing 5 boxes
    
      Predicting bounding boxes and class probabilities: Each cell predicts a set of bounding boxes and class probabilities
    
      Removing overlapping guesses: YOLO uses non-maximum suppression to remove any guesses that overlap with other guesses
    
      Outputting the remaining guesses: YOLO outputs the remaining guesses as rectangles and object labels
    
**2) Object detection vs segmentation**
   
   a) Finding the object and location of the object.
   
   b) Fine-grained information
   
   Object detection:
     Focuses on identifying and localizing specific objects within an image or video. It involves finding bounding boxes around objects and classifying them.
   
   Segmentation:
     Focuses on dividing an image into meaningful regions and assigning class labels to each pixel. It provides fine-grained information about object boundaries and regions.

**3) Different types of filters:**
   
   a) Smoothing filters:
   
     Gaussian filter: This filter applies a two-dimensional Gaussian function to the neighborhood pixels to smoothen the image. The greater the standard deviation of the Gaussian distribution, the greater the blur will be.
   
     Median filter: This filter replaces each pixel value with the median of the neighboring pixels. It is effective in reducing the salt and pepper noise from the images.
   
   b) Sharpening filters
   
     Laplacian filter: This filter convolves over the image based on the principle of the Laplace transform. It calculates the image matrix's second-order derivative and highlights its edges and details by emphasizing regions of rapid intensity changes.
   
   c) Edge detection filters:
   
	1) Sobel filter: It detects the edges by calculating the horizontal and vertical derivatives of the image and then combining them.
	
	     	Sobel function in opencv is used to perform edge detection on an image. it computes the gradient of the image intensity at each pixel, which can be used to detect edges or sharp changes in intensity. Sobel edge detection typically involves convolving the image with a Sobel kernel in the both the horizontal and vertical directions to compute the gradient magnitude and direction.
   
     	2) Robert filter: It detects the edges by calculating and combining derivatives of both the image diagonals.
   
   d) Thresholding filters:
   
      Binary threshold filter: This filter converts a greyscaled image into a binary image by setting pixel values above a threshold to white and values below the threshold to black.
   
      Adaptive threshold filter: It is similar to the binary threshold filter, but it determines its threshold based on the local neighborhood of each pixel.
      
   e) Morphological filters:
   
      Dilation filter: This filter expands the boundaries of regions in an image by replacing each pixel with a maximum value in its neighborhood. It helps fill gaps, join broken lines, and enlarge objects.
   
      Erosion filter: This filter shrinks the boundaries of regions by replacing each pixel with the minimum value with its neighborhood. It helps remove noise, separates connected objects, and reduces object size.

   f) The anisotropic diffusion filter (ADF) is a technique used in image processing and computer vision to reduce image noise while preserving image content.
  
   g) The Bilateral Filter is a non-linear, edge-preserving smoothing filter that is commonly used in Computer Vision as a simple noise-reduction stage in a pipeline.
  
   h) Morphological operations include dilation, erosion, opening, closing, and boundary extraction. For example, dilation can expand image pixels or add pixels on object boundaries, while erosion can shrink the image pixels or remove pixels on object boundaries. Compound operations often combine dilation and erosion, such as closing, which performs dilation and then erosion, or opening, which performs erosion and then dilation.
   
**4) Different types of segmentation(Semantic vs instance segmentation):**
   
   a) Semantic segmentation : One class consider as same entity.
   
   b) Instane segmentation : Distinguishes between different instances of the same class
   
   c) Semantic segmentation treats all objects within a category as one entity. Instance segmentation treats multiple objects in the same class as unique individual instances. 
      Semantic and instance segmentation have real-world applications such as: Urban planning and smart city management, Medical diagnostics and research, Autonomous vehicles and advanced driver-assistance systems (ADAS), Analyzing  medical scans, and Satellite or aerial imagery. 
     

**5) How RT-DERT works?**
   
    Efficient Hybrid Encoder: Baidu's RT-DETR uses an efficient hybrid encoder that processes multiscale features by decoupling intra-scale interaction and cross-scale fusion. This unique Vision Transformers-based design reduces computational costs and allows for real-time object detection.
  
    **Key Features**
      Efficient Hybrid Encoder: Baidu's RT-DETR uses an efficient hybrid encoder that processes multiscale features by decoupling intra-scale interaction and cross-scale fusion. This unique Vision Transformers-based design reduces computational costs and allows for real-time object detection.
      IoU-aware Query Selection: Baidu's RT-DETR improves object query initialization by utilizing IoU-aware query selection. This allows the model to focus on the most relevant objects in the scene, enhancing the detection accuracy.
      Adaptable Inference Speed: Baidu's RT-DETR supports flexible adjustments of inference speed by using different decoder layers without the need for retraining. This adaptability facilitates practical application in various real-time object detection scenarios.

6) Difference between low level and highlevel languages?
   
    High-level languages are easy to understand, debug, and are widely used today. They are portable and do not depend on machines. Low-level languages, on the other hand, are machine-friendly, difficult to understand, and not portable. They are machine-dependent and not commonly used for programming today.

**7) Difference between pytorch and tensorflow:**
   
     a) PyTorch and TensorFlow are two of the most popular deep learning frameworks. Both frameworks have their own strengths and weaknesses, and the best choice for you will depend on your specific needs.
   
     b) PyTorch is a Python-based deep learning framework that is known for its flexibility and ease of use. PyTorch uses a dynamic computation graph, which allows you to create and modify your models on the fly. This makes PyTorch a good choice for rapid prototyping and experimentation.
   
     c) TensorFlow is another Python-based deep learning framework that is known for its scalability and performance. TensorFlow uses a static computation graph, which means that you need to define your model before you can start training it. This can make TensorFlow less flexible than PyTorch, but it also makes TensorFlow more efficient for training large models.


**8) What is CUDA and why it is used?**
   
    Compute Unified Device Architecture (CUDA) is a parallel computing platform and application programming interface (API) that allows software to use certain types of graphics processing units (GPUs) for accelerated general-purpose processing, an approach called general-purpose computing on GPUs (GPGPU).
     
   
**9) CUDA using pytorch:**
    
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


**10) CUDA using tensorflow:**
    
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


**11) What is a tensor?**
    
      A tensor is a mathematical object representing a multi-dimensional array of numerical values. In the context of machine learning frameworks like TensorFlow and PyTorch, tensors are the fundamental data structures used for computation.

    a) Dimensionality:
    
    b) Data Types:

    c) Operations:

    d) Memory Layout:

    e) Gradient Computation:

**12) Difference between Tensor and Numpy:**

    Tensors and NumPy arrays are both used to represent multi-dimensional arrays of numerical data, but they have some differences, especially in the context of machine learning frameworks like TensorFlow and PyTorch.

    a) Integration with Deep Learning Frameworks:

    b) Computation on Accelerators:

    c) Automatic Differentiation:

    d) Memory Sharing:

**13) What is REST API?**
    
      REST API stands for Representational State Transfer Application Programming Interface. It is an architectural style for designing networked applications. RESTful APIs are designed to be simple, lightweight, and scalable, making them popular for building web services and APIs.

      a) Statelessness:

      b) Resources and URIs:

      c) HTTP Methods:

      d) Representation:

      e) Uniform Interface:

      f) State Transfer:

      RESTful APIs are widely used in web development for building web services, mobile applications, and IoT (Internet of Things) devices. They provide a flexible and scalable way to expose functionality over the web, allowing different clients to interact with server-side resources using standard protocols and formats.


**14) Tensor CPU to GPU using pythorch and tensorflow:**

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


- Command for docker in ec2

      echo "Running a new container from the latest image..."
      # Run a new container from the latest image with a specific name
      docker run -d --name fastapi-app-simple-container -e AWS_ACCESS_KEY_ID= tour_access_key_id -e AWS_SECRET_ACCESS_KEY=your_access_key -e AWS_DEFAULT_REGION=ap-south-1 -p 8000:8000 amarnathreddysurapureddy0201/fastapi-app-simple:latest

      1) amarnathreddysurapureddy0201 is user name
      2) fastapi-app-simple:latest is image
      3) Container : fastapi-app-simple-container
  
**15) what is the use of activation function in neural network?**

    a) Activation functions, also known as transfer functions, are used in neural networks to calculate the weighted sum of inputs and biases, which then determines if a neuron can be activated. They also manipulate the presented data and produce an output for the neural network that contains the parameters in the data. Activation functions can be linear or nonlinear, and are used to control the output of neural networks across different domains.
    
    b) Activation functions introduce non-linearities to neural networks, enabling them to learn complex patterns and make non-linear predictions. For example, the sigmoid function is commonly used in artificial neural networks, particularly in feedforward neural networks, because it allows the network to introduce non-linearity into the model, which allows the neural network to learn more complex decision boundaries.

    c) Here are some examples of activation functions:
    
        1) ReLU:
    
            The most used activation function in the world, used in almost all the convolutional neural networks or deep learning.
    
        2) Leaky ReLU:
    
            An improved version of the ReLU function, where the gradient is 0 for x<0, which would deactivate the neurons in that region.
    
        3) tanh:
    
            Also called the hyperbolic tangent activation function, this mathematical function commonly used in artificial neural networks for their hidden layers. It transforms input values to produce output values between -1 and 1.
    
        4) Linear:
    
            Also known as "no activation," or "identity function" (multiplied x1.0), this function doesn't do anything to the weighted sum of the input, it simply spits out the value it was given.
    
**16) how do you handle missing or corrupted data in a dataset?**
    
    a) Method 1 is deleting rows or columns.
    
        We usually use this method when it comes to empty cells.
        For example, if the majority of our data is missing for a column or for a row, we can simply delete them.
    
    b) Method 2 is replacing the missing data with aggregated values.
    
        In this case, we can calculate the aggregated value based on the rest of the values we have in the column and put the received number to the empty spot.
    
    c) Method 3 is creating an unknown category.
    
        Categorical features have a number of possible values, which gives us an opportunity to create one more category for the missing values. This way we will lower the variance by adding new information to the data. This could be used when the original information is missing or cannot be understood,
    
    d) Method 4 is predicting missing values.
    
        where we have no missing values, we can train a statistical or machine learning algorithm in order to predict the missing values. Since among the samples for which this training is performed, there are missing values, it is necessary to replace them initially using one of the simplest methods for recovering gaps. This way will give us better performance, unless, of course, a missing value should have a high variance. As always, an example. With Madan here, we don’t have any number for the experience column. If we have a bigger table, with more people with similar information — the same country, profession, and education — it is possible to calculate correctly the most possible result for the missing feature. In this case, even if we didn’t guess absolutely right.

**17) What is Random seed?**
    
    Random seed is used to ensure that results are reproducible. This is important in data science and other fields. For example, in Python, random seed is used to generate a pseudo-random encryption key, which is an important part of computer security. Random seed also makes optimization of codes easy where random numbers are used for testing.

    ```
      import random
  
      random.seed(10)
      print(random.random())
      
      random.seed(10)
      print(random.random())


**18) Why YOLO ?**

    Model for real time detection.

    Yolov1 : problem with Small objects.

    Yolov2 : Bounding boxes + Multi class

    Yolov3 : Pyramid n/w's

        Different scales and resolutions

    Yolov4 : Accuracy and speed

        CSPDarknet53 as the backbone network, Mish activation function, and improved data augmentation.

    Yolov5 :

    Yolov8 :

        Along with its versatility, YOLOv8 boasts several other innovations that make it a strong candidate for a wide range of object detection and image segmentation tasks. These include a new backbone network, anchor-free detection head, and loss function. Additionally, YOLOv8 is highly efficient and can run on a variety of hardware, from CPUs to GPUs.

    Yolov9:

        This model is superior to RT-DETR and YOLO-MS in terms of accuracy and efficiency, setting new standards in lightweight model performance.


**19) What is Convolutional Neural Network?**

    CNN stands for Convolutional Neural Network, which is a class of deep neural networks commonly used in tasks involving visual imagery analysis, such as image classification, object detection, and image segmentation.

    Here's a breakdown of CNNs and their components:

      1) Convolutional Layers : These are the fundamental building blocks of CNNs. Convolutional layers apply convolution operations to the input data using filters (also called kernels) to extract features. The filters slide over the input data, computing dot products at each position, which helps capture **spatial patterns and local dependencies in the data**.
   
      2) Pooling Layers: Pooling layers are typically inserted between convolutional layers to **reduce the spatial dimensions of the feature maps** while retaining the most important information. Common **pooling operations include max pooling and average pooling, which downsample the input by taking the maximum or average** value within each pooling region.
   
      3) Activation Functions: **Activation functions introduce non-linearity into the network**, allowing **CNNs to learn complex patterns and relationships in the data**. Popular activation functions used in CNNs include ReLU (Rectified Linear Unit), sigmoid, and tanh.
   
      4) Fully Connected Layers: Fully connected layers, also known as dense layers, are typically found at the end of a CNN architecture. These layers connect every neuron in one layer to every neuron in the next layer, allowing the network to learn high-level features and make predictions based on the extracted features.
   
      5) Flattening: Before passing the output of convolutional and pooling layers to fully connected layers, the feature maps are flattened into a one-dimensional vector. This flattening operation reshapes the data into a format suitable for input to the fully connected layers.
   
    **CNNs** are trained using **backpropagation and gradient descent algorithms**, where the network learns to minimize a loss function by adjusting its weights and biases during the training process. They are particularly effective in handling high-dimensional data like images due to their ability to automatically learn hierarchical representations of features directly from the raw data.


**20) What is the purpose of GridSearcCV**

    	GridSearchCV is a technique for finding the optimal parameter values from a given set of parameters in a grid. It's essentially a cross-validation technique. The model as well as the parameters must be entered. After extracting the best parameter values, predictions are made

    	```
	    params = dict()
     
	    params["C"] = (1e-6,1,10,100.0 )
     
	    params["gamma"] = (1e-6,1,10,100.0)
     
	    params["degree"] = (1,2,3)
     
	    params["kernel"] = ['linear','poly', 'rbf', 'sigmoid']
     
**21) How to change tensor variable**
	Now let's try to change one of the elements of the changable tensor.
	
	# Will error (requires the .assign() method)
	changeable_tensor[0] = 7
	changeable_tensor
	---------------------------------------------------------------------------
	TypeError                                 Traceback (most recent call last)
	<ipython-input-14-daecfbad2415> in <cell line: 2>()
	      1 # Will error (requires the .assign() method)
	----> 2 changeable_tensor[0] = 7
	      3 changeable_tensor
	
	TypeError: 'ResourceVariable' object does not support item assignment
	To change an element of a tf.Variable() tensor requires the assign() method.
	
	# Won't error
	changeable_tensor[0].assign(7)
	changeable_tensor
 
**22) Difference Between set, multiset, unordered_set, unordered_multiset in C++**
    
	1. Set: Sets are associative containers that store unique elements following a specific order. Following are the properties of sets:

		Stores the values in sorted order. 
		Stores only unique values. 
		Elements can only be inserted or deleted but cannot be modified. 
		We can erase more than 1 element by giving the start iterator and end iterator position. 
		Traversal using iterators. 
		Sets are implemented as Binary Search Tree.

	3. Multisets: Multisets are associative containers that store multiple elements having equivalent values following a specific order. Following are the properties of multisets:

		Stores elements in sorted order.

		It allows the storage of multiple elements.

		We can erase more than 1 element by giving the start iterator and end iterator.

	3. unordered_set: unordered_set are associative containers that store unique elements in no particular order. Following are the properties of Unordered_sets: 

		Elements can be stored in any order. ( no sorted order )

		Stores only unique values.

		Hash-table used to store elements.

		We can erase only the element for which the iterator position is given.

	4. Unordered_multiset: Unordered_multiset is an associative container that contains a set of non-unique elements in unsorted order. Following are the properties of Unordered_multiset: 

		Elements can be stored in any order.

		Duplicate elements can be stored.

		Hash-table used to store elements.

		We can erase only the element for which the iterator position is given.

**23) Map vs multimap:**
	
 	Map stores unique key-value pairs in a sorted manner. Each key is uniquely associated with a value that may or may not be unique. A key can be inserted or deleted from a map but cannot be modified. Values assigned to keys can be changed. It is a great way for quickly accessing value using the key and it is done in O(1) time.

	Multimap is similar to map with an addition that multiple elements can have same keys. Also, it is NOT required that the key value and mapped value pair has to be unique in this case. One important thing to note about multimap is that multimap keeps all the keys in sorted order always. These properties of multimap makes it very much useful in competitive programming.


**24) Backward Pass (Backpropagation):**
	
 	Backpropagation is the process of computing the gradient of the loss function with respect to each weight in the network, layer by layer, starting from the output layer and moving backward to the input layer. This gradient represents the **direction and magnitude of change that each weight should undergo to minimize the loss function.**


**25) Substring present:**

    	def how_may_substrings(main,sub):
	    number =0 
	    if len(main) > len(sub):
	        main,sub=main,sub
	    else:
	        main,sub = sub,main
	    main_len =len(main)
	    sub_len = len(sub)
	    print(main_len,sub_len)
	    for i in range(0,main_len-sub_len+1):
	        print(main[i:i+sub_len])
	        if (main[i:i+sub_len]==sub):
	            number+=1
	    return number
	
	print(how_may_substrings("abababa","aaaba"))

**26) Greedy search vs Beam search:**

		Greedy search and beam search are both search algorithms used in machine learning and natural language processing (NLP) tasks. They differ in how they make decisions during the search process:

		Greedy search Selects the single most likely option. It's simple and fast, but it only considers each position in isolation.

		Beam search Maintains a beam of multiple candidates at each step, ranked based on their probabilities. It's more complex and computationally expensive than greedy search, but it's more accurate because it considers future steps when selecting the next word.


**27) Super Resolution in OpenCV:**

	https://learnopencv.com/super-resolution-in-opencv/

 	Super-resolution refers to the process of upscaling or improving the details of the image. Follow this blog to learn the options for Super Resolution in OpenCV. When increasing the dimensions of an image, the extra pixels need to be interpolated somehow. Basic image processing techniques do not give good results as they do not take the surroundings in context while scaling up. Deep learning and, more recently, GANs come to the rescue here and provide much better results.

 	1) Resnet architecture

  	2) Residual Blocks are skip-connection blocks that learn residual functions with reference to the layer inputs, instead of learning unreferenced functions. They were introduced as part of the ResNet architecture.

   	3) Different techniques:
    		a) EDSR : Enhanced deep resdiual network. it is slower than FSRCNN.
      		b) FSRCNN : 
		c) LapSRN : Same results as FSRCNN.
  		d) ESPCN : Same speed as FSRCNN , giving less count than fsrcnn.

**28) Anagrom:**

	def anagrom(first,second):
	    true_or_false = True
	    if first!=second:
	        true_or_false= False
	    return true_or_false
	        
	print(anagrom(["a",2,"df"],["a",2,"df"]))

**29) A (typical) architecture of a convolutional neural network**


	1) A convolutional layer is the main building block of a CNN. It contains a set of filters (or kernels), parameters of which are to be learned throughout the training. The size of the filters is usually smaller than the actual image. Each filter convolves with the image and creates an activation map.

	2) A hidden layer in a neural network is a layer of neurons that is neither the input nor output layer. The term "hidden" refers to the fact that these layers are not directly observable and are responsible for the depth of neural networks, allowing them to process complex data representations.

	3) The purpose of the pooling layers is to reduce the dimensions of the hidden layer by combining the outputs of neuron clusters at the previous layer into a single neuron in the next layer



The "2D" means our inputs are two dimensional (height and width), even though they have 3 colour channels, the convolutions are run on each channel invididually.
filters - these are the number of "feature extractors" that will be moving over our images.
kernel_size - the size of our filters, for example, a kernel_size of (3, 3) (or just 3) will mean each filter will have the size 3x3, meaning it will look at a space of 3x3 pixels each time. The smaller the kernel, the more fine-grained features it will extract.
stride - the number of pixels a filter will move across as it covers the image. A stride of 1 means the filter moves across each pixel 1 by 1. A stride of 2 means it moves 2 pixels at a time.
padding - this can be either 'same' or 'valid', 'same' adds zeros the to outside of the image so the resulting output of the convolutional layer is the same as the input, where as 'valid' (default) cuts off excess pixels where the filter doesn't fit (e.g. 224 pixels wide divided by a kernel size of 3 (224/3 = 74.6) means a single pixel will get cut off the end.

stride = ((n-f)/s)+1

 	n1 X n2 =>  (((n1-f)/s)+1) * (((n2-f)/s)+1)
	n - input image size
 	f - filter size
  	s - stride size

    example : 6 X 7 image size , filter(f=2) and stride is 3

    	(((6-2)/3)+1) * (((7-2)/3)+1)

stride + padding : f=2 and stride =3

 	n1 X n2 =>  (((n1-f+2p)/s)+1) * (((n2-f+2p)/s)+1)
  	
   	(((n1-2+2p)/3)+1) * (((n2-2+2p)/3)+1)

	
The Adam optimizer, short for “Adaptive Moment Estimation,” is an iterative optimization algorithm used to minimize the loss function during the training of neural networks. Adam can be looked at as a combination of RMSprop and Stochastic Gradient Descent with momentum



**30) Fibonic**

	k=4
	end =7

	second_final=[]
	
	index = 0
	for i in range(end):
	    if i > k-1:
	        sum= 0
	
	        for t in second_final[index : len(second_final)]:
	            print("fatat : ",index)
	            sum+=t
	        index+=1
	
	        second_final.append(sum)
	
	    else:
	        second_final.append(1)




 
**31 Booble sort**

	data =[33,2,33,1,2,45,2,4,-1,4,23]

	data =[1,2,3,4,4]
	
	for i in range(len(data)-1):
	    tr_fal = False
	    
	    for j in range(len(data)-1-i):
	        
	        if data[j]>data[j+1]:
	            tr_fal = True
	            
	            data[j],data[j+1] = data[j+1],data[j]
	    
	    if tr_fal == False:
	        print(tr_fal)
	        break
	    
	    
	print(data)


**32 Selection sort**

	for i in range(len(data)-1):
    
	    tr_fal = False
	    for j in range(i+1,len(data)):
	        
	        if data[i]>data[j]:
	            tr_fal = True
	            
	            data[i],data[j] = data[j],data[i]
	        
	    
	    if tr_fal == False:
	        print(tr_fal)
	        break
	
	print(data)

**33) insertion sort**

	data =[10,15,9,-1,0]
	for i in range(1,len(data)):
	    
	    j = i-1
	    mid = data[i]
	    
	    while j>=0 and  data[j]  > mid:
	        
	        data[j+1] = data[j]
	        j-=1
	    
	    data[j+1] = mid
	    
	
	print(data)

	
**34) Class and object:**

	class Dog:
	    # Class variable to count the number of dogs
	    number_of_dogs = 0
	    
	    def __init__(self, name, age):
	        self.name = name
	        self.age = age
	        Dog.number_of_dogs += 1
	
	    def description(self):
	        return f"{self.name} is {self.age} years old"
	    
	    # @classmethod
	    # def get_number_of_dogs(cls):
	    def get_number_of_dogs(self):
	        # return cls.number_of_dogs
	        return self.number_of_dogs

	# Create instances
	dog1 = Dog("Buddy", 3)
	dog2 = Dog("Bella", 5)
	
	dog2 = Dog("Bella", 5)
	
	data = dog2
	
	# Access class variable
	print(data.get_number_of_dogs())  # Output: 2
