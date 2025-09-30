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

          1. A loss function (also called a cost function or objective function) is a mathematical function that measures how well the model’s predictions match the target values.
          
          2. Roles in PyTorch training loop:
          
                    a. Measure error → Quantifies the difference between predicted outputs (y_pred) and true labels (y_true).
          
                    b. Guide optimization → Provides a signal for backpropagation (loss.backward()) so gradients can be calculated.
          
                    c. Control learning behavior → Different tasks need different losses (classification, regression, segmentation, etc.).
          
                    d. Impact convergence → The choice of loss affects how fast and how well the model learns.
          
          3. Differnt loss functions
          
                    a. Regression Losses
                              i. Mean Squared Error Loss
                              ii. Mean Absolute Error Loss
                    b. Classification Losses
                              i. Cross Entropy Loss
                              ii. Binary Cross Entropy Loss
                              iii. Negative Log Likelihood Loss
                    c. Ranking & Margin Losses
                              i. Hinge Embedding Loss (nn.HingeEmbeddingLoss)
                              ii. Margin Ranking Loss (nn.MarginRankingLoss)
                              iii. Triplet Margin Loss (nn.TripletMarginLoss) (e.g., face verification, Siamese networks).
                    d. Specialized Losses
                              i. Huber Loss
                              ii. KL Divergence Loss
                              iii. CTCLoss
                              iv. Dice Loss (custom, not built-in)
