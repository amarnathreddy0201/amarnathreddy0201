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
