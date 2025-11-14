# Pytorch functions 

### 1) Tensor Creation
```
import torch

// From Python list

x = torch.tensor([1, 2, 3])
print(x)  // tensor([1, 2, 3])

// Uninitialized tensor (random values in memory)

x = torch.empty(2, 3)
print(x.shape)  // torch.Size([2, 3])

// Zeros

x = torch.zeros(2, 3)
print(x)  // tensor([[0., 0., 0.],
          //         [0., 0., 0.]])

// Ones

x = torch.ones(2, 3)
print(x)  // tensor([[1., 1., 1.],
          //         [1., 1., 1.]])

// Range

x = torch.arange(0, 10, 2)
print(x)  // tensor([0, 2, 4, 6, 8])

// Linspace

x = torch.linspace(0, 1, steps=5)
print(x)  // tensor([0.0000, 0.2500, 0.5000, 0.7500, 1.0000])

// Identity matrix

x = torch.eye(3)
print(x)
// tensor([[1., 0., 0.],
//         [0., 1., 0.],
//         [0., 0., 1.]])

// Random

x = torch.rand(2, 2)    # Uniform [0,1)
x = torch.randn(2, 2)   # Normal distribution (mean=0, std=1)
```
### 2. Tensor operations
```
x = torch.tensor([[1, 2, 3],
                  [4, 5, 6]])

// Reshape

y = x.reshape(3, 2)
print(y)
// tensor([[1, 2],
//         [3, 4],
//         [5, 6]])

// View (like reshape, but may share memory)

y = x.view(3, 2)

// Squeeze (remove dim=1)

x = torch.tensor([[1], [2], [3]])
print(x.shape)        

// torch.Size([3, 1])

y = x.squeeze()
print(y.shape)        
// torch.Size([3])

// Unsqueeze (add dimension)

y = x.unsqueeze(0)
print(y.shape)         
// torch.Size([1, 3, 1])

// Flatten

x = torch.tensor([[1, 2], [3, 4]])
y = x.flatten()
print(y)              
// tensor([1, 2, 3, 4])

// Concatenate

a = torch.tensor([1, 2])
b = torch.tensor([3, 4])
c = torch.cat([a, b])
print(c)              // tensor([1, 2, 3, 4])

// Stack (adds new dimension)

d = torch.stack([a, b])
print(d)              // tensor([[1, 2],
                     //         [3, 4]])
```

### 3) Mathematical Operations 
```
a = torch.tensor([1., 2., 3.])
b = torch.tensor([4., 5., 6.])

// Element-wise

print(torch.add(a, b))  

// tensor([5., 7., 9.])

print(torch.mul(a, b))  

// tensor([ 4., 10., 18.])

// Reduction

x = torch.tensor([[1., 2.], [3., 4.]])
print(x.sum())   // tensor(10.)
print(x.mean())  // tensor(2.5)
print(x.max())   // tensor(4.)
print(x.argmax())// tensor(3) (flattened index)

// Linear Algebra

A = torch.tensor([[1., 2.], [3., 4.]])

B = torch.tensor([[5., 6.], [7., 8.]])

print(torch.matmul(A, B))

// tensor([[19., 22.],
//         [43., 50.]])
```

### 4) Device management/Gpu
```
x = torch.tensor([1, 2, 3])

// Check GPU

print(torch.cuda.is_available())

// Move tensor to GPU

if torch.cuda.is_available():
    x = x.to("cuda")
    print(x.device)   # cuda:0
```

### 5) Autograd
```
x = torch.tensor([2.0], requires_grad=True)
y = x**2 + 3*x
y.backward()        // dy/dx = 2x + 3
print(x.grad)       // tensor([7.])

// No gradient tracking
with torch.no_grad():
    z = x * 2
print(z.requires_grad)  // False
```


### 6) Neural network
```
import torch.nn as nn

// Linear layer

layer = nn.Linear(4, 2)
x = torch.rand(1, 4)
print(layer(x))   # Output shape: (1, 2)

// Activation

act = nn.ReLU()
print(act(torch.tensor([-1., 0., 2.])))  # tensor([0., 0., 2.])

// Loss

loss_fn = nn.MSELoss()
y_pred = torch.tensor([0.5, 0.7])
y_true = torch.tensor([1.0, 0.0])
print(loss_fn(y_pred, y_true))  # tensor(0.3700)
```

### 7) Optimization 
```
model = nn.Linear(2, 1)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

// Dummy data

x = torch.tensor([[1., 2.]])
y = torch.tensor([[1.]])

// Training step

pred = model(x)
loss = nn.MSELoss()(pred, y)
optimizer.zero_grad()
loss.backward()
optimizer.step()
```

### 8) Data loading 
```
from torch.utils.data import Dataset, DataLoader, TensorDataset

// Custom Dataset

class MyDataset(Dataset):
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels
    def __len__(self):
        return len(self.data)
    def __getitem__(self, idx):
        return self.data[idx], self.labels[idx]

data = torch.tensor([[1], [2], [3]])
labels = torch.tensor([0, 1, 0])

dataset = MyDataset(data, labels)
loader = DataLoader(dataset, batch_size=2, shuffle=True)

for batch in loader:
    print(batch)
```

### 9) Serialization 
```
// Save model

torch.save(model.state_dict(), "model.pth")

// Load model

model = nn.Linear(2, 1)
model.load_state_dict(torch.load("model.pth"))
```
### 10) Random 
```
torch.manual_seed(42)
print(torch.rand(2, 2))   # Reproducible random values

print(torch.randperm(5))  # Random permutation
print(torch.randint(0, 10, (3,)))  # Random integers
```

### 11) Utilities 
```
x = torch.tensor([[1, 2, 3], [4, 5, 6]])

print(x.numel())    # 6 (number of elements)
print(x.size())     # torch.Size([2, 3])
print(x.shape)      # (2, 3)
print(x.clone())    # Copy of tensor
print(torch.equal(x, x.clone()))  # True
```
### 12) Pytorch dataset and data loader

🔹 Dataset

- Represents the entire data (images, text, numbers, etc.).

- Defines how to access one sample from the dataset.

- Implements __getitem__(index) → returns one data sample.

- Implements __len__() → returns total number of samples.

- Can be predefined (e.g., torchvision datasets) or custom (subclass Dataset).

- Example: A dataset of 10,000 images where each call gives one image + label.


🔹 DataLoader

- Works as a wrapper around Dataset.

- Provides an iterator over the dataset.

- Loads data in batches instead of one sample.

- Handles shuffling of data.

- Supports parallel loading using num_workers.

- Speeds up training by efficiently preparing batches.

- Example: Instead of fetching 1 image, DataLoader fetches a batch of 64 images at once.

```
from torch.utils.data import Dataset, DataLoader
import torch

// Step 1: Create dataset
class MyDataset(Dataset):
    def __init__(self):
        self.data = torch.arange(10)  # numbers 0-9

    def __len__(self):
        return len(self.data)  # total samples

    def __getitem__(self, idx):
        return self.data[idx]  # single sample

dataset = MyDataset()

// Step 2: Use DataLoader
loader = DataLoader(dataset, batch_size=3, shuffle=True)

// Step 3: Iterate batches
for batch in loader:
    print(batch)  # prints 3 numbers per batch
```

### 13) Components of PyTorch

- Tensors (torch.Tensor) → The basic data structure in PyTorch, similar to NumPy arrays, but with extra features like GPU acceleration.

- Autograd → PyTorch’s automatic differentiation engine that computes gradients for tensors, which is the key for training neural networks.

- Neural Network Module (torch.nn) → A high-level module that provides layers, loss functions, and tools to easily build neural network models.

- Optimizers (torch.optim) → Algorithms like SGD and Adam that update model parameters using the gradients calculated by autograd.

- Data Utilities (torch.utils.data) → Classes like Dataset and DataLoader to handle data loading, batching, and preprocessing efficiently.

- Ecosystem Libraries → Extensions such as TorchVision (for images), TorchText (for language), and TorchAudio (for audio tasks).

- CUDA Support (torch.cuda) → Lets you easily move tensors and models to GPU for faster training and computation.

### 14) Role of Loss Functions in PyTorch

- A loss function (also called a cost function or objective function) is a mathematical function that measures how well the model’s predictions match the target values.
          
- Roles in PyTorch training loop:

          - Measure error → Quantifies the difference between predicted outputs (y_pred) and true labels (y_true).
  
          - Guide optimization → Provides a signal for backpropagation (loss.backward()) so gradients can be calculated.
  
          - Control learning behavior → Different tasks need different losses (classification, regression, segmentation, etc.).
  
          - Impact convergence → The choice of loss affects how fast and how well the model learns.

- Differnt loss functions
  
          - Regression Losses
  
                      - Mean Squared Error Loss
  
                      - Mean Absolute Error Loss
  
          - Classification Losses
  
                      - Cross Entropy Loss
  
                      - Binary Cross Entropy Loss
  
                      - Negative Log Likelihood Loss
  
          - Ranking & Margin Losses
  
                      - Hinge Embedding Loss (nn.HingeEmbeddingLoss)
  
                      - Margin Ranking Loss (nn.MarginRankingLoss)
  
                      - Triplet Margin Loss (nn.TripletMarginLoss) (e.g., face verification, Siamese networks).
  
          - Specialized Losses
  
                      - Huber Loss
  
                      - KL Divergence Loss
  
                      - CTCLoss
  
                      - Dice Loss (custom, not built-in)

### 15) Common Learning Rate Schedules in PyTorch

	a. StepLR

	b. MultiStepLR

	c. ExponentialLR

	d. CosineAnnealingLR

	e. ReduceLROnPlateau

	d. CyclicLR

### 16) what are the different tensor datatypes available in pyTorch?
| **Data Type**                    | **Description**                                    | **Memory Size** | **Default Usage**              | **Example**                                      |
| -------------------------------- | -------------------------------------------------- | --------------- | ------------------------------ | ------------------------------------------------ |
| `torch.float32` / `torch.float`  | 32-bit floating point                              | 4 bytes         | Default for most deep learning | `torch.tensor([1.0, 2.0], dtype=torch.float32)`  |
| `torch.float64` / `torch.double` | 64-bit floating point                              | 8 bytes         | High-precision calculations    | `torch.tensor([1.0, 2.0], dtype=torch.float64)`  |
| `torch.float16` / `torch.half`   | 16-bit floating point (faster GPU training)        | 2 bytes         | Mixed precision training       | `torch.tensor([1.0, 2.0], dtype=torch.float16)`  |
| `torch.bfloat16`                 | 16-bit “brain float” (TPUs/GPU)                    | 2 bytes         | Mixed precision training       | `torch.tensor([1.0, 2.0], dtype=torch.bfloat16)` |
| `torch.int8`                     | 8-bit signed integer                               | 1 byte          | Small integer storage          | `torch.tensor([1, -2], dtype=torch.int8)`        |
| `torch.uint8`                    | 8-bit unsigned integer                             | 1 byte          | Image data / masks             | `torch.tensor([0, 255], dtype=torch.uint8)`      |
| `torch.int16` / `torch.short`    | 16-bit signed integer                              | 2 bytes         | Small integer storage          | `torch.tensor([1000, 2000], dtype=torch.int16)`  |
| `torch.int32` / `torch.int`      | 32-bit signed integer                              | 4 bytes         | General integer storage        | `torch.tensor([1000, 2000], dtype=torch.int32)`  |
| `torch.int64` / `torch.long`     | 64-bit signed integer                              | 8 bytes         | Default for indices            | `torch.tensor([1000, 2000], dtype=torch.int64)`  |
| `torch.bool`                     | Boolean tensor (True/False)                        | 1 byte          | Masks, conditions              | `torch.tensor([True, False], dtype=torch.bool)`  |
| `torch.complex64`                | 64-bit complex number (32-bit real + 32-bit imag)  | 8 bytes         | Scientific computing           | `torch.tensor([1+2j], dtype=torch.complex64)`    |
| `torch.complex128`               | 128-bit complex number (64-bit real + 64-bit imag) | 16 bytes        | High-precision complex numbers | `torch.tensor([1+2j], dtype=torch.complex128)`   |


Some save memory, some provide precesion, some enable GPU Acceleration.

### 17) What is the difference between torch.Tensor and torch.tensor()?

	1) torch.Tensor is the class constructor(like a factory), while tensor.tesor() is a function(like a smart assistance) that infers data types automatically.

	2) torch.Tensor([1,2,3]).dtype // torch.float32

	3) torch.tensor([1, 2, 3]).dtype  //  torch.int64

### 18) How can you convert a Numpy array to a Pytorch tensor and vice versa?

	a) Numpy to torch tensor
	```
		import numpy as np
		numpy_array = np.array([1,2,3,4])
		tensor = torch.from_numpy(numpy_array)
		tensor2 = torch.tensor(numpy_array)
	
	```
	b) torch to numpy
	```
		torch_tensor = torch.tensor([5,6,7,8])
		numpy_back = torch_tensor.numpy()
	```

	c) Combination numpy to tensor and tensor to numpy

	```
		numpy_array = np.array([1,2,3,4])
		torch_tensor = torch.from_numpy(numpy_array)
		numpy_back = torch_tensor.numpy()
	```

### 19) What is a gradient desecnt in pytorch?

	Gradient Descent is an optimization algorithm used to minimize a loss function in machine learning and deep learning.

	A loss function measures how far your model’s predictions are from the true values.

	Gradient descent updates the model’s parameters in the direction that reduces the loss.

### 20) How do you create a tensor in Pytoch

	Pytorch offers multiple ways to forge your data into powerful tensor form, each method serving different purpose.

	data = [[1,2],[3,4]]
	torch.tensor(data)
	torch.zeros(2,3)
	torch.ones(3,2)
	torch.randn(4)
	torch.randn(2, 3)
	torch.randint(3, 5, (3,))  // tensor([4, 3, 4])
	torch.randint(10, (2, 2))  // tensor([[0, 2], [5, 5]])
	torch.randint(3, 10, (2, 2)) // tensor([[4, 5], [6, 7]])

	torch.arange(5) // tensor([ 0,  1,  2,  3,  4])
	torch.arange(1, 4) // tensor([ 1,  2,  3])
	torch.arange(1, 2.5, 0.5) // tensor([ 1.0000,  1.5000,  2.0000])

	input = torch.empty(2, 3)
	torch.zeros_like(input)

	torch.zeros_like(torch.tensor(9)) // 0 is the output.

### 21) torch shape

import torch

// Create a 1D tensor

x = torch.tensor([1, 2, 3, 4, 5, 6])

print("Original tensor x:", x)
print("Shape of x:", x.shape)

// Reshape to a 2x3 matrix

y = torch.reshape(x, (2, 3))
print("\nReshaped tensor y (2x3):", y)
print("Shape of y:", y.shape)

// Reshape using the -1 wildcard

z = x.reshape((3, -1)) # Let PyTorch infer the second dimension
print("\nReshaped tensor z (3x-1):", z)
print("Shape of z:", z.shape)

// Flatten a 2D tensor

matrix = torch.tensor([[1, 2], [3, 4]])

flat_matrix = matrix.reshape(-1) # Flatten to 1D

print("\nOriginal matrix:", matrix)
print("Flattened matrix:", flat_matrix)
print("Shape of flattened matrix:", flat_matrix.shape)

### 22) What is pythorch and how does it differ from the tensorflow
	
	- PyTorch: A Python-based deep learning framework that uses dynamic computation graphs, making it easy and flexible for research and experimentation.

	- TensorFlow: A deep learning framework by Google that originally used static computation graphs, now supports dynamic graphs (eager execution). It’s widely used in production and deployment.
	- pytorch example
	```
		import torch
		x = torch.tensor([2.0], requires_grad=True)
		z = x**3 + 1
		z.backward()
		print("Value of z:", z.item())        
		print("Gradient dz/dx:", x.grad.item())
	```
	- Tensorflow example 

	```
		import tensorflow as tf  
		x = tf.Variable([2.0])
		with tf.GradientTape() as tape:
		    z = x**2 + 1
		dz_dx = tape.gradient(z, x)
		print("Value of z:", z.numpy())        
		print("Gradient dz/dx:", dz_dx.numpy())
	```

### 23) Explain the role of torch.Tensor

	It's a multi-dimensional array that can store numbers, perform mathematical operations, and automatically calculate gradients for macine learning.

	0D tensor → scalar (x = torch.tensor(5))
	1D tensor → vector (x = torch.tensor([1,2,3]))
	2D tensor → matrix (x = torch.tensor([[1,2],[3,4]]))

	x = torch.tensor([1, 2, 3])
	y = x * 2  # element-wise multiply → [2, 4, 6]

### 24) How to handle dimensional error in pytorch 

Check shapes → Always print(tensor.shape) before operations.

Broadcasting → Works if sizes match except for 1, else reshape.

Reshape correctly → Use .view(), .reshape(), .unsqueeze(), .squeeze().

Matrix multiplication → Inner dimensions must match (m, n) @ (n, p).

Concatenation → All tensors must match in every dimension except the one you concat on.

Padding / trimming → Use torch.nn.functional.pad() to equalize sizes.

Batch dimension → Models expect (batch, channels, H, W) → add with .unsqueeze(0).

### 25) Benefits of transfer learning

The main benefits of transfer learning in AI are reduced training time and data requirements, leading to lower computational costs and higher accuracy. By leveraging knowledge from pre-trained models, developers can achieve better performance with less task-specific data, making AI development more efficient and accessible.  

Here's a breakdown of the benefits:

	Reduced Training Time: Instead of training a model from scratch, transfer learning uses pre-trained models, which have already learned general features from large datasets. This allows the new model to learn the target task much faster. 
	
	Less Data Required: Training deep learning models from scratch requires vast amounts of data, which can be expensive and difficult to obtain. Transfer learning enables high-quality results with smaller datasets, making it valuable for tasks where data is limited, such as in specialized domains.
	
	Improved Performance & Accuracy: Models often perform better on the new task because they start with a foundation of learned features and patterns from a related problem. This pre-learned knowledge helps the model generalize more effectively.
	
	Lower Computational Costs: By reducing the need for extensive training and data, transfer learning significantly decreases the computational resources (like processor units and memory) needed to build and train AI models.
	
	Enhanced Generalization: Transfer learning improves a model's ability to handle unseen data, as the pre-trained model has already captured broad patterns from diverse datasets, making it more robust in real-world applications.
	
	Faster Prototyping: The efficiency gains in training time and data requirements allow for faster experimentation and prototyping of new AI applications.

### 26) autograd vs no_grad in PyTorch

autograd → tracks operations for gradients (used in training).

no_grad → disables gradient tracking (used in inference).
```
import torch
import torch.nn as nn

# Simple model
model = nn.Linear(2, 1)

x = torch.tensor([[1.0, 2.0]])

# Training mode (gradients tracked)
y = model(x)
loss = y.mean()
loss.backward()  # computes gradients
print("Grad available:", model.weight.grad is not None)

# Inference mode (no gradients)
with torch.no_grad():
    pred = model(x)
print("Grad tracked in inference:", pred.requires_grad)

```

### 27) Higher order derivatives
```
x = torch.tensor(2.0, requires_grad=True)

y = x**3  # f(x) = x^3
dy_dx = torch.autograd.grad(y, x, create_graph=True)[0]  # first derivative

d2y_dx2 = torch.autograd.grad(dy_dx, x)[0]  # second derivative

print("f(x):", y.item())       # 8
print("dy/dx:", dy_dx.item())  # 3x^2 = 12
print("d²y/dx²:", d2y_dx2.item())  # 6x = 12
```
### 28) Derivate function in pytorch
```
x = torch.tensor(2.0, requires_grad=True)
y = torch.tensor(3.0, requires_grad=True)

// f(x,y) = x^2 * y + y^3
f = x^2 * y + y^3
f.backward()

print("∂f/∂x:", x.grad.item())  # derivative wrt x = 2xy = 2*2*3 = 12
print("∂f/∂y:", y.grad.item())  # derivative wrt y = x^2 + 3y^2 = 4 + 27 = 31
```
### 29) Padding to equal.
```
import torch
from torch.nn.utils.rnn import pad_sequence

sequences = [
    torch.tensor([1, 2, 3]),
    torch.tensor([4, 5]),
    torch.tensor([6])
]

// Pad to equal length
padded = pad_sequence(sequences, batch_first=True, padding_value=0)

print(padded)
```
### 30) Simple model training 
```
import torch
import torch.nn as nn
import torch.optim as optim

- Example data
input = torch.randn(64, 784)  # Batch of 64 samples, each with 784 features
labels = torch.randint(0, 10, (64,))  # Batch of 64 labels (10 classes)

- Simple model
model = nn.Linear(784, 10)  # Input size 784, output size 10 (classification)
loss_fn = nn.CrossEntropyLoss()  # Loss function
optimizer = optim.SGD(model.parameters(), lr=0.01)  # Optimizer

- Training loop (1 step shown for simplicity)
- Forward pass
predictions = model(input)  # Compute predictions
loss = loss_fn(predictions, labels)  # Calculate loss

- Backward pass
optimizer.zero_grad()  # Clear previous gradients
loss.backward()  # Compute gradients

 - Update parameters
optimizer.step()  # Apply optimization step
```

### 31) Difference between pytorch and tensorflow:**
   
a) PyTorch and TensorFlow are two of the most popular deep learning frameworks. Both frameworks have their own strengths and weaknesses, and the best choice for you will depend on your specific needs.
   
     b) PyTorch is a Python-based deep learning framework that is known for its flexibility and ease of use. PyTorch uses a dynamic computation graph, which allows you to create and modify your models on the fly. This makes PyTorch a good choice for rapid prototyping and experimentation.
   
     c) TensorFlow is another Python-based deep learning framework that is known for its scalability and performance. TensorFlow uses a static computation graph, which means that you need to define your model before you can start training it. This can make TensorFlow less flexible than PyTorch, but it also makes TensorFlow more efficient for training large models.

### 32) CUDA using pytorch:**
    
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

### 33) CUDA using tensorflow:**
    
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


### 34) What is a tensor?**
    
      A tensor is a mathematical object representing a multi-dimensional array of numerical values. In the context of machine learning frameworks like TensorFlow and PyTorch, tensors are the fundamental data structures used for computation.

    a) Dimensionality:
    
    b) Data Types:

    c) Operations:

    d) Memory Layout:

    e) Gradient Computation:

### 35) Difference between Tensor and Numpy:**

    Tensors and NumPy arrays are both used to represent multi-dimensional arrays of numerical data, but they have some differences, especially in the context of machine learning frameworks like TensorFlow and PyTorch.

    a) Integration with Deep Learning Frameworks:

    b) Computation on Accelerators:

    c) Automatic Differentiation:

    d) Memory Sharing:

### 36) What is CUDA and why it is used?**
   
    Compute Unified Device Architecture (CUDA) is a parallel computing platform and application programming interface (API) 
	
	that allows software to use certain types of graphics processing units (GPUs) for accelerated general-purpose processing, 
	
	an approach called general-purpose computing on GPUs (GPGPU).

### 37) Tensor CPU to GPU using pythorch and tensorflow:**
```
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
```

### 38) what is the use of activation function in neural network?**

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

### 39) how to prevent cnnimage classification overfittinng using pytorch?

	a) data Augmentation : random crops, rotations, flips, color jittering(torch.transform)

 	b) Regularization : 

  	c) Dropout:

   		1) Use dropout layers in your n/w to randomly set some activation to zero during training.

   	d) Batch normalization: 
    
    	1) Normalize the activations of the layers to improve convergence and regularization.

    	2) Batch Normalization (BatchNorm) is a technique to improve the training of deep neural networks by normalizing the inputs to each layer, which helps in accelerating training and reducing the 				sensitivity to network initialization

    e) Early stopping:

    f) Smaller model: 
      
      	1) Reduce the complexity of your model by decreasing the number of layers or the number of units per layer.

    g) More data:
       	1) Collect more training data if possible to improve generalization.


### 40) how to prevent cnnimage classification underfittinng using pytorch

	a) Increase model complexity:

 	b) Increase Training Duration:

  	c) Learning Rate Tuning:
   
		1) Ensure the learning rate is neither too high nor too low. If too high, the model may converge prematurely to a suboptimal solution. If too low, the model may converge too slowly or get stuck.

  	d) Reduce Regularization:
   		
     	1) If you are using regularization techniques like dropout or weight decay, try reducing them as they can sometimes prevent the model from learning effectively.

  	e) Data Preprocessing:

   	f) Use Pretrained Models:
    
    g) Batch Normalization:

     	
### 41) Machine Learning Epoch
    
    a) In machine learning, an epoch is one complete pass through the entire training dataset during the training process of a model. Training typically involves multiple epochs to improve the model's accuracy.

### 42) How can we get good results using pytorch using pretrained/transfer learning

    a) Leverages Prelearned Features:
        
        Pretrained models are typically trained on large and diverse datasets, such as ImageNet, which contains millions of images across thousands of categories. These models learn a variety of features that are generally useful for many tasks, such as edges, textures, and shapes. When you use a pretrained model, you start with a network that already knows these useful features, providing a strong foundation.

    b) Reduces Training Time:
        Training a deep neural network from scratch can be computationally expensive and time-consuming. Transfer learning allows you to start from an already trained model, requiring only a fraction of the time and computational resources to fine-tune the network for your specific task.

    c) Improves Performance with Limited Data:
        
        When you have a small dataset, training a deep network from scratch can lead to overfitting. Pretrained models, on the other hand, help mitigate this by starting from a set of weights that generalize well, thus needing fewer data to fine-tune the model effectively.

    d) Provides Robust Feature Extraction:
        
        Pretrained models are effective feature extractors. Even if you only retrain the final layers, the earlier layers can provide robust and meaningful features for your specific problem, improving overall model performance.
    
    Practical Steps to Leverage Transfer Learning for Better Results:

        1) Choosing pre-trained model, modify the model, freezing layer, fine tunning, Data augmentation, hyper parameters, Regularization techniques.


### 43) Linear regression
```
import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

// Sample data
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)   // Independent variable
y = np.array([2, 4, 5, 4, 5])                  # Dependent variable

// Create and train model
model = LinearRegression()

model.fit(X, y)

// Predictions
y_pred = model.predict(X)

// Coefficients
print("Slope (m):", model.coef_[0])

print("Intercept (c):", model.intercept_)

// Plot
plt.scatter(X, y, color="blue", label="Data points")
plt.plot(X, y_pred, color="red", label="Regression line")
plt.legend()
plt.show()
```

### 44) Logistic regression 
```
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

// Sample dataset: exam score → pass/fail
X = np.array([[35], [45], [50], [60], [70], [80], [90]])  # Exam scores
y = np.array([0, 0, 0, 1, 1, 1, 1])                       # 0 = Fail, 1 = Pass

// Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

// Train logistic regression
model = LogisticRegression()
model.fit(X_train, y_train)

// Predictions
y_pred = model.predict(X_test)

// Evaluation
print("Predictions:", y_pred)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Report:\n", classification_report(y_test, y_pred))
```

### 45) Perceptron

![Alt text](Perceptron.jpg)

    - Perceptron is a single-layer neural network that computes a weighted sum of inputs, adds a bias, and applies an activation function (originally a step function). It can only classify linearly separable data.

    - MLP (Multi-Layer Perceptron) is a feedforward, fully connected neural network with one or more hidden layers. It uses non-linear activation functions and is trained using backpropagation with gradient descent, allowing it to learn non-linear decision boundaries.

### 46) What is a model in Machine learning.

	In machine learning, a model is essentially a mathematical or computational representation of a system, process, or pattern in data. It’s what “learns” from data and is used to make predictions, classifications, or decisions.

# 🚀 Optimizer Comparison: Gradient Descent vs Momentum vs Adam vs AdamW

## 🔹 1. Gradient Descent (GD)

Answer: Gradient Descent updates parameters directly in the opposite direction of the gradient.

It’s simple but can be slow and may oscillate in narrow valleys.

Formula: θt+1=θt−η∇J(θt)

One-liner: “GD is the baseline optimizer but suffers from slow convergence and zig-zagging.”

This table summarizes the differences between **GD**, **Momentum**, **Adam**, and **AdamW** with equations, strengths, and use cases.

## 🔹 2. Momentum

**Answer:**  
Momentum adds a velocity term (like inertia) so updates don’t just depend on the current gradient but also on past gradients.  

This helps **speed up convergence** and **reduce oscillations** in narrow valleys.

**Formula:**  

- Velocity update:  
  `v(t+1) = β * v(t) + η * ∇J(θ(t))`

- Parameter update:  
  `θ(t+1) = θ(t) - v(t+1)`

**One-liner:**  
“Momentum is like rolling a ball down a hill—it smooths updates and converges faster.”

## 🔹 3. Adam (Adaptive Moment Estimation)

**Answer:**  
Adam combines **Momentum + adaptive learning rates**.  

It maintains running averages of gradients (mean) and squared gradients (variance).  
Each parameter gets its **own learning rate**, making Adam **fast and effective**, especially in NLP and sparse data.

**Formula (simplified):**  

- Compute biased first moment (mean of gradients):  
  `m(t) = β1 * m(t-1) + (1 - β1) * ∇J(θ(t))`

- Compute biased second moment (variance of gradients):  
  `v(t) = β2 * v(t-1) + (1 - β2) * (∇J(θ(t)))^2`

- Bias-corrected moments:  
  `m_hat(t) = m(t) / (1 - β1^t)`  
  `v_hat(t) = v(t) / (1 - β2^t)`

- Parameter update:  
  `θ(t+1) = θ(t) - η * m_hat(t) / (sqrt(v_hat(t)) + ε)`

**One-liner:**  
“Adam adapts the learning rate for each parameter and usually converges quickly.”


## 🔹 4. AdamW

**Answer:**  
Adam originally didn’t handle **weight decay** correctly—it coupled it with adaptive updates.  

**AdamW decouples weight decay**, leading to much better generalization, especially in large models like Transformers.

**Formula (simplified):**  

- Compute biased first moment (mean of gradients):  
  `m(t) = β1 * m(t-1) + (1 - β1) * ∇J(θ(t))`

- Compute biased second moment (variance of gradients):  
  `v(t) = β2 * v(t-1) + (1 - β2) * (∇J(θ(t)))^2`

- Bias-corrected moments:  
  `m_hat(t) = m(t) / (1 - β1^t)`  
  `v_hat(t) = v(t) / (1 - β2^t)`

- Parameter update with **decoupled weight decay**:  
  `θ(t+1) = θ(t) - η * ( m_hat(t) / (sqrt(v_hat(t)) + ε) + λ * θ(t) )`  
  where `λ` is the weight decay factor.

**One-liner:**  
“AdamW is basically Adam with correctly implemented weight decay—it’s the default optimizer for modern deep nets.”


---


## 🔍 Differences Between GD, Momentum, Adam, and AdamW

| Optimizer | Update Rule (simplified) | Key Difference | Pros | Cons | Best Use Case |
|-----------|---------------------------|----------------|------|------|---------------|
| **Gradient Descent (GD)** | θ(t+1) = θ(t) - η ∇J(θ(t)) | Basic gradient step | Simple, easy to understand | Slow, oscillates in narrow valleys | Small/simple ML problems |
| **Momentum** | v(t+1) = β v(t) + η ∇J(θ(t)) <br> θ(t+1) = θ(t) - v(t+1) | Adds "velocity" (inertia) to updates | Faster, smoother convergence | Needs LR tuning | CNNs, vision tasks |
| **Adam** | θ(t+1) = θ(t) - η ( m̂(t) / (√v̂(t)+ε) ) | Combines **momentum + adaptive learning rate** | Fast, works well with sparse gradients | Overfits, weaker generalization | NLP, general DL |
| **AdamW** | θ(t+1) = θ(t) - η ( m̂(t)/(√v̂(t)+ε) + λθ(t) ) | **Adam + decoupled weight decay** | Best generalization, stable | Slightly more hyperparams | Transformers, modern DL |


## 🔑 Interview Quick Recall
- **GD:** Simple, follows gradient, slow.  
- **Momentum:** Adds inertia, smoother and faster.  
- **Adam:** Combines momentum + adaptive learning rate, very fast.  
- **AdamW:** Adam with correct weight decay → better generalization.  

### 46) VLM vs DL

![Alt text]('vlm vs dl.png')

![Alt text]("clm vs dl1.png")




### 47) Why k=10
- In a RAG system, we usually retrieve the top-k most relevant chunks from a vector store — and a common default is k = 10.
The reason is that it balances recall and efficiency. Retrieving too few chunks might miss important context, while retrieving too many adds noise and increases token usage.
Empirically, 10 gives good coverage without overloading the model’s context window or harming response quality.
Of course, the optimal number depends on the data and can be tuned, but 10 is a solid starting point.

### 48) How RNN works
    
    - Gated cells: Instead of a simple feedback loop, LSTMs use a cell state and a system of gates to regulate the flow of information.
    - Forget gate: Decides which information from the previous cell state to discard.
    - Input gate: Decides which new information from the current input to store in the cell state.
    - Output gate: Decides what part of the cell state to output for the next step.
    - Cell state: Acts as a conveyor belt for information, allowing it to flow through the network with minimal changes unless explicitly altered by the gates.

### 49) R-squared (\(R^{2}\))
    
    - is not an "error" but a metric that measures the proportion of the variance in the dependent variable that is predictable from the independent variables in a regression model

# 🔍 Retrieval Methods in RAG — Comparison Table

| Retrieval Method | Type | Similarity Metric | When It Helps (Use Case) | Pros | Cons |
|:------------------|:------|:------------------|:--------------------------|:------|:------|
| **Cosine Similarity** | Dense / Semantic | Measures angle between vectors (normalized) | General-purpose retrieval where embeddings represent semantic meaning | Fast, widely supported, normalization removes magnitude bias | Ignores vector magnitude |
| **Dot Product (Inner Product)** | Dense / Semantic | Measures alignment without normalization | When embeddings are trained using dot product (e.g., OpenAI models) | Efficient, simple | Sensitive to vector magnitude |
| **Euclidean Distance (L2)** | Dense / Numeric | Straight-line distance | When embeddings encode spatial meaning or numeric relationships | Intuitive, works for structured data | Sensitive to scale differences |
| **Manhattan Distance (L1)** | Dense | Sum of absolute differences | Sparse or high-dimensional embeddings | Robust to outliers | Less smooth metric, slower optimization |
| **BM25 / TF-IDF** | Sparse / Lexical | Keyword frequency and document frequency | When exact term match or domain-specific jargon is important | Excellent keyword matching | No semantic understanding |
| **Hybrid (Dense + Sparse)** | Mixed | Weighted combination of dense + lexical scores | Balanced retrieval in real-world RAG systems | Combines semantics + keywords | Slightly complex to tune |
| **Neural Reranker (Cross-Encoder)** | ML-based | Learned relevance score | Second-stage re-ranking for high-precision QA or doc ranking | Very accurate, context-aware | Slow, computationally expensive |
| **Graph-Based Retrieval** | Structural / Knowledge | Traversal of entity relationships | Knowledge-rich or linked data (e.g., ontologies, enterprise KBs) | Understands relationships, logical connections | Requires structured graph data |
| **ANN (Approx. Nearest Neighbor)** | Indexing Technique | Any (Cosine, Dot, L2) | Large-scale retrieval for millions of vectors | Scalable and fast | Slight recall loss |

---

### ✅ Quick Recommendations

| Goal | Recommended Retrieval Setup |
|:------|:-----------------------------|
| Fast semantic search | **Cosine or Dot Product** |
| Domain-specific keyword search | **BM25** |
| Mix of semantics and keywords | **Hybrid (Dense + Sparse)** |
| Highly accurate question answering | **Vector retrieval + Neural Reranker** |
| Large-scale production systems | **ANN-based indexing (e.g., HNSW, IVF)** |
| Knowledge graph or ontology search | **Graph-based retrieval** |

---

### 💡 Tip
In production-grade RAG pipelines:
1. Start with **vector retrieval (cosine or dot product)** for top-k candidates.  
2. Apply a **reranker** for better precision.  
3. Optionally add **BM25** or **hybrid scoring** for better coverage of exact keywords.









